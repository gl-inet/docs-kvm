"""Check a provider's Responses SSE contract without logging secrets or payloads."""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


class PreflightError(RuntimeError):
    """A safe, payload-free error suitable for public Actions logs."""


def check_stream(response) -> None:
    content_type = response.headers.get('Content-Type', '').split(';', 1)[0].strip().lower()
    if content_type != 'text/event-stream':
        raise PreflightError('Expected text/event-stream. Check the full Responses API endpoint and streaming support.')

    data_lines = []
    size = 0
    deadline = time.monotonic() + 60
    # SSE permits multi-line data and CRLF. A final event also needs a blank line.
    for raw in response:
        size += len(raw)
        if size > 1024 * 1024 or time.monotonic() > deadline:
            raise PreflightError('Streaming preflight exceeded its size or time limit. Check provider health.')
        try:
            line = raw.decode('utf-8').rstrip('\r\n')
        except UnicodeDecodeError:
            raise PreflightError('The provider returned invalid UTF-8 in its event stream.') from None
        if line.startswith('data:'):
            data_lines.append(line[5:].lstrip(' '))
        elif not line and data_lines:
            data = '\n'.join(data_lines)
            data_lines = []
            if data == '[DONE]':
                break  # Chat Completions-style termination is not sufficient.
            try:
                event = json.loads(data)
            except ValueError:
                raise PreflightError('The provider returned invalid JSON in its event stream.') from None
            if not isinstance(event, dict):
                raise PreflightError('The provider returned a non-object streaming event.')
            kind = event.get('type')
            if kind == 'response.completed':
                return
            if kind in ('error', 'response.failed', 'response.incomplete'):
                raise PreflightError('The provider reported a failed/incomplete response. Check model access, quota and provider logs.')
    raise PreflightError('Stream closed before response.completed. Check the Responses endpoint, model access and gateway SSE forwarding; [DONE] alone is not sufficient.')


def probe(endpoint: str, api_key: str, model: str) -> None:
    if not api_key or not endpoint or not model:
        raise PreflightError('Configure OPENAI_API_KEY, CODEX_RESPONSES_API_ENDPOINT and CODEX_MODEL in the OpenAI environment.')
    try:
        url = urllib.parse.urlsplit(endpoint)
    except ValueError:
        raise PreflightError('Configure a valid HTTPS Responses API endpoint.') from None
    if url.scheme != 'https' or not url.netloc or url.username or url.password or url.fragment:
        raise PreflightError('Configure CODEX_RESPONSES_API_ENDPOINT as a full HTTPS Responses API URL without embedded credentials or a fragment.')
    request = urllib.request.Request(
        endpoint,
        data=json.dumps({'model': model, 'input': 'Reply with OK.', 'stream': True, 'store': False}).encode('utf-8'),
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json', 'Accept': 'text/event-stream'},
        method='POST',
    )
    # Never forward the bearer token to a redirect target.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=30) as response:
            check_stream(response)
    except urllib.error.HTTPError as exc:
        raise PreflightError(f'Responses API returned HTTP {exc.code}. Check the endpoint, API key, model access and provider logs.') from None
    except (OSError, urllib.error.URLError):
        raise PreflightError('Responses API connection failed or timed out. Check provider availability and runner connectivity.') from None


def main() -> int:
    try:
        probe(os.environ.get('CODEX_RESPONSES_API_ENDPOINT', ''),
              os.environ.get('CODEX_API_KEY', ''), os.environ.get('CODEX_MODEL', ''))
    except PreflightError as exc:
        print(f'::error::{exc}', file=sys.stderr)
        return 1
    print('Responses API streaming preflight passed (response.completed received).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

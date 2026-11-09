# Codex API configuration and troubleshooting {#codex-api-configuration-and-troubleshooting}

The translation and PR-review workflows use environment secrets from the
`OpenAI` GitHub environment:

- `OPENAI_API_KEY`: a narrowly scoped, budget-limited provider API key.
- `CODEX_RESPONSES_API_ENDPOINT`: the full HTTPS Responses API URL, including
  `/v1/responses` when required by the provider, not just a base URL.

Both workflows explicitly use `gpt-6.1-sol`. Optionally set the environment
variable `CODEX_MODEL` to a model supported by the configured endpoint. The
preflight and Codex invocation always select the same model.

## Client compatibility {#client-compatibility}

Both workflows pin Codex CLI and its Responses proxy to `0.166.0`, used by
successful `docs4.x` translation runs. KVM run
[42582342430](https://github.com/gl-inet/docs-kvm/actions/runs/42582342430)
automatically installed `0.167.0` and failed before the first model response.
This pin is a compatibility mitigation, not proof of a CLI bug: secret names
shared across repositories do not establish equal values or provider routing.
Test the configured provider before changing both version pins together.

## Streaming preflight {#streaming-preflight}

Before starting Codex, `scripts/codex_preflight.py` sends a small authenticated
request with `stream: true` and requires an SSE `response.completed` event.
It uses the same endpoint and model as Codex. This consumes a small amount of
API usage, but never prints URLs, credentials, response bodies or model output.
Redirects are refused to avoid forwarding the bearer token to another URL.

The preflight fails early for HTTP errors, non-SSE content, malformed events,
failed/incomplete responses, and streams that close without `response.completed`.
A stream ending with only `[DONE]` does not satisfy this Responses API contract.
A passing probe checks basic streaming only, not compatibility with Codex's
full tool-calling and structured-output requests.

For `stream closed before response.completed`, check the full endpoint URL,
model access, provider health and gateway SSE forwarding. The final
`sudo exited with code 1` wraps Codex's failure and does not by itself identify
a sudo problem. Do not disable privilege reduction or sandboxing to work around
an API stream error.

After publishing workflow fixes, start a new workflow run. Rerunning an old run
reuses its old workflow revision. Verify the preflight and the actual Codex step
before claiming the API problem is resolved.

## Offline tests {#offline-tests}

Run without credentials or network access:

```powershell
python -m unittest discover -s scripts/tests -v
```

import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import urllib.error

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from codex_preflight import PreflightError, check_stream, probe


class Response(io.BytesIO):
    def __init__(self, body, content_type='text/event-stream; charset=utf-8'):
        super().__init__(body)
        self.headers = {'Content-Type': content_type}


class PreflightTests(unittest.TestCase):
    def test_completed_stream(self):
        check_stream(Response(b': keepalive\r\n\r\nevent: response.completed\r\ndata: {"type":\r\ndata: "response.completed"}\r\n\r\n'))

    def test_incomplete_and_invalid_streams(self):
        for body in (b'', b'data: [DONE]\n\n', b'data: {"type":"response.created"}\n\n',
                     b'data: {"type":"response.failed"}\n\n',
                     b'data: {"type":"response.incomplete"}\n\n',
                     b'data: {"type":"error","message":"SECRET"}\n\n',
                     b'data: bad SECRET\n\n', b'data: []\n\n', b'data: \xff\n\n',
                     b'data: {"type":"response.completed"}\n'):
            with self.subTest(body=body), self.assertRaises(PreflightError) as error:
                check_stream(Response(body))
            self.assertNotIn('SECRET', str(error.exception))
        with self.assertRaisesRegex(PreflightError, 'text/event-stream'):
            check_stream(Response(b'{"secret":"hidden"}', 'application/json'))

    @patch('codex_preflight.urllib.request.build_opener')
    def test_request_and_redirect_protection(self, build):
        opener = build.return_value
        opener.open.return_value.__enter__.return_value = Response(b'data: {"type":"response.completed"}\n\n')
        probe('https://provider.example/v1/responses', 'SECRET', 'selected-model')
        request = opener.open.call_args.args[0]
        self.assertEqual(request.get_header('Authorization'), 'Bearer SECRET')
        self.assertEqual(json.loads(request.data), {'model': 'selected-model', 'input': 'Reply with OK.', 'stream': True, 'store': False})
        handler = build.call_args.args[0]
        self.assertIsNone(handler.redirect_request(None, None, 302, '', {}, 'https://other.example'))

    @patch('codex_preflight.urllib.request.build_opener')
    def test_safe_http_and_connection_errors(self, build):
        for code in (302, 401, 403, 404, 429, 500):
            build.return_value.open.side_effect = urllib.error.HTTPError('https://SECRET', code, 'SECRET', {}, None)
            with self.assertRaisesRegex(PreflightError, f'HTTP {code}') as error:
                probe('https://provider.example/v1/responses', 'SECRET', 'model')
            self.assertNotIn('SECRET', str(error.exception))
        build.return_value.open.side_effect = urllib.error.URLError('SECRET')
        with self.assertRaisesRegex(PreflightError, 'connection failed') as error:
            probe('https://provider.example/v1/responses', 'SECRET', 'model')
        self.assertNotIn('SECRET', str(error.exception))

    def test_configuration(self):
        for endpoint, key, model in (('', 'key', 'model'), ('https://provider.example', '', 'model'),
                                     ('https://provider.example', 'key', ''),
                                     ('http://provider.example', 'key', 'model'),
                                     ('https://user:password@provider.example', 'key', 'model')):
            with self.subTest(endpoint=endpoint), self.assertRaises(PreflightError):
                probe(endpoint, key, model)


if __name__ == '__main__':
    unittest.main()

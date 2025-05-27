import unittest
import sys

from app.utils import get_headers, get_header, get_header_data, is_valid_header

class TestHeaderUtilities(unittest.TestCase):

    def test_get_headers_standard_request(self):
        request = (
            "GET /home HTTP/1.1\r\n"
            "Host: example.com\r\n"
            "Connection: keep-alive\r\n"
            "Accept: */*\r\n"
            "\r\n"
        )
        expected = [
            "Host: example.com",
            "Connection: keep-alive",
            "Accept: */*"
        ]
        self.assertEqual(get_headers(request), expected)

    def test_get_headers_only_request_line(self):
        request = "GET /home HTTP/1.1\r\n\r\n"
        self.assertEqual(get_headers(request), [])

    def test_get_headers_empty_string(self):
        request = ""
        self.assertEqual(get_headers(request), [])

    def test_get_header_found(self):
        headers = [
            "Host: example.com",
            "User-Agent: Mozilla/5.0",
            "Accept: text/html"
        ]
        self.assertEqual(get_header(headers, "User-Agent"), "User-Agent: Mozilla/5.0")

    def test_get_header_not_found(self):
        headers = ["Host: example.com"]
        self.assertIsNone(get_header(headers, "Authorization"))

    def test_get_header_case_sensitive(self):
        headers = ["host: example.com"]
        self.assertIsNone(get_header(headers, "Host"))

    def test_get_header_data_basic(self):
        header = "Authorization: Bearer xyz.abc.123"
        self.assertEqual(get_header_data(header), "Bearer")

    def test_get_header_data_with_colon_in_value(self):
        header = "Location: http://example.com:8080"
        self.assertEqual(get_header_data(header), "http://example.com:8080".split(" ")[0])

    def test_get_header_data_with_extra_spaces(self):
        header = "X-Custom-Header:    Token 12345"
        # header.split(":") gives ["X-Custom-Header", "    Token 12345"]
        # value.split(" ") = ["", "", "", "", "Token", "12345"] → index 1 is 'Token'
        self.assertEqual(get_header_data(header), "Token")

    def test_get_header_data_missing_space(self):
        header = "Authorization:BearerToken"
        self.assertEqual(get_header_data(header), "BearerToken")

    def test_get_header_data_malformed(self):
        header = "InvalidHeaderWithoutColon"
        with self.assertRaises(ValueError):
            get_header_data(header)

    def test_valid_headers(self):
        self.assertTrue(is_valid_header("Host: example.com"))
        self.assertTrue(is_valid_header("User-Agent: Mozilla/5.0"))
        self.assertTrue(is_valid_header("Accept: */*"))
        self.assertTrue(is_valid_header("Content-Type: application/json"))
        self.assertTrue(is_valid_header("X-Custom-Header: 123"))

    def test_invalid_headers_no_colon(self):
        self.assertFalse(is_valid_header("Host example.com"))
        self.assertFalse(is_valid_header("Authorization Bearer token"))
        self.assertFalse(is_valid_header("User-Agent Mozilla"))

    def test_invalid_headers_empty_key_or_value(self):
        self.assertFalse(is_valid_header(": value only"))
        self.assertFalse(is_valid_header("Key: "))
        self.assertFalse(is_valid_header("   : value"))
        self.assertFalse(is_valid_header("   :     "))

    def test_header_with_extra_colons(self):
        self.assertTrue(is_valid_header("Location: http://example.com:8080"))
        self.assertTrue(is_valid_header("Auth: Bearer:abc.def"))  # still valid
        self.assertTrue(is_valid_header("A: B: C: D"))

    def test_header_with_whitespace_only(self):
        self.assertFalse(is_valid_header("    "))
        self.assertFalse(is_valid_header("   :    "))

    def test_header_edge_cases(self):
        self.assertFalse(is_valid_header(""))
        self.assertFalse(is_valid_header("\n"))
        self.assertFalse(is_valid_header("::::"))

if __name__ == "__main__":
    unittest.main()

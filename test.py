import unittest
import requests as r
import sys

class WebServerTests(unittest.TestCase):

    def test_webserver_accessible(self):
        res = r.get("http://localhost:5000")
        self.assertTrue(res.text, "Hello World!")

if __name__ == '__main__':
    unittest.main()
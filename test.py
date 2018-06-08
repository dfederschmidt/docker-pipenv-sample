import unittest
import requests as r

class WebServerTests(unittest.TestCase):
    URL = "localhost"

    def test_webserver_accessible(self):
        res = r.get("http://{}:5000".format(URL))
        self.assertTrue(res.text, "Hello World!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        WebServerTests.URL = sys.argv.pop()

    unittest.main()
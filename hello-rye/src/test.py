import unittest

from hello_rye import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('Hello from hello-rye!', hello())

if __name__ == '__main__':
    unittest.main()

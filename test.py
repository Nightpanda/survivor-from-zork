import unittest

class TestClass(unittest.TestCase):
    def test_name(self):
        self.assertEquals(1, 1)

if __name__ == '__main__':
    unittest.main()


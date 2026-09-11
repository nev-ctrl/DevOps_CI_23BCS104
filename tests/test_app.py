import unittest
from src.app import greet, add

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertIn("23BCS104", greet())

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

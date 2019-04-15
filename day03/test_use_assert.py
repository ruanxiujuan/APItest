import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1.0)
        self.assertEqual({"a": 1, "b": 2}, {"b": 2, "a": 1})
        self.assertIn("abc", "abcdefg")
        self.assertTrue(1)
        self.assertFalse({})
        self.assertIsNone(None)


if __name__ == '__main__':
    unittest.main()

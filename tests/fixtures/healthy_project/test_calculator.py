import unittest

from calculator import total


class CalculatorTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([1, 2, 3]), 6)

    def test_empty(self):
        self.assertEqual(total([]), 0)

    def test_rejects_non_numeric(self):
        with self.assertRaises(TypeError):
            total([1, "2"])


if __name__ == "__main__":
    unittest.main()

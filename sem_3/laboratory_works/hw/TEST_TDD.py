import unittest
from main import sum
from main import substract
from main import multiply
from main import diverge
from main import get_mod


class TEST_TDD(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(-4, 16), 12)
        self.assertEqual(substract(314, 24), 290)
        self.assertEqual(multiply(113, 10), 1130)
        self.assertEqual(diverge(121, 11), 11)
        self.assertEqual(diverge(13, 0), 'err')
        self.assertEqual(get_mod(15, 2), 1)


if __name__ == "__main__":
    unittest.main()

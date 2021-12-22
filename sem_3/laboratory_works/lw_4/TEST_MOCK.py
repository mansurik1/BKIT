import unittest
from unittest.mock import Mock

from main import get_roots


class TEST_MOCK(unittest.TestCase):
    def test(self):
        root_mock = Mock(return_value=5)
        get_roots(root_mock(), 5, 5)


if __name__ == "__main__":
    unittest.main()

import unittest
from interview.practice.code.strings.FirstNonRepeatingCharacter import first_non_repeating_character


class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_something(self):
        self.assertEqual('h', first_non_repeating_character("character"))  # add assertion here


if __name__ == '__main__':
    unittest.main()

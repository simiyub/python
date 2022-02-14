import unittest

from interview.real.random.RandomGenerator import RandomGenerator

"""
Tests for RandomGenerator
"""


class TestRandomGenerator(unittest.TestCase):

    def setUp(self):
        self.random_numbers = [-1, 0, 1, 2, 3]
        self.probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
        self.generator = RandomGenerator(self.random_numbers, self.probabilities)

    def test_frequencies(self):

        expected = dict(zip(self.generator.random_values_used(), self.generator.probabilities_used()))

        runs = 100
        actual = {}
        for _ in range(runs):
            val = self.generator.next_num()
            actual[val] = actual.get(val, 0) + 1

        for value, expected_frequency in expected.items():
            actual_frequency = actual.get(value, 0) / runs
            self.assertAlmostEqual(expected_frequency, actual_frequency,
                                   msg=f' value {value} expected {expected_frequency} received {actual_frequency}',
                                   delta=0.1)

if __name__ == '__main__':
    unittest.main()

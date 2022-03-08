import unittest
from interview.practice.code.arrays.TournamentWinner import winner


class TestTournamentWinner(unittest.TestCase):
    def test_winner(self):
        self.assertEqual('C', winner([['A', 'B'], ['A', 'C'], ['B', 'C']], [0, 0, 0]))  # add assertion here


if __name__ == '__main__':
    unittest.main()

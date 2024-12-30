import unittest
from blockBlastSolver import checkClear

class Tests(unittest.TestCase):
    def test_checkClear_1(self):
        game = [[0, 1], [0, 1]]
        expected = [[0, 0], [0, 0]]
        
        checkClear(game)
        self.assertEqual(game, expected)

    def test_checkClear_2(self):
        game = [[1, 0], [1, 0]]
        expected = [[0, 0], [0, 0]]

        checkClear(game)
        self.assertEqual(game, expected)

    def test_checkClear_3(self):
        game = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        checkClear(game)
        self.assertEqual(game, expected)

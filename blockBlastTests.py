import unittest
from blockBlastSolver import checkClear, createGame

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

    def test_createGame_1(self):
        game = createGame(4, 2)
        expected = [[0, 0], [0, 0], [0, 0], [0, 0]]

        self.assertEqual(game, expected)

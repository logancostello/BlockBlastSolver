import unittest
from blockBlastSolver import checkClear, createGame, canPlayPiece, playPiece

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

    def test_playPiece_1(self):
        game = createGame(2, 2)
        playPiece(game, 0, 0, [[0, 0]])
        expected = [[1, 0], [0, 0]]

        self.assertEqual(game, expected)

    def test_playPiece_2(self):
        game = createGame(2, 2)
        playPiece(game, 0, 0, [[0, 0], [1, 0], [0, 1], [1, 1]])
        expected = [[1, 1], [1, 1]]

        self.assertEqual(game, expected)

    def test_canPlayPiece_1(self):
        game = createGame(2, 2)
        piece = [[0, 0]]

        self.assertTrue(canPlayPiece(game, 0, 0, piece))
        self.assertTrue(canPlayPiece(game, 1, 1, piece))
        self.assertFalse(canPlayPiece(game, 2, 2, piece))

    def test_canPlayPiece_2(self):
        game = createGame(3, 3)
        playPiece(game, 0, 0, [[0, 0]])
        piece = [[0, 0]]

        self.assertFalse(canPlayPiece(game, 0, 0, piece))
   
    def test_canPlayPiece_3(self):
        game = createGame(3, 3)
        playPiece(game, 0, 0, [[1, 1]])
        
        self.assertTrue(canPlayPiece(game, 0, 0, [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]]))
        self.assertFalse(canPlayPiece(game, 0, 0, [[0, 0], [1, 0], [0, 1], [1, 1]]))













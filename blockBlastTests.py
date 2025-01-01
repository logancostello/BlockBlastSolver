import unittest
from blockBlastSolver import checkClear, createGame, canPlayPiece, playPiece, scoreCurrentState, findBestMove, findBestMovesInOrder

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

    def test_scoreCurrentState_1(self):
        game1 = createGame(3, 3)
        game2 = createGame(3, 3)
        game3 = createGame(3, 3)
        playPiece(game2, 0, 0, [[0, 0]])
        playPiece(game3, 1, 1, [[0, 0]])

        self.assertTrue(scoreCurrentState(game1) > scoreCurrentState(game2))
        self.assertTrue(scoreCurrentState(game2) > scoreCurrentState(game3))

    def test_scoreCurrentState_2(self):
        game1 = createGame(2, 2)
        game2 = createGame(2, 2)
        piece = [[0, 0], [1, 0]]
        playPiece(game1, 0, 0, piece)
        playPiece(game2, 0, 1, piece)

        self.assertEqual(scoreCurrentState(game1), scoreCurrentState(game2))

    def test_scoreCurrentState_3(self):
        game1 = createGame(2, 2)
        game2 = createGame(2, 2)
        playPiece(game1, 0, 0, [[0, 0], [1, 0]])
        playPiece(game2, 0, 0, [[0, 0], [1, 1]])

        self.assertTrue(scoreCurrentState(game1) > scoreCurrentState(game2))

    def test_findBestMove_1(self):
        game = createGame(2, 2)
        piece = [[0, 0], [1, 0], [0, 1]]
        pos, score = findBestMove(game, piece)

        self.assertEqual(pos, [0, 0])

    def test_findBestMove_2(self):
        game = createGame(3, 3)
        piece = [[1, 0], [0, 1], [1, 1], [1, 2]]

        pos, score = findBestMove(game, piece)

        self.assertEqual(pos, [1, 0])

    def test_findBestMove_3(self):
        game = createGame(3, 3)
        playPiece(game, 0, 0, [[0, 0], [0, 1]])
        piece = [[0, 0]]
        pos, score = findBestMove(game, piece)

        self.assertEqual(pos, [0, 2])

    def test_findBestMove_4(self):
        game = createGame(1, 1)
        pos, score = findBestMove(game, [[0, 0], [1, 0]])

        self.assertEqual(pos, None)
        self.assertEqual(score, float('-inf'))

    def test_findBestMovesInOrder_1(self):
        game = createGame(3, 3)
        piece1 = [[0, 0], [1, 0], [1, 1], [0, 1]]
        piece2 = [[0, 2], [1, 2], [2, 2], [2, 0], [2, 1]]
        pieces = [piece1, piece2]

        moves, score = findBestMovesInOrder(game, pieces)

        self.assertEqual(moves, [[0, 0], [0, 0]])

    def test_findBestMovesInOrder_2(self):
        game = createGame(4, 4)
        piece = [[0, 0]]
        pieces = [piece, piece, piece, piece]

        moves, score = findBestMovesInOrder(game, pieces)
        
        self.assertEqual(score, scoreCurrentState(game))



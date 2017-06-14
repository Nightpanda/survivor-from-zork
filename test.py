import unittest
from survivor import changeBoard

board = [[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1]]

class TestClass(unittest.TestCase):
    def test_changesBoardPositionToChar(self):
	print board
	newBoard = changeBoard('2,2', 'x')
	print newBoard
        self.assertEquals(newBoard[2][2], 'x')

if __name__ == '__main__':
	unittest.main()

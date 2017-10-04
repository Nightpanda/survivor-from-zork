import unittest
from survivor import changeBoard, wizardLegalMovesFor, isCoordinateOutsideGrid, isMoveLegalWizard

board = [[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 1]]

class TestClass(unittest.TestCase):
    def test_changesBoardPositionToChar(self):
	newBoard = changeBoard('2,2', 'x')
        self.assertEquals(newBoard[2][2], 'x')

    def test_wizardLegalMovesFor(self):
        self.assertEquals(wizardLegalMovesFor('0,0'), [[1,2], [2,1]])
        self.assertEquals(wizardLegalMovesFor('2,2'), [[3,0], [1,0], [0,3], [0,1]])

    def test_isCoordinateOutsideGrid(self):
        self.assertEquals(isCoordinateOutsideGrid([-1,2]), True)
        self.assertEquals(isCoordinateOutsideGrid([-1,-2]), True)
        self.assertEquals(isCoordinateOutsideGrid([2,-1]), True)
        self.assertEquals(isCoordinateOutsideGrid([3,4]), True)
        self.assertEquals(isCoordinateOutsideGrid([4,1]), True)
        self.assertEquals(isCoordinateOutsideGrid([0,3]), False)

    def test_isMoveLegalWizard(self):
        self.assertEquals(isMoveLegalWizard('0,0', '1,1'), False)
        self.assertEquals(isMoveLegalWizard('0,0', '2,1'), True)

if __name__ == '__main__':
	unittest.main()

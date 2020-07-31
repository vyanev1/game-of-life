from cell import Cell
from copy import deepcopy


class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._environment = [[Cell(x, y) for x in range(self._columns)] for y in range(self._rows)]

    def generateCells(self, inputMatrix):
        for y in range(self._rows):
            for x in range(self._columns):
                cellState = inputMatrix[y][x]

                if cellState == 1:
                    self._environment[y][x].setColor('green')

    def draw(self):
        for row in self._environment:
                print(f'{[int(cell) for cell in row]}')
        print()  # move to new line

    def getCell(self, x, y):
        return self._environment[y][x]

    def getNeighbours(self, x, y):
        neighbours = []
        for row in range(-1, 2):
            for column in range(-1, 2):
                neighbour_coordX = column + x
                neighbour_coordY = row + y

                if neighbour_coordX == x and neighbour_coordY == y:
                    continue
                elif neighbour_coordX < 0 or neighbour_coordX >= self._columns:
                    continue
                elif neighbour_coordY < 0 or neighbour_coordY >= self._rows:
                    continue
                else:
                    neighbours.append(self.getCell(neighbour_coordX, neighbour_coordY))
        return neighbours

    def update(self):
        gridCache = deepcopy(self)
        for row in self._environment:
            for cell in row:
                neighbours = gridCache.getNeighbours(cell.coordX, cell.coordY)
                cell.updateState(neighbours)
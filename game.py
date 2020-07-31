from grid import Grid


class Game:
    def __init__(self, sizeX, sizeY, inputMatrix):
        self.generation = 0
        self.grid = Grid(sizeX, sizeY)
        self.grid.generateCells(inputMatrix)
        self.targetCount = 0

    def toNextGeneration(self):
        self.grid.update()
        self.generation += 1

    def updateState(self, targetX, targetY):
        color = self.grid.getCell(targetX, targetY).color
        if color == 'green':
            self.targetCount += 1
        self.toNextGeneration()
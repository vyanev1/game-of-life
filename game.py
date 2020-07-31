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


if __name__ == '__main__':
    # grid size
    sizeX, sizeY = input().strip().split(',')
    sizeX = int(sizeX)
    sizeY = int(sizeY)

    # initial state input (generation zero)
    inputMatrix = []
    for _ in range(sizeY):
        inputMatrix.append([int(cell) for cell in input().strip()])

    # get target cell coordinates and number of generations that will be played
    targetX, targetY, N = input().strip().split(',')
    targetX = int(targetX)
    targetY = int(targetY)
    N = int(N)

    # Initiate the game and play for N generations
    game = Game(sizeX, sizeY, inputMatrix)
    while game.generation <= N:
        game.updateState(targetX, targetY)

    print(game.targetCount)
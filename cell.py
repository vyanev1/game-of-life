class Cell:
    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y
        self.color = 'red'  # initialize all cells to be red on object creation

    def setColor(self, newColor):
        self.color = newColor

    def updateState(self, neighbours: list):
        greenNeighbours = 0

        for cell in neighbours:
            if cell.color == 'green':
                greenNeighbours += 1

        if self.color == 'red':
            if greenNeighbours in (3, 6):
                self.setColor('green')
        elif self.color == 'green':
            if greenNeighbours not in (2, 3, 6):
                self.setColor('red')

    def __int__(self):
        if self.color == 'green':
            return 1
        elif self.color == 'red':
            return 0
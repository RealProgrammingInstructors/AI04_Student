import pygame

class Apple(object):
    #x and y should be grid position
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self, surface, grid):
        # calculate the world position of the apple
        x = int(grid.grid[self.x][self.y].x + 0.1 * grid.cellWidth)
        y = int(grid.grid[self.x][self.y].y + 0.1 * grid.cellHeight)
        # render it
        pygame.draw.rect(surface, (255, 0, 0), [x, y, int(grid.cellWidth * 0.8), int(grid.cellHeight * 0.8)])

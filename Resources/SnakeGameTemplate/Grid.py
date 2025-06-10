import pygame

class GridCell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0 #state 0 is nothing, 1 is apple, -1 means occupied by the player

    def display(self, surface, cell_width, cell_height):
        pygame.draw.rect(surface, (0,0,0), [self.x, self.y, cell_width, cell_height], 1)

class Grid(object):
    def __init__(self, columns, rows, width, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height

        self.cellWidth = width / columns #though columns go up and down, how many of them we have go left and right
        self.cellHeight = height / rows

        #we'll start the grid as an empty list and append lists to the lists to make a 2D list
        self.grid = []
        #loops over the columns, adding a list of row for each of them, allowing us to access it [x][y]
        for x in range(columns):
            self.grid.append([])
            #add to the new list
            for y in range(rows):
                self.grid[x].append(GridCell(x*self.cellWidth, y*self.cellHeight))

    def display(self, surface):
        for x in range(self.columns):
            for y in range(self.rows):
                self.grid[x][y].display(surface, self.cellWidth, self.cellHeight)

    def get_grid(self):
        new_grid = []
        for x in range(self.columns):
            new_grid.append([])
            #add to the new list
            for y in range(self.rows):
                new_grid[x].append(self.grid[x][y].state)

        return new_grid
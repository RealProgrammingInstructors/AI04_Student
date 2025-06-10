import pygame
from Grid import Grid, GridCell

class Piece(object):
    #the x and y here should probably be grid location not acutal location
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.previousX = x
        self.previousY = y
        self.colour = colour
        self.child = None

    #moves the piece
    def move(self, newX, newY):
        #continue down the chain of the rest of the tail
        if self.child is not None:
            self.child.move(self.x, self.y)
        #set the previous position, used when adding a new item to the end of the tail
        self.previousX = self.x
        self.previousY = self.y
        self.x = newX
        self.y = newY

    #adds a new piece to the end of the tail
    def grow(self):
        #if this is the end of the tail, add a new piece behind you
        if self.child is None:
            self.child = Piece(self.previousX, self.previousY, self.colour)
        #otherwise tell the next piece of the tail to grow
        else:
            self.child.grow()

    #draws the piece
    def display(self, surface, grid):
        #calculate the world position of the piece
        x = int(grid.grid[self.x][self.y].x)
        y = int(grid.grid[self.x][self.y].y)
        #render it
        pygame.draw.rect(surface, self.colour, [x, y, int(grid.cellWidth), int(grid.cellHeight)])
        #tell the child node to also display
        if self.child is not None:
            self.child.display(surface, grid)

class Player(Piece):
    def __init__(self, x, y, colour, childColour):
        super().__init__(x, y, colour)
        self.direction = None

        #move the player's previous position over by 1 on x to add a child
        self.previousX = x - 1
        #have the player grow
        self.grow()
        #reset the child's colour to have the tail and head be different colours
        self.child.colour = childColour
        #move the child's previous position over by 1 on x to add another child (so starting size is 3)
        self.child.previousX = self.child.x - 1
        #just calling grow on the player should grow to the end of the tail
        self.grow()

    #change what the player is doing
    def act(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == 0: #right
            super().move(self.x + 1, self.y)
        elif self.direction == 1: #up
            super().move(self.x, self.y-1)
        elif self.direction == 2: #left
            super().move(self.x - 1, self.y)
        elif self.direction == 3: #down
            super().move(self.x, self.y + 1)








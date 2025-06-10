import pygame
from Grid import Grid
from Player import Player, Piece
from Apple import Apple
from Controller import Controller
import random

class SnakeGame(object):
    def __init__(self, controller, min_distance):
        self.controller = controller
        self.min_distance = min_distance
        pygame.init()
        pygame.display.set_caption('Snake')
        self.font = pygame.font.SysFont("Arial", 30)
        self.width = 500
        self.height = 500
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.columns = 20
        self.rows = 20
        self.score = 0
        self.reset()

    def reset(self):
        #reset the score to 0
        self.score = 0
        #create the grid
        self.grid = Grid(self.columns, self.rows, self.width, self.height)
        #start the player 3 in and half way up
        self.player = Player(2, int(self.rows / 2), (148, 186, 247), (0, 0, 180))
        #spawn the apple
        self.spawnApple()
        #tell the controller about the game state (used only for the ai)
        self.controller.setGameState(self.grid, self.player, self.apple)


    def spawnApple(self):
        #make sure the apple is at least a certain distance away and not inside of the player
        invalid = True
        while invalid:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns-1)

            #make sure the random x and y is far enough away
            distance = abs(x - self.player.x) + abs(y - self.player.y)
            if distance < self.min_distance:
                continue

            #and that it isn't inside of the player
            if self.grid.grid[x][y].state == 0:
                invalid = False
                self.apple = Apple(x, y)
                self.grid.grid[x][y].state = 1

    def clearGridOfPlayer(self):
        for x in range(len(self.grid.grid)):
            for y in range(len(self.grid.grid[x])):
                if self.grid.grid[x][y].state == -1:
                    self.grid.grid[x][y].state = 0

    def fillGridWithPlayer(self):
        currentPiece = self.player
        while currentPiece is not None:
            self.grid.grid[currentPiece.x][currentPiece.y].state = -1
            currentPiece = currentPiece.child

    def update(self):
        did_reset = False

        #update how the player should be moving
        direction = self.controller.getDirection(self.player.direction)
        if direction is not None:
            self.player.act(direction)

        #move the player
        self.player.move()


        #check the player hasn't move out of bounds, restarting the game if they have
        if self.player.x < 0 or self.player.y < 0 or self.player.x >= self.columns or self.player.y >= self.rows:
            print(f"Game Over: out of bounds, Score: {self.score}")
            self.controller.reset(self.score)
            self.reset()
            did_reset = True


        #check that the player hasn't hit themselves, restarting the game if they have, the none check prevents automatic loss before the game even starts
        if self.grid.grid[self.player.x][self.player.y].state == -1 and self.player.direction is not None:
            print(f"Game Over: hit yourself, Score: {self.score}")
            self.controller.reset(self.score)
            self.reset()
            did_reset = True

        #check that the player has eaten the apple
        if self.player.x == self.apple.x and self.player.y == self.apple.y:
            #mark the spot in the grid as a player spot not an apple spot
            self.grid.grid[self.apple.x][self.apple.y].state = -1
            #spawn a new apple
            self.spawnApple()
            #make the player grow
            self.player.grow()
            #gain a point
            self.score += 1
            #and tell the controller it has eaten (used only for the ai)
            self.controller.eat()

        #clear the grid from last frame and refill it with this frame's data
        self.clearGridOfPlayer()
        self.fillGridWithPlayer()

        #tell the controller about the new game state (used only for the ai)
        self.controller.setGameState(self.grid, self.player, self.apple)

        #return wheter or not we reset or had a game over this frame
        return did_reset


    def display(self):
        #clear colour
        self.surface.fill((255, 255, 255))

        #draw the grid
        #self.grid.display(self.surface)

        #draw the player
        self.player.display(self.surface, self.grid)

        #draw the apple
        self.apple.display(self.surface, self.grid)

        #draw the score
        text = "Score: " + str(self.score)
        text_img = self.font.render(text, True, (0,0,0))
        self.surface.blit(text_img, (0, 0))

        pygame.display.flip()
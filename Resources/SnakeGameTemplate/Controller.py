import pygame
from Grid import Grid, GridCell
from Player import Player
from Apple import Apple

class Controller(object):
    def __init__(self):
        self.resetEvents()
        self.gameState = None

    #we will override this function seperately for the AI and Human controllers
    def getDirection(self, current_direction):
        return None

    def resetEvents(self):
        self.w = False
        self.s = False
        self.d = False
        self.a = False

    def readEvent(self, event):
        if event.key == pygame.K_w:
            self.w = True
        if event.key == pygame.K_s:
            self.s = True
        if event.key == pygame.K_a:
            self.a = True
        if event.key == pygame.K_d:
            self.d = True


    #will override this for the ai controller
    def setGameState(self, grid, player, apple):
        self.gameState = None

    def reset(self, score):
        self.resetEvents()
        self.gameState = None

    #will override this for the ai controller to give points when the ai eats an apple
    def eat(self):
        pass
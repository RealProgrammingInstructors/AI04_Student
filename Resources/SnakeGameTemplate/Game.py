import pygame
from Snake import SnakeGame
from HumanController import HumanController

fps = 20 #target maximum fps, set to 20 for human players, set as high as possible for AI training
fpsClock = pygame.time.Clock() #used to control the maximum fps

controller = HumanController()
game = SnakeGame(controller, 3)

#game loop
running = True
while running:
    #check all of window events
    for event in pygame.event.get():
        #if they pressed a key
        if event.type == pygame.KEYDOWN:
            #and it was escape then close the game
            if event.key == pygame.K_ESCAPE:
                running = False
            #otherwise have the controller process the keyboard input
            else:
                game.controller.readEvent(event)
        #if they hit the red exit, close the game
        elif event.type == pygame.QUIT:
            running = False

    #update the game
    game_ended = game.update()
    game.display()

    #limit the framerate
    fpsClock.tick(fps)
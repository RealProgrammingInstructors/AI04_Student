from Controller import Controller

class HumanController(Controller):
    def __init__(self):
        super().__init__()

    #overloading the function and allowing polymorpihsm to decide which to use
    def getDirection(self, current_direction):
            if self.w and current_direction != 3: # if trying to go up and not currently going down
                self.resetEvents()
                return 1 #up
            if self.a and current_direction != 0: # if trying to go left and not currently going right
                self.resetEvents()
                return 2 #left
            if self.s and current_direction != 1: # if trying to go down and not currently going up
                self.resetEvents()
                return 3 #down
            if self.d and current_direction != 2: # if trying to go right and not currently going left
                self.resetEvents()
                return 0 #right
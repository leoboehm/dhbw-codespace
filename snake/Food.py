import random

class Food:
    windowWidth = 0
    windowHeight = 0
    x = None
    y = None
    active = False

    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth-30
        self.windowHeight = windowHeight-30
        self.x = int(self.windowWidth/2)
        self.y = int(self.windowHeight/2)

    def setNewPos(self):
        self.x = random.randint(0, int(self.windowWidth/30)) * 30
        self.y = random.randint(0, int(self.windowHeight/30)) * 30
        self.active = True
    

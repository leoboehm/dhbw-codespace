import random

class Food:
    x = None
    y = None
    active = False

    def setNewPos(self):
        self.x = random.randint(0, 25) * 30
        self.y = random.randint(0, 25) * 30
        self.active = True
    

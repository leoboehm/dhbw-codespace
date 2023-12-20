import random

class Food:
    x = None
    y = None
    active = False

    def setNewPos(self):
        self.x = random.randint(0, 770)
        self.y = random.randint(0, 770)
        self.active = True
    

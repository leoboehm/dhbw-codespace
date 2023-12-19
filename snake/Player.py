
class Player:
    x = 380
    y = 380
    speed = 1
    
    def moveRight(self):
        self.x += self.speed

    def moveLeft(self):
        self.x -= self.speed
    
    def moveUp(self):
        self.y += self.speed
    
    def moveDown(self):
        self.y -= self.speed
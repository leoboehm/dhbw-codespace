
class Player:
    x = 380
    y = 380
    speed = 0.2
    
    def moveRight(self):
        if self.x < 760:
            self.x += self.speed

    def moveLeft(self):
        if 0 < self.x:
            self.x -= self.speed
    
    def moveUp(self):
        if 0 < self.y:
            self.y -= self.speed
    
    def moveDown(self):
        if self.y < 760:
            self.y += self.speed
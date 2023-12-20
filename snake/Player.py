
class Player:
    x = 385
    y = 385
    speed = 0.1
    length = 1
    
    def moveRight(self):
        if self.x < 770:
            self.x += self.speed

    def moveLeft(self):
        if 0 < self.x:
            self.x -= self.speed
    
    def moveUp(self):
        if 0 < self.y:
            self.y -= self.speed
    
    def moveDown(self):
        if self.y < 770:
            self.y += self.speed
    
    def eatFood(self):
        self.length += 1
        
        if self.length % 2 == 1:
            self.speed += 0.05

class Player:
    x = [385]
    y = [385]
    speed = 30
    length = 1
    direction = 0
    updateCount = 0
    updateCountMax = 2
    
    def update(self):
        self.updateCount += 1
        if self.updateCount < self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.speed
            if self.direction == 1:
                self.x[0] = self.x[0] - self.speed
            if self.direction == 2:
                self.y[0] = self.y[0] - self.speed
            if self.direction == 3:
                self.y[0] = self.y[0] + self.speed

            self.updateCount = 0
        
    def moveRight(self):
        if self.x[0] < 770 and not self.direction == 1:
            self.direction = 0
            self.update()

    def moveLeft(self):
        if 15 < self.x[0] and not self.direction == 0:
            self.direction = 1
            self.update()
    
    def moveUp(self):
        if 15 < self.y[0] and not self.direction == 3:
            self.direction = 2
            self.update()
    
    def moveDown(self):
        if self.y[0] < 770 and not self.direction == 2:
            self.direction = 3
            self.update()
    
    def eatFood(self):
        self.length += 1
        self.x.append(0)
        self.y.append(0)
        self.update()
    
    def draw(self, surface, image):
        for i in range(self.length):
            surface.blit(image, (self.x[i], self.y[i]))
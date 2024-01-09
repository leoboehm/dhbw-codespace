import pygame
from pygame.locals import *
import time
from Player import *
from Food import *

class App:
    windowWidth = 0
    windowHeight = 0
    
    player = 0
    score = 0

    def __init__(self):
        pygame.init()
        pinfo = pygame.display.Info()

        self.windowWidth = pinfo.current_w -10
        self.windowHeight = pinfo.current_h -100

        self._running = True
        self._display = None
        self._playerImg = None
        self._foodImg = None
        self.player = Player(self.windowWidth, self.windowHeight)
        self.food = Food(self.windowWidth, self.windowHeight)
    
    def on_init(self):
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._playerImg = pygame.image.load("./img/body.png")
        self._foodImg = pygame.image.load("./img/apple.png")

    def on_render(self):
        pygame.display.set_caption("Snake Score: " + str(self.score))
        self._display.fill((0, 0, 0))
        self.player.draw(self._display, self._playerImg)
        self._display.blit(self._foodImg, (self.food.x, self.food.y))
        pygame.display.flip()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def spawnFood(self):
        if not self.food.active:
            self.food.setNewPos()

    def checkCollision(self):
        # food collision, player eats food
        if self.food.x - 15 < self.player.x[0] < self.food.x + 15 and self.food.y - 15 < self.player.y[0] < self.food.y + 15:
            self.score += 1
            self.player.eatFood()
            self.food.active = False
        
        # player collision, game ends
        for i in range(1, self.player.length):
            if self.player.x[0] == self.player.x[i] and self.player.y[0] == self.player.y[i]:
                self._running = False

    def play(self):
        if self.on_init() == False:
            self._running = False
        
        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            self.spawnFood()

            if keys[K_RIGHT]:
                self.player.moveRight()
            if keys[K_LEFT]:
                self.player.moveLeft()
            if keys[K_UP]:
                self.player.moveUp()
            if keys[K_DOWN]:
                self.player.moveDown()

            if keys[K_ESCAPE]:
                self._running = False
            
            pass
            self.checkCollision()
            self.on_render()

            time.sleep (100.0 / 1000.0)

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.play()    

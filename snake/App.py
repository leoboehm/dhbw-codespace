import pygame
from pygame.locals import *
import asyncio
from Player import *
from Food import *

class App:

    windowWidth = 800
    windowHeight = 800
    player = 0
    score = 0

    def __init__(self):
        self._running = True
        self._display = None
        self._playerImg = None
        self._foodImg = None
        self.player = Player()
        self.food = Food()
    
    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._playerImg = pygame.image.load("./img/redSquare.png")
        self._foodImg = pygame.image.load("./img/pinkSquare.png")

    def on_render(self):
        pygame.display.set_caption("Snake Score: " + str(self.score))
        self._display.fill((0, 0, 0))
        self._display.blit(self._playerImg, (self.player.x, self.player.y))
        self._display.blit(self._foodImg, (self.food.x, self.food.y))
        pygame.display.flip()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def spawnFood(self):
        if not self.food.active:
            self.food.setNewPos()

    def comparePos(self):
        if (self.food.x - 15 < int(self.player.x) < self.food.x + 15) and (self.food.y - 15 < int(self.player.y) < self.food.y + 15):
            self.score += 1
            self.player.eatFood()
            self.food.active = False

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
            self.comparePos()
            self.on_render()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.play()    

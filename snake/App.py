import pygame
from pygame.locals import *
from Player import *

class App:

    _running = False
    _display = None
    _img = None

    windowWidth = 800
    windowHeight = 800
    player = None

    def __init__(self):
        # start game and create player
        self._running = True
        self.player = Player()

        pygame.init()
        self._img = pygame.image.load("./img/redSquare.png")
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._display.fill((0, 0, 0))
        self._display.blit(self._img, (self.player.x, self.player.y))
        pygame.display.flip()
        pygame.display.set_caption("Snake")


    def play(self):
        if self.__init__ == False:
            self._running = False
        
        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

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

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.play()    

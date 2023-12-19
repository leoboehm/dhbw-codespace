import pygame
from pygame.locals import *
from Player import *

class App:

    windowWidth = 800
    windowHeight = 800
    player = 0

    def __init__(self):
        # start game and create player
        self._running = True
        self._display = None
        self._img = None
        self.player = Player()
    
    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._img = pygame.image.load("./img/redSquare.png")
        pygame.display.set_caption("Snake")

    def on_render(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self._img, (self.player.x, self.player.y))
        pygame.display.flip()
    
    def on_loop(self):
        pass

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False


    def play(self):
        if self.on_init() == False:
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

            self.on_loop()
            self.on_render()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.play()    

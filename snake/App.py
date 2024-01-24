import pygame
from pygame.locals import *
import time
from Player import *
from Food import *

class App:
    windowWidth = 0
    windowHeight = 0
    
    score = 0

    def __init__(self):
        pygame.init()
        pinfo = pygame.display.Info()
        self.fontSmall = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.fontMid = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.fontBig = pygame.font.Font(pygame.font.get_default_font(), 48)

        self.windowWidth = pinfo.current_w -10
        self.windowHeight = pinfo.current_h -100

        self._running = True
        self.started = False
        self.lost = False
        self._display = None
        self._playerImg = None
        self._foodImg = None
        self.player = Player(self.windowWidth, self.windowHeight)
        self.food = Food(self.windowWidth, self.windowHeight)
    
    def on_init(self):
        self._display = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._playerImg = pygame.image.load("./img/body.png")
        self._foodImg = pygame.image.load("./img/apple.png")
        self._snakeImg = pygame.image.load("./img/snake.png")

    def on_render(self):
        pygame.display.set_caption("Snake")

        if self.started:
            self.renderIngameScreen()
        
        elif self.lost:
            self.renderEndScreen()
            
        else:
            self.renderStartScreen()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def start(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            pygame.event.pump()
            
            self.on_render()
            
            if self.started:
                self.play()

            if not self.started and not self.lost:
                keys = pygame.key.get_pressed()

                if keys[K_SPACE]:
                    self.started = True

                if keys[K_ESCAPE]:
                    self._running = False
            
            if self.lost:
                keys = pygame.key.get_pressed()

                if keys[K_SPACE]:
                    self.lost = False

                if keys[K_ESCAPE]:
                    self._running = False
                 
        pygame.quit()

    def play(self):
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

    def renderStartScreen(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self._snakeImg, (self.windowWidth-320, self.windowHeight-380))
        self._display.blit(self.fontBig.render("Welcome to Snake!", True, (50, 200, 0)), (50,50))
        self._display.blit(self.fontMid.render("Instructions:", True, (50, 200, 200)), (50,160))
        self._display.blit(self.fontSmall.render("- To start the game, press [SPACE]", True, (50, 200, 200)), (50,220))
        self._display.blit(self.fontSmall.render("- Move the snake using arrow keys", True, (50, 200, 200)), (50,260))
        self._display.blit(self.fontSmall.render("- To exit the game, press [ESC]", True, (50, 200, 200)), (50,300))
        self._display.blit(self.fontSmall.render("Eat as many apples as possible without biting your tail!", True, (50, 200, 200)), (50,360))
        self._display.blit(self.fontBig.render("Good luck!", True, (250, 250, 0)), (150,480))
        pygame.display.flip()
  
    def renderEndScreen(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self._snakeImg, (self.windowWidth-320, self.windowHeight-380))
        self._display.blit(self.fontBig.render("GAME OVER - You lost!", True, (250, 0, 0)), (50,50))
        self._display.blit(self.fontMid.render("Your Score: " + str(self.score), True, (250, 250, 0)), (50,160))
        self._display.blit(self.fontSmall.render("- To return to the start screen, press [SPACE]", True, (50, 200, 200)), (50,240))
        self._display.blit(self.fontSmall.render("- To exit the game, press [ESC]", True, (50, 200, 200)), (50,280))
        self._display.blit(self.fontBig.render("Thank's for playing!", True, (50, 200, 0)), (150,400))
        pygame.display.flip()
    
    def renderIngameScreen(self):
        self._display.fill((0, 0, 0))
        self._display.blit(self.fontSmall.render("Score: " + str(self.score), True, (0, 200, 0)), (10,10))
        self._display.blit(self._foodImg, (self.food.x, self.food.y))
        self.player.draw(self._display, self._playerImg)
        pygame.display.flip()

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
                self.started = False
                self.lost = True


if __name__ == "__main__":
    app = App()
    app.start()    

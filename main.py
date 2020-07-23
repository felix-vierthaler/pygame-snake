import pygame
from array import *
import math
from random import *


class App:
    WIDTH = 1000
    HEIGHT = 700
    TITLE = "Snake"

    def __init__(self, startScene):
        self.startScene = startScene
        self.running = True
        self.screen = 0

    def changeScene(self, newScene):
        self.activeScene = newScene(self, self.WIDTH, self.HEIGHT)
    def changeSceneObj(self, newScene, obj):
        self.activeScene = newScene(self, self.WIDTH, self.HEIGHT, obj)

    def stop():
        self.running = False

    def start(self):
        clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption(self.TITLE)
        self.changeScene(self.startScene)
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        while self.running:
            #test if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            self.activeScene.handleEvent()
            self.activeScene.update()
            self.activeScene.render(self.screen)


            pygame.display.flip()
            clock.tick(60)

class SceneBase:
    def __init__(self, app, width, height):
        self.app = app
        self.width = width
        self.height = height

    def handleEvent(self):
        print('handleEvent needs to be overwritten!')
    def update(self):
        print('update needs to be overwritten!')
    def render(self, screen):
        print('render needs to be overwritten!')


class GameScene(SceneBase):
    def __init__(self, app, width, height):
        SceneBase.__init__(self, app, width, height)

        self.score = 50

    def handleEvent(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]: 
            self.app.changeScene(MenuScene)
        if pressed[pygame.K_UP]: 
            self.app.changeSceneObj(OverScene, self.score)


    def update(self):
        pass
    def render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100,100,50,50))


class MenuScene(SceneBase):
    def __init__(self, app, width, height):
        SceneBase.__init__(self, app, width, height)


        self.fontL = pygame.font.SysFont("comicsansms", 100)
        self.fontS = pygame.font.SysFont("comicsansms", 50)


    def handleEvent(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]: 
            self.app.changeScene(GameScene)

    def update(self):
        pass
    def render(self, screen):
        screen.fill((255, 255, 255))

        text1 = self.fontL.render("Welcome to SNAKE", True, (0, 128, 0))
        text2 = self.fontS.render("Press ENTER to start", True, (0, 0, 0))

        screen.blit(text1, (self.width/2 - text1.get_width()/2, self.height/2 - 100))
        screen.blit(text2, (self.width/2 - text2.get_width()/2, self.height/2 - 0))


class OverScene(SceneBase):
    def __init__(self, app, width, height, obj):
        SceneBase.__init__(self, app, width, height)
        self.obj = obj

        self.fontL = pygame.font.SysFont("comicsansms", 100)
        self.fontS = pygame.font.SysFont("comicsansms", 50)


    def handleEvent(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]: 
            self.app.changeScene(GameScene)
        if pressed[pygame.K_ESCAPE]: 
            self.app.changeScene(MenuScene)

    def update(self):
        pass
    def render(self, screen):
        screen.fill((255, 255, 255))

        text1 = self.fontL.render("GAME OVER!", True, (0, 128, 0))
        text2 = self.fontS.render("Press ENTER to restart", True, (0, 0, 0))
        text3 = self.fontS.render("SCORE: " + str(self.obj), True, (0, 0, 0))

        screen.blit(text1, (self.width/2 - text1.get_width()/2, self.height/2 - 100))
        screen.blit(text2, (self.width/2 - text2.get_width()/2, self.height/2 - 0))
        screen.blit(text3, (self.width/2 - text3.get_width()/2, self.height/2 - 150))

    


if __name__ == "__main__":
    app = App(MenuScene)
    app.start()

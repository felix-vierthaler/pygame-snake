import pygame

import snake
import apples

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
    BOX_WIDTH = 30

    def __init__(self, app, width, height):
        SceneBase.__init__(self, app, width, height)

        self.snake = snake.Snake(width, height, self.BOX_WIDTH)
        self.apples = apples.Apples(width, height, self.BOX_WIDTH)

        self.apples.addApple()

        self.font = pygame.font.SysFont("comicsansms", 40)

    def handleEvent(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]: 
            self.app.changeScene(MenuScene)

        if pressed[pygame.K_UP]: 
            self.snake.up()
        if pressed[pygame.K_DOWN]: 
            self.snake.down()
        if pressed[pygame.K_RIGHT]: 
            self.snake.right()
        if pressed[pygame.K_LEFT]: 
            self.snake.left()


    def update(self):
        self.snake.update()

        intersections = self.snake.checkIntersectList(self.apples.apples)
        for intersection in intersections:
            self.apples.remove(intersection)
            self.snake.addSchwanz()


        if self.snake.isDead:
            self.app.changeSceneObj(OverScene, self.snake.score)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.apples.render(screen)
        self.snake.render(screen)

        text = self.font.render("Score: " + str(self.snake.score), True, (255, 255, 255))
        screen.blit(text, (6,6))

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
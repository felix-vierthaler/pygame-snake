import pygame
from random import randint

#import own packages
import snake
import apples
import nukes
import eatAnimation

#base class for all scenes
class SceneBase:
    def __init__(self, app, width, height):
        self.app = app
        self.width = width
        self.height = height

    #functions need to be overwritten
    def handleEvent(self):
        print('handleEvent needs to be overwritten!')
    def update(self):
        print('update needs to be overwritten!')
    def render(self, screen):
        print('render needs to be overwritten!')
    def stop(self):
        print('stop needs to be overwritten!')

#first scene responsible for handling the game scene.
class GameScene(SceneBase):
    BOX_WIDTH = 30

    def __init__(self, app, width, height):
        SceneBase.__init__(self, app, width, height)

        #create snake and apple
        self.snake = snake.Snake(width, height, self.BOX_WIDTH)
        self.apples = apples.Apples(width, height, self.BOX_WIDTH)
        self.nukes = nukes.Nukes(width, height, self.BOX_WIDTH)

        #add specific amount of apples at beginning
        for i in range(6):
            self.apples.addApple()

        #add specific amount of nukes at beginning
        for i in range(12):
            self.nukes.addNuke()

        #init particles
        self.animationEat = eatAnimation.EatAnimation(self.BOX_WIDTH)
        self.animationNuke = eatAnimation.EatAnimation(self.BOX_WIDTH)
        self.animationNuke.setColor((248,20,25))
        
        #font needed for score overlay
        self.font = pygame.font.SysFont("comicsansms", 40)

        #load music
        pygame.mixer.music.load("music/music.mp3")
        pygame.mixer.music.play(-1)

        #add sounds
        self.explosionSound = pygame.mixer.Sound("music/explosion.wav")
        
    #get the inputs from pygame and process them
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
        self.animationEat.update()
        self.animationNuke.update()

        #check if apples intersect with snake
        intersections = self.snake.checkIntersectList(self.apples.apples)
        for intersection in intersections:
            self.snake.addSchwanz()  #add schwanz to snake
            self.apples.remove(intersection)  #remove intersecting apples
            self.animationEat.start(self.snake.x, self.snake.y, randint(5,30))

        #check if nukes intersect with snake
        intersections = self.snake.checkIntersectList(self.nukes.nukes)
        for intersection in intersections:
            self.nukes.remove(intersection)  #remove intersecting apples
            if not self.snake.dying:
                pygame.mixer.Sound.play(self.explosionSound)
                self.animationNuke.start(self.snake.x, self.snake.y, randint(5,30))
            self.snake.die()

        #if snake died, go to OverScene
        if self.snake.isDead:
            self.app.changeSceneObj(OverScene, self.snake.score)

    def render(self, screen):
        #fill bg in black
        screen.fill((60, 50, 7))
        #render apples and snake and nukes
        self.apples.render(screen)
        self.nukes.render(screen)
        self.animationEat.render(screen)
        self.animationNuke.render(screen)
        self.snake.render(screen)

        #render score overlay
        text = self.font.render("Score: " + str(self.snake.score), True, (255, 255, 255))
        screen.blit(text, (6,6))

    def stop(self):
        pygame.mixer.music.fadeout(2000)

class MenuScene(SceneBase):
    def __init__(self, app, width, height):
        SceneBase.__init__(self, app, width, height)

        #create fonts
        self.fontL = pygame.font.SysFont("comicsansms", 70)
        self.fontS = pygame.font.SysFont("comicsansms", 35)

    def handleEvent(self):
        #if enter is pressed, go to GameScene
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]: 
            self.app.changeScene(GameScene)

    def update(self):
        pass

    def render(self, screen):
        #fill bg in white
        screen.fill((255, 255, 255))

        #create text
        text1 = self.fontL.render("Welcome to SNAKE", True, (0, 128, 0))
        text2 = self.fontS.render("Press ENTER to start", True, (0, 0, 0))

        #add text to screen
        screen.blit(text1, (self.width/2 - text1.get_width()/2, self.height/2 - 100))
        screen.blit(text2, (self.width/2 - text2.get_width()/2, self.height/2 - 0))

    def stop(self):
        pass

class OverScene(SceneBase):
    def __init__(self, app, width, height, obj):
        SceneBase.__init__(self, app, width, height)
        self.obj = obj

        #create fonts
        self.fontL = pygame.font.SysFont("comicsansms", 100)
        self.fontS = pygame.font.SysFont("comicsansms", 50)

    def handleEvent(self):
        #if enter key is pressed go to game scene, if esc is pressed go to menu scene
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]: 
            self.app.changeScene(GameScene)
        if pressed[pygame.K_ESCAPE]: 
            self.app.changeScene(MenuScene)

    def update(self):
        pass
    def render(self, screen):
        #fill bg in white
        screen.fill((255, 255, 255))

        #create text
        text1 = self.fontL.render("GAME OVER!", True, (0, 128, 0))
        text2 = self.fontS.render("Press ENTER to restart", True, (0, 0, 0))
        text3 = self.fontS.render("SCORE: " + str(self.obj), True, (0, 0, 0))

        #add text to screen
        screen.blit(text1, (self.width/2 - text1.get_width()/2, self.height/2 - 100))
        screen.blit(text2, (self.width/2 - text2.get_width()/2, self.height/2 - 0))
        screen.blit(text3, (self.width/2 - text3.get_width()/2, self.height/2 - 150))

    def stop(self):
        pass
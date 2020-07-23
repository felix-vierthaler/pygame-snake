import pygame
from array import *
import math
from random import *


class Snake:
    addSchwanzTrue = False

    def __init__(self, startX, startY, boxWidth):
        self.startX = startX
        self.startY = startY
        self.x = startX
        self.y = startY
        self.boxWidth = boxWidth

        self.tailX = []
        self.tailY = []
        self.direction = 2 #down
        self.nextDirection = 0
        self.speed = 1

    def update(self):
        #if snake is directly on field
        if self.x % self.boxWidth == 0 and self.y % self.boxWidth ==0:
            #add postition to the tail
            self.tailX.append(self.x)
            self.tailY.append(self.y)

            if not self.addSchwanzTrue:
                del self.tailX[0]
                del self.tailY[0]
            else:
                self.addSchwanzTrue = False

            #change direction if possible
            if abs(self.nextDirection-self.direction) != 2:
                self.direction = self.nextDirection

        #move snake according to speed and direction
        if(self.direction == 0): self.y += self.speed
        elif(self.direction == 1): self.x -= self.speed
        elif(self.direction == 2): self.y -= self.speed
        elif(self.direction == 3): self.x += self.speed

        #check if snake ran into itself
        self.checkIntersect()

    def render(self, screen):
        for x in range(len(self.tailX)):
            pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(self.tailX[x], self.tailY[x], self.boxWidth, self.boxWidth))

        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    def die(self):
        self.tailX = []
        self.tailY = []
        self.x = self.startX
        self.y = self.startY
        self.direction = 2
        self.nextDirection = 0

    def addSchwanz(self):
        self.addSchwanzTrue = True

    def checkIntersect(self):
        for i in range(len(self.tailX)-1):
            x=abs(self.x - self.tailX[i])
            y=abs(self.y - self.tailY[i])

            if(x==0 or y==0):
                if x+y < self.boxWidth:
                    self.die()
                    break

    def checkIntersectList(self, list):
        intersections = []
        for item in list:
            x=abs(self.x - item.x)
            y=abs(self.y - item.y)

            if(x==0 or y==0):
                if x+y == 0:
                    intersections.append(item)
        
        return intersections


    def up(self):
        self.nextDirection = 2
    def down(self):
        self.nextDirection = 0
    def left(self):
        self.nextDirection = 1
    def right(self):
        self.nextDirection = 3

class Apples:
    apples = []
    def __init__(self, width, height, boxWidth):
        self.width = width
        self.height = height
        self.boxWidth = boxWidth

    class Apple:
        def __init__(self, x, y, boxWidth):
            self.x = x
            self.y = y
            self.boxWidth = boxWidth

        def render(self, screen):
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    def addApple(self):
        widthM = self.width / self.boxWidth
        heightM = self.height / self.boxWidth
        apple = self.Apple(randint(0, widthM) * self.boxWidth, randint(0, heightM) * self.boxWidth, self.boxWidth)
        self.apples.append(apple)

    def remove(self, apple):
        self.apples.remove(apple)

    def render(self, screen):
        for apple in self.apples:
            apple.render(screen)




class App:
    BOX_WIDTH = 30
    WIDTH = BOX_WIDTH * 30
    HEIGHT = BOX_WIDTH *30

    def __init__(self):
        self.screen = 0

        self.snake = Snake(self.WIDTH//2, self.HEIGHT//2, self.BOX_WIDTH)
        self.apples = Apples(self.WIDTH, self.HEIGHT, self.BOX_WIDTH)

        for i in range(40):
            self.apples.addApple()

    def start(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        appRunning = True
        while appRunning:
            appRunning = self.menuLoop()
            if not appRunning:
                break
            appRunning = self.gameLoop()
            if not appRunning:
                break
        

    def gameLoop(self):
        returnValue = True
        clock = pygame.time.Clock()
        done = False
        while not done:
            #test if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    returnValue = False

            self.getInput()
            status = self.update()
            self.screen.fill((0, 0, 0))
            self.render()

            if not status:
                done = True

            pygame.display.flip()

            clock.tick(200)

        return returnValue

    def menuLoop(self):
        returnValue = True
        clock = pygame.time.Clock()
        menu = True
        while menu:
            #test if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    returnValue = False
                if event.type == pygame.KEYDOWN:
                    menu = False

            self.screen.fill((255, 255, 255))

            pygame.display.flip()
            clock.tick(60)

        return returnValue

    def restart():
        pass


    def getInput(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            self.snake.up()
        if pressed[pygame.K_DOWN]: 
            self.snake.down()
        if pressed[pygame.K_LEFT]: 
            self.snake.left()
        if pressed[pygame.K_RIGHT]:
            self.snake.right()

    def update(self):
        status = True

        #update snake
        self.snake.update()

        #if snake goes outside screen let her die
        if(self.snake.x > self.WIDTH-self.BOX_WIDTH or self.snake.x < 0 or self.snake.y > self.HEIGHT-self.BOX_WIDTH or self.snake.y < 0):
            self.snake.die()
            status = False

        #check if snake eats apple / intersects with it and remove those
        intersections = self.snake.checkIntersectList(self.apples.apples)
        for intersection in intersections:
            self.snake.addSchwanz()
            self.apples.remove(intersection)

        return status

    def render(self):
        self.apples.render(self.screen)
        self.snake.render(self.screen)


if __name__ == "__main__":
    app = App()
    app.start()

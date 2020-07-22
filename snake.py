import pygame
from array import *
import math


class Snake:
    def __init__(self, startX, startY, boxWidth):
        self.x = startX
        self.y = startY
        self.boxWidth = boxWidth

        self.tailX = []
        self.tailY = []
        self.direction = 2 #down
        self.nextDirection = 0
        self.speed = 1

    def update(self):
        if self.x % self.boxWidth == 0 and self.y % self.boxWidth ==0:
            self.tailX.append(self.x)
            self.tailY.append(self.y)

            if len(self.tailX) >= 30:
                del self.tailX[0]
                del self.tailY[0]

            if abs(self.nextDirection-self.direction) != 2:
                self.direction = self.nextDirection

        if(self.direction == 0): self.y += self.speed
        elif(self.direction == 1): self.x -= self.speed
        elif(self.direction == 2): self.y -= self.speed
        elif(self.direction == 3): self.x += self.speed

        self.checkIntersect()

    def render(self, screen):
        for x in range(len(self.tailX)):
            pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(self.tailX[x], self.tailY[x], self.boxWidth, self.boxWidth))

        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    def die(self, x, y):
        self.tailX = []
        self.tailY = []
        self.x = x
        self.y = y
        self.direction = 2
        self.nextDirection = 0

    def checkIntersect(self):
        for i in range(len(self.tailX)-1):
            x=abs(self.x - self.tailX[i])
            y=abs(self.y - self.tailY[i])

            print(self.x, ' -- ', self.tailX[i])

            print(x, ' ', y)

            if(x==0 or y==0):
                if x+y < self.boxWidth:
                    self.die(200,200)
                    break



            


    def up(self):
        self.nextDirection = 2
    def down(self):
        self.nextDirection = 0
    def left(self):
        self.nextDirection = 1
    def right(self):
        self.nextDirection = 3


class Map:
    def __init__(self):
        pass




class App:
    BOX_WIDTH = 50
    WIDTH = BOX_WIDTH * 20
    HEIGHT = BOX_WIDTH *20

    def __init__(self):
        self.screen = 0

        self.snake = Snake(self.WIDTH/2, self.HEIGHT/2, self.BOX_WIDTH)

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        done = False
        while not done:
            #test if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.getInput()
            self.update()
            self.screen.fill((0, 0, 0))
            self.render()

            pygame.display.flip()

            clock.tick(300)

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
        self.snake.update()

        if(self.snake.x > self.WIDTH-self.BOX_WIDTH or self.snake.x < 0 or self.snake.y > self.HEIGHT-self.BOX_WIDTH or self.snake.y < 0):
            self.snake.die(self.WIDTH/2, self.HEIGHT/2)

    def render(self):
        self.snake.render(self.screen)



if __name__ == "__main__":
    app = App()
    app.start()

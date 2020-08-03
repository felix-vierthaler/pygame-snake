from random import randint
import pygame
import math

#class for snake object in game
class Snake:
    DIE_FRAMES = 200
    DYING_SPEED_MULTIPLYER = 0.98
    addSchwanzTrue = False  #wether or not to add a schwanz piece

    def __init__(self, width, height, boxWidth):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.boxWidth = boxWidth

        self.tailX = []  #stores x and y coordinates of schwanz pieces
        self.tailY = []  #
        self.direction = 0  #0=down 1=left 2=up 3=right
        self.nextDirection = 0  #direction it will go once it is in middle of field
        self.speed = 2 #danger: has to be dividable by boxWidth

        self.isDead = False
        self.dying = False
        self.framesSinceDead = 0
        self.score = 0

        #add assets
        self.snakeBodyImg = pygame.image.load('assets/snake-body.png')
        self.snakeBodyImg = pygame.transform.scale(self.snakeBodyImg, (boxWidth, boxWidth))
        self.imgCounter = 0

        self.snakeHeadImg = pygame.image.load('assets/snake-head.png')
        self.snakeHeadImg = pygame.transform.scale(self.snakeHeadImg, (boxWidth, boxWidth))

        #add sounds
        self.biteSound = pygame.mixer.Sound("music/bite2.wav")

    def update(self):
        #if snake is directly on field
        if self.x % self.boxWidth == 0 and self.y % self.boxWidth ==0:
            #add postition to the tail
            self.tailX.append(self.x)
            self.tailY.append(self.y)

            #delete last tail element if no schwanz is to be added and still moving
            if not self.addSchwanzTrue and self.speed != 0:
                del self.tailX[0]
                del self.tailY[0]
            self.addSchwanzTrue = False

            #if snake didnt die yet
            if not self.dying:
                #change direction if possible
                if abs(self.nextDirection-self.direction) != 2:
                    self.direction = self.nextDirection
            #if it died, slow down speed until 0
            elif self.speed > 0:
                self.speed -= 1

        #move snake according to speed and direction
        if(self.direction == 0): self.y += self.speed
        elif(self.direction == 1): self.x -= self.speed
        elif(self.direction == 2): self.y -= self.speed
        elif(self.direction == 3): self.x += self.speed

        #check if out of bounds
        if self.x < 0 or self.x > self.width - self.boxWidth:
            self.die()
        if self.y < 0 or self.y > self.height - self.boxWidth:
            self.die()
        
        #check if snake ran into itself
        self.checkIntersect()

        #if dying add died frames
        if self.dying:
            self.framesSinceDead += 1
            if self.framesSinceDead >= self.DIE_FRAMES:
                self.isDead = True

    def render(self, screen):
        #draw all tail elements on screen

        #turn snake body every few frames to animate
        self.imgCounter += 1
        if self.imgCounter >= 4 and self.speed != 0:
            self.imgCounter = 0
            self.snakeBodyImg = pygame.transform.rotate(self.snakeBodyImg, 90)

        #draw all snake bodys on the screen
        for x in range(len(self.tailX)):
            screen.blit(self.snakeBodyImg, pygame.Rect(self.tailX[x], self.tailY[x], self.boxWidth, self.boxWidth))
            #pygame.draw.rect(screen, (0, 100, 255), pygame.Rect(self.tailX[x], self.tailY[x], self.boxWidth, self.boxWidth))

        #draw main snake element on screen
        turnAmount = 90 + self.direction * 90
        img = pygame.transform.rotate(self.snakeHeadImg, 360 - turnAmount)
        
        
        #pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    #initiates dying process and fades music out
    def die(self):
        self.dying = True
        pygame.mixer.music.fadeout(2000)

    #adds one schwanz element and plays eat sound
    def addSchwanz(self):
        self.score += 1
        self.addSchwanzTrue = True

        #play sound
        pygame.mixer.Sound.play(self.biteSound)

    #checks for intersection with itself, die if this is the case
    def checkIntersect(self):
        for i in range(len(self.tailX)-1):
            x=abs(self.x - self.tailX[i])
            y=abs(self.y - self.tailY[i])

            if(x==0 or y==0):
                if x+y < self.boxWidth:
                    self.die()
                    break
    
    #checks intersection with all elements on list, returns list
    def checkIntersectList(self, list):
        intersections = []
        for item in list:
            x=abs(self.x - item.x)
            y=abs(self.y - item.y)

            if(x==0 or y==0):
                if x+y < self.boxWidth:
                    intersections.append(item)
        
        return intersections

    #functions to set direction of next movement from outside of class
    def up(self):
        self.nextDirection = 2
    def down(self):
        self.nextDirection = 0
    def left(self):
        self.nextDirection = 1
    def right(self):
        self.nextDirection = 3
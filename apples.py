import pygame
from random import randint
import math

#class that organizes all the apples
class Apples:
    def __init__(self, width, height, boxWidth):
        self.apples = []
        self.width = width
        self.height = height
        self.boxWidth = boxWidth

    #class to store one apple
    class Apple:
        def __init__(self, x, y, boxWidth):
            self.x = x
            self.y = y
            self.boxWidth = boxWidth

            #assets
            self.appleImg = pygame.image.load('assets/gold.png')
            self.appleImg = pygame.transform.scale(self.appleImg, (boxWidth, boxWidth))

        def render(self, screen):
            screen.blit(self.appleImg, pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))
            #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    #add apple at random position
    def addApple(self):
        widthM = self.width / self.boxWidth
        heightM = self.height / self.boxWidth
        apple = self.Apple(randint(0, widthM-1) * self.boxWidth, randint(0, heightM-1) * self.boxWidth, self.boxWidth)
        self.apples.append(apple)

    #remove specified apple
    def remove(self, apple):
        self.apples.remove(apple)
        self.addApple()

    #render all apples in list
    def render(self, screen):
        for apple in self.apples:
            apple.render(screen)
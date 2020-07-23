import pygame
from random import randint
import math

#class that organizes all the apples
class Nukes:
    def __init__(self, width, height, boxWidth):
        self.nukes = []
        self.width = width
        self.height = height
        self.boxWidth = boxWidth

    #class to store one apple
    class Nuke:
        def __init__(self, x, y, boxWidth):
            self.x = x
            self.y = y
            self.boxWidth = boxWidth

            #import assets
            #assets
            self.nukeImg = pygame.image.load('assets/enemie.png')
            self.nukeImg = pygame.transform.scale(self.nukeImg, (boxWidth, boxWidth))

        def render(self, screen):
            screen.blit(self.nukeImg, pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))
            #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.boxWidth, self.boxWidth))

    #add apple at random position
    def addNuke(self):
        widthM = self.width / self.boxWidth
        heightM = self.height / self.boxWidth
        nuke = self.Nuke(randint(0, widthM-1) * self.boxWidth, randint(0, heightM-1) * self.boxWidth, self.boxWidth)
        self.nukes.append(nuke)

    #remove specified apple
    def remove(self, nuke):
        self.nukes.remove(nuke)
        self.addNuke()

    #render all apples in list
    def render(self, screen):
        for nuke in self.nukes:
            nuke.render(screen)
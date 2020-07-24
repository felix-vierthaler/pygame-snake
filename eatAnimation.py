import pygame
from random import randint,uniform

#class for organizing particle animations
class EatAnimation:
    def __init__(self, boxWidth):
        self.boxWidth = boxWidth
        self.particles = []
        self.size = 6
        self.color = 0

    def setColor(self, color):
        self.color = color

    #class for storing one particle
    class Particle:
        MAX_SPEED = 10
        GRAVITY = 0.9
        START_SIZE = 6

        def __init__(self, animation, x, y, color):
            self.x = x
            self.y = y
            self.xS = randint(-self.MAX_SPEED, self.MAX_SPEED)
            self.yS = randint(-self.MAX_SPEED, self.MAX_SPEED)
            self.size = self.START_SIZE
            self.animation = animation
            self.sizeChange = uniform(0.01, 0.1)
            self.color = color

        #returns set color, if no color set, use the default
        def getColor(self):
            if not self.color:
                return (randint(248,255), randint(220,230), 11)
            else: 
                return self.color 

        #updates position and size of particle
        def update(self):
            self.xS = self.xS * self.GRAVITY
            self.yS = self.yS * self.GRAVITY

            self.x += self.xS
            self.y += self.yS

            self.size -= self.sizeChange
            if self.size <= 1:
                self.animation.remove(self)

        #renders itself on the screen
        def render(self, screen):
            pygame.draw.rect(screen, self.getColor(), pygame.Rect(self.x, self.y, self.size, self.size))
    
    #updates all particles in array
    def update(self):
        for particle in self.particles:
            particle.update()

    #render all particles on screen
    def render(self, screen):
        for particle in self.particles:
            particle.render(screen)

    #initiates the animation process
    def start(self, x, y, amount):
        for i in range(amount):
            self.particles.append(self.Particle(self, x, y, self.color))

    #removes one item from array
    def remove(self, item):
        self.particles.remove(item)
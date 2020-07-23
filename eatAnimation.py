import pygame
from random import randint,uniform

class eatAnimation:
    def __init__(self, boxWidth):
        self.boxWidth = boxWidth
        self.particles = []
        self.size = 6


    class Particle:
        MAX_SPEED = 10
        GRAVITY = 0.9
        START_SIZE = 6

        def __init__(self, animation, x, y):
            self.x = x
            self.y = y
            self.xS = randint(-self.MAX_SPEED, self.MAX_SPEED)
            self.yS = randint(-self.MAX_SPEED, self.MAX_SPEED)
            self.size = self.START_SIZE
            self.animation = animation
            self.sizeChange = uniform(0.01, 0.1) 

        def update(self):
            self.xS = self.xS * self.GRAVITY
            self.yS = self.yS * self.GRAVITY

            self.x += self.xS
            self.y += self.yS

            self.size -= self.sizeChange
            if self.size <= 1:
                self.animation.remove(self)

        def render(self, screen):
            pygame.draw.rect(screen, (randint(248,255), randint(220,230), 11), pygame.Rect(self.x, self.y, self.size, self.size))
    
    def update(self):
        for particle in self.particles:
            particle.update()


    def render(self, screen):
        for particle in self.particles:
            particle.render(screen)


    def start(self, x, y, amount):
        for i in range(amount):
            self.particles.append(self.Particle(self, x, y))
    def remove(self, item):
        self.particles.remove(item)
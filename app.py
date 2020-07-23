import pygame

class App:
    WIDTH = 900
    HEIGHT = 600
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
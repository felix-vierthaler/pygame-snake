import pygame

#Class to handle the game loop and the scenes
class App:
    WIDTH = 900
    HEIGHT = 600
    TITLE = "Snake"

    def __init__(self, startScene):
        self.startScene = startScene
        self.activeScene = 0
        self.running = True
        self.screen = 0

    #creates new object of given class and sets activeScene to it
    def changeScene(self, newScene):
        if self.activeScene:
            self.activeScene.stop()
        self.activeScene = newScene(self, self.WIDTH, self.HEIGHT)
    #same as above, but an object can be passed to the new Scene
    def changeSceneObj(self, newScene, obj):
        if self.activeScene:
            self.activeScene.stop()
        self.activeScene = newScene(self, self.WIDTH, self.HEIGHT, obj)

    #function to stop gameloop from outside
    def stop(self):
        self.running = False

    #starts the gameloop
    def start(self):
        #pygame setup
        clock = pygame.time.Clock()
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.display.set_caption(self.TITLE)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        #set starting scene
        self.changeScene(self.startScene)

        while self.running:
            #test if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            #handle events, update and render active Scene
            self.activeScene.handleEvent()
            self.activeScene.update()
            self.activeScene.render(self.screen)

            #flip pygame buffer to actually render to screen
            pygame.display.flip()
            #set framerate of 60fps
            clock.tick_busy_loop(120)
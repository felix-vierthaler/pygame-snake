#own imports
import scenes
import app

#main function
if __name__ == "__main__":
    #create app object with Menu as starting scene
    app = app.App(scenes.MenuScene)
    #start the app
    app.start()

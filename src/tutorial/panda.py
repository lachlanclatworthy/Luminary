# panda.py

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Game(ShowBase):
    def __init__(self, window):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(window.width, window.height)
        self.win.requestProperties(properties)

def run():
    game = Game(Window(1600, 900))
    game.run()

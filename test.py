from mdln import *

class TestGame(Game):
    def __init__(self, **kwargs):
        ON_EVENT(pg.QUIT, self.event_quit)

        super().__init__(**kwargs)

    def event_quit(self, e):
        exit()

game = TestGame()

scene = Scene()
game.set_scene(scene)

game.start()

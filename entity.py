import pygame as pg

from mdln.const import *
from mdln.icon import Icon

class Entity():
    position: pg.math.Vector2 = None
    layer = LAYER_DEFAULT
    scene = None
    icon: Icon = None

    def __init__(self):
        self.position = pg.math.Vector2(0, 0)

    def tick(self):
        pass

    def draw(self):
        if self.icon is not None:
            self.scene.game.screen.blit(self.icon.get_surface(self.scene.game.frame), self.position)

    def event(self, event):
        pass

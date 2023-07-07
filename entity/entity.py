import pygame as pg

from mdln.const import *
from mdln.icon import Icon

class Entity():
    position: pg.math.Vector2 = None
    layer = LAYER_DEFAULT
    scene = None
    icon: Icon = None
    visible: bool = False

    def __init__(self):
        self.position = pg.math.Vector2(0, 0)

    def tick(self):
        pass

    def draw(self) -> pg.Surface:
        if self.icon is not None:
            return self.icon.get_surface(self.scene.game.frame)
        
        return None

    def event(self, event):
        pass

import pygame as pg

from mdln.const import *
from mdln.icon import Icon

class Entity():
    rect: pg.Rect = None
    layer = LAYER_DEFAULT
    stage = None
    icon: Icon = None
    visible: bool = False

    def __init__(self, rect=None):
        if rect:
            self.rect = rect
        else:
            self.rect = pg.Rect(0, 0, RECT_SIZE_DEFAULT[0], RECT_SIZE_DEFAULT[1])

    def tick(self):
        pass

    def draw(self) -> pg.Surface:
        if self.icon is not None:
            return self.icon.get_surface(self.stage.scene.game.frame)
        
        return None

    def event(self, event):
        pass

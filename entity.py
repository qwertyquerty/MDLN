from pygame.math import Vector2

from mdln.const import *
from mdln.icon import Icon

def Entity():
    position: Vector2 = None
    layer = LAYER_DEFAULT
    scene = None
    icon: Icon = None

    def __init__(self):
        pass

    def tick(self):
        pass

    def draw(self):
        pass

    def event(self, event):
        pass

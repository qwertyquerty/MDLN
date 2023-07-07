import pygame as pg

from mdln.entity import Entity

class Sprite(Entity):
    visible = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

import pygame as pg

class Component():
    entity = None

    def __init__(self, entity=None):
        self.entity = entity

    def init(self):
        pass

    def tick(self):
        pass

    def draw(self, screen: pg.Surface):
        pass

    def attach(self, entity):
        self.entity = entity

from mdln.const import *
from mdln.entity import Entity

class Scene():
    entities: list[Entity] = None
    game = None

    def __init__(self):
        self.entities = []

    def _tick(self):
        self.tick()

        for entity in self.entities:
            entity.tick()

    def _draw(self):
        self.draw()

        for entity in sorted(self.entities, key=lambda e: e.layer):
            entity.draw()

    def _event(self, event):
        self.event(event)

        for entity in self.entities:
            entity.event(event)

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.scene = self

    def tick(self):
        pass
    
    def draw(self):
        pass

    def event(self, event):
        pass

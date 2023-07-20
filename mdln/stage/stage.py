from mdln.const import *
from mdln.entity import Entity

class Stage():
    entities: list[Entity] = None
    scene = None
    layer: int = LAYER_DEFAULT

    def __init__(self):
        self.entities = []

    def _tick(self):
        self.tick()
        # somehow faster than a for loop
        list(map(lambda e: e.tick(), (e for e in self.entities if e.ticks)))
                
    def _draw(self, screen):
        self.draw(screen)

        for entity in sorted(self.entities, key=lambda e: e.layer):
            if entity.visible:
                surf = entity.draw()

                if surf is not None:
                    screen.blit(surf, entity.rect.topleft)

    def _event(self, event):
        self.event(event)

        for entity in self.entities:
            entity.event(event)

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.stage = self

    def tick(self):
        pass

    def draw(self, screen):
        pass

    def event(self, event):
        pass

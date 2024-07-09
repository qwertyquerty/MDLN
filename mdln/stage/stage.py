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
        
        for entity in self.entities:
            if entity.ticks:
                entity.tick()
                
    def _draw(self, screen):
        self.draw(screen)
        self.draw_entities(screen)
        self.post_draw(screen)

    def draw_entities(self, screen):
        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            if entity.visible:
                surf = entity.draw()

                if surf is not None:
                    screen.blit(surf, entity.rect.topleft)

    def _init(self):
        self.init()

        for entity in self.entities:
            entity.init()

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.stage = self

        if self.scene and self.scene.game and self.scene.game.running:
            entity.init()

    def tick(self):
        pass

    def draw(self, screen):
        pass
    
    def post_draw(self, screen):
        pass

    def init(self):
        pass

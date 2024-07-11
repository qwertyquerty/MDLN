from mdln.const import *
from mdln.entity import Entity
from mdln.system import System

import bisect

class Stage():
    initialized: bool = False

    entities: list[Entity] = None
    
    systems: list[System] = None

    scene = None
    
    layer: int = LAYER_DEFAULT

    ticks: int = 0

    _deletion_queue: list = None

    def __init__(self):
        self.entities = []
        self.systems = []

        self._deletion_queue = []

    def _tick(self):
        self.tick()
        
        for entity in self.entities:
            if entity.active:
                entity.tick()
        
        self.systems.sort(key=lambda s: s.priority)

        for system in self.systems:
            if system.active and (self.ticks % system.wait) == 0:
                system.tick()
                system.ticks += 1
    
        for entity in self._deletion_queue:
            self.entities.remove(entity)
        
        self._deletion_queue = []

        self.ticks += 1
                
    def _draw(self, screen):
        self.draw(screen)
        self.draw_entities(screen)
        self.post_draw(screen)

    def draw_entities(self, screen):
        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            if entity.visible:
                surf = entity.draw(screen)

                if surf is not None:
                    screen.blit(surf, entity.rect.topleft())

    def _init(self):
        if not self.initialized:
            self.initialized = True
            
            self.init()

            for entity in self.entities:
                if not entity.initialized:
                    entity.init()
                    entity.initialized = True
            
            for system in self.systems:
                if not system.initialized:
                    system.init()
                    system.initialized = True

    def add_entity(self, entity):
        self.entities.append(entity)
        entity.stage = self

        if self.scene and self.scene.game and self.scene.game.running and not entity.initialized:
            entity.init()

    def add_system(self, system):
        bisect.insort(self.systems, system, key=lambda s: s.priority)
        system.stage = self

        if self.scene and self.scene.game and self.scene.game.running and not system.initialized:
            system.init()

    def tick(self):
        pass

    def draw(self, screen):
        pass
    
    def post_draw(self, screen):
        pass

    def init(self):
        pass

    def get_entities_with_component(self, component_type):
        return (entity for entity in self.entities if entity.has_component(component_type))

    def get_entities_with_components(self, component_types: tuple):
        return (entity for entity in self.entities if entity.matches_components(component_types))

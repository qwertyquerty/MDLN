from __future__ import annotations
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
    from mdln.scene import Scene

from mdln.const import *
from mdln.entity import Entity
from mdln.system import System

import bisect

class Stage():
    # private

    _deletion_queue: list = None

    # public

    initialized: bool = False

    entities: list[Entity] = None
    
    systems: list[System] = None

    scene: Scene = None
    
    layer: int = LAYER_DEFAULT

    ticks: int = 0

    def __init__(self):
        self.entities = []
        self.systems = []

        self._deletion_queue = []

    def _init(self) -> None:
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

    def _tick(self) -> None:
        self.tick()
        
        for entity in self.entities:
            if entity.active:
                entity._tick()
        
        self.systems.sort(key=lambda s: s.priority)

        for system in self.systems:
            if system.active and (self.ticks % system.wait) == 0:
                system.tick()
                system.ticks += 1
    
        for entity in self._deletion_queue:
            self.entities.remove(entity)
        
        self._deletion_queue = []

        self.ticks += 1
                
    def _draw(self, screen: pg.Surface) -> None:
        self.draw(screen)
        self.draw_entities(screen)
        self.post_draw(screen)

    def init(self) -> None:
        pass

    def tick(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass
    
    def post_draw(self, screen: pg.Surface) -> None:
        pass

    def draw_entities(self, screen: pg.Surface) -> None:
        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            if entity.visible:
                surf = entity.draw(screen)

                if surf is not None:
                    screen.blit(surf, entity.rect.topleft())

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
        entity.stage = self

        if self.scene and self.scene.game and self.scene.game.running and not entity.initialized:
            entity.init()

    def add_system(self, system: System) -> None:
        bisect.insort(self.systems, system, key=lambda s: s.priority)
        system._attach(self)

        if self.scene and self.scene.game and self.scene.game.running and not system.initialized:
            system.init()

    def get_entities_with_component(self, component_type: type) -> Iterator[Entity]:
        return (entity for entity in self.entities if entity.has_component(component_type))

    def get_entities_with_components(self, component_types: Tuple[type]) -> Iterator[Entity]:
        return (entity for entity in self.entities if entity.matches_components(component_types))

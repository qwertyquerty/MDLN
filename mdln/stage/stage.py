from __future__ import annotations
from typing import TYPE_CHECKING, Iterator, Tuple

if TYPE_CHECKING:
    from mdln.scene import Scene

from mdln.const import *
from mdln.entity import Entity
from mdln.system import System
from mdln.util import Context

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

    def _init(self, ctx: Context) -> None:        
        if not self.initialized:
            self.initialized = True
            
            ctx.stage = self

            self.init(ctx)

            for entity in self.entities:
                if not entity.initialized:
                    entity._init(ctx)
                    entity.initialized = True
            
            for system in self.systems:
                if not system.initialized:
                    system._init(ctx)
                    system.initialized = True

    def _tick(self, ctx: Context) -> None:
        ctx.stage = self
        self.tick(ctx)
        
        for entity in self.entities:
            if entity.active:
                entity._tick(ctx)
        
        self.systems.sort(key=lambda s: s.priority)

        for system in self.systems:
            if system.active and (self.ticks % system.wait) == 0:
                system._tick(ctx)
    
        for entity in self._deletion_queue:
            self.entities.remove(entity)
        
        self._deletion_queue = []

        self.ticks += 1
                
    def _draw(self, ctx: Context) -> None:
        ctx.stage = self
        self.draw(ctx)
        self.draw_entities(ctx)

        for system in self.systems:
            if system.active:
                system.draw(ctx)

        self.post_draw(ctx)

    def init(self, ctx: Context) -> None:
        pass

    def tick(self, ctx: Context) -> None:
        pass

    def draw(self, ctx: Context) -> None:
        pass

    def draw_entities(self, ctx: Context) -> None:
        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            if entity.visible:
                surf = entity.draw(ctx)

                if surf is not None:
                    ctx.surface.blit(surf, entity.rect.topleft())

    def post_draw(self, ctx: Context) -> None:
        pass

    def add_entity(self, entity: Entity) -> None:
        self.entities.append(entity)
        entity.stage = self

        if self.scene and self.scene.game and self.scene.game.running and not entity.initialized:
            entity.init(Context.from_stage(self))
            entity.initialized = True

    def add_system(self, system: System) -> None:
        bisect.insort(self.systems, system, key=lambda s: s.priority)
        system._attach(self)

        if self.scene and self.scene.game and self.scene.game.running and not system.initialized:
            system.init(Context.from_stage(self))
            system.initialized = True
            
    def get_entities_with_component(self, component_type: type) -> Iterator[Entity]:
        return (entity for entity in self.entities if entity.has_component(component_type))

    def get_entities_with_components(self, component_types: Tuple[type]) -> Iterator[Entity]:
        return (entity for entity in self.entities if entity.matches_components(component_types))

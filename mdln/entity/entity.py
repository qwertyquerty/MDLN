from __future__ import annotations
from typing import TYPE_CHECKING, Self, Tuple, Dict

if TYPE_CHECKING:
    from mdln.stage import Stage
    from mdln.component import Component

from mdln.const import *
from mdln.geometry import Rect, Vec2
from mdln.icon import Icon
from mdln.registry import ENTITY_REGISTRY
from mdln.util import Context

import inspect
import pygame as pg


class Entity():
    # private

    _component_registry: Dict[type, Component] = None

    # public

    initialized: bool = False

    rect: Rect = None
    
    layer: int = LAYER_DEFAULT
    
    stage: Stage = None
    
    icon: Icon = None
    
    visible: bool = False
    
    active: bool = True
    
    deleted: bool = False

    def __init__(self, rect: Rect = None):
        self._component_registry = {}

        self.rect = rect or Rect(
            Vec2(0, 0),
            Vec2(RECT_SIZE_DEFAULT[0], RECT_SIZE_DEFAULT[1])
        )
    
    def __init_subclass__(cls) -> None:
        """
        Register all known subtypes in the entity registry under their entity path
        """

        tree = list(inspect.getmro(cls))
        tree.remove(Entity)
        tree.remove(object)
        path = '.'.join([o.__name__ for o in tree[::-1]])        
        ENTITY_REGISTRY[path.lower()] = cls

    def _init(self, ctx: Context) -> None:
        ctx.entity = self
        self.init(ctx)

    def _tick(self, ctx: Context) -> None:
        ctx.entity = self
        self.tick(ctx)

        for component in self._component_registry.values():
            component.tick(ctx)

    def init(self, ctx: Context) -> None:
        pass

    def tick(self, ctx: Context) -> None:
        pass

    def draw(self, ctx: Context) -> pg.Surface:
        ctx.entity = self

        for component in self._component_registry.values():
            component.draw(ctx)

        if self.icon is not None:
            return self.icon.get_surface(ctx.game.tick)

        return None

    def add_component(self, component: Component) -> Self:
        existing = self.get_component(type(component))

        if existing is not None:
            raise Exception(f"entity already contains existing component of type {type(component)}")

        self._component_registry[type(component)] = component
        component._attach(self)
        component.init(Context.from_entity(self))

        return self

    def get_component(self, component_type: type) -> Component:
        return self._component_registry.get(component_type)

    def del_component(self, component_type: type) -> bool:
        if self.get_component(component_type) is not None:
            del self._component_registry[component_type]
            return True
        
        return False
    
    def has_component(self, component_type: type) -> bool:
        return component_type in self._component_registry
    
    def matches_components(self, component_types: Tuple[type]) -> bool:
        for ct in component_types:
            if ct not in self._component_registry:
                return False
        
        return True

    def qdel(self) -> None:
        if not self.deleted:
            self.deleted = True
            self.stage._deletion_queue.append(self)

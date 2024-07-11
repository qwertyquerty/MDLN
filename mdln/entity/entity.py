import pygame as pg
import inspect

from mdln.const import *
from mdln.geometry import Rect, Vec2
from mdln.icon import Icon
from mdln.registry import ENTITY_REGISTRY

class Entity():
    initialized: bool = False

    rect: Rect = None
    
    layer = LAYER_DEFAULT
    
    stage = None
    
    icon: Icon = None
    
    visible: bool = False
    
    active: bool = True
    
    deleted: bool = False

    _component_registry: dict = None

    def __init__(self, rect=None):
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

    def tick(self):
        for component in self._component_registry.values():
            component.tick()

    def draw(self, screen: pg.Surface) -> pg.Surface:
        if self.icon is not None:
            return self.icon.get_surface(self.stage.scene.game.tick)

        for component in self._component_registry.values():
            component.draw(screen)

        return None

    def init(self):
        pass

    def add_component(self, component):
        existing = self.get_component(type(component))

        if existing is not None:
            raise Exception(f"entity already contains existing component of type {type(component)}")

        self._component_registry[type(component)] = component
        component.attach(self)
        component.init()

    def get_component(self, component_type):
        return self._component_registry.get(component_type)

    def del_component(self, component_type) -> bool:
        if self.get_component(component_type) is not None:
            del self._component_registry[component_type]
            return True
        
        return False
    
    def has_component(self, component_type):
        return component_type in self._component_registry
    
    def matches_components(self, component_types):
        for ct in component_types:
            if ct not in self._component_registry:
                return False
        
        return True

    def qdel(self):
        if not self.deleted:
            self.deleted = True
            self.stage._deletion_queue.append(self)

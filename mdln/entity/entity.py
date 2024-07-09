import pygame as pg
import inspect

from mdln.const import *
from mdln.geometry import Rect, Vec2
from mdln.icon import Icon
from mdln.registry import ENTITY_REGISTRY

class Entity():
    rect: Rect = None
    layer = LAYER_DEFAULT
    stage = None
    icon: Icon = None
    visible: bool = False
    ticks: bool = True

    _component_registry = {}

    def __init__(self, rect=None, components=None):
        self.components = components or []
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
        for component in self._component_registry.items():
            component.tick()

    def draw(self) -> pg.Surface:
        if self.icon is not None:
            return self.icon.get_surface(self.stage.scene.game.frame)

        return None

    def init(self):
        pass

    def add_component(self, component):
        existing = self.get_component(type(component))

        if existing is not None:
            raise Exception(f"entity already contains existing component of type {type(component)}")

        self._component_registry[type(component)] = component
        component.attach(self)

    def get_component(self, component_type):
        return self._component_registry.get(component_type)

    def del_component(self, component_type) -> bool:
        if self.get_component(component_type) is not None:
            del self._component_registry[component_type]
            return True
        
        return False
    
    def matches_components(self, component_types):
        for ct in component_types:
            if ct not in self._component_registry:
                return False
        
        return True

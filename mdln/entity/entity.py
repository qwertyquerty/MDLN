import pygame as pg

from mdln.const import *
from mdln.icon import Icon

class Entity():
    rect: pg.Rect = None
    layer = LAYER_DEFAULT
    stage = None
    icon: Icon = None
    visible: bool = False
    _component_registry = {}

    def __init__(self, rect=None, components=None):
        self.components = components or []
        self.rect = rect or pg.Rect(0, 0, RECT_SIZE_DEFAULT[0], RECT_SIZE_DEFAULT[1])

    def tick(self):
        for component in self._component_registry.items():
            component.tick()

    def draw(self) -> pg.Surface:
        if self.icon is not None:
            return self.icon.get_surface(self.stage.scene.game.frame)

        return None

    def event(self, event):
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

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mdln.entity import Entity

import pygame as pg

class Component():
    # public
    
    entity: Entity = None

    def init(self) -> None:
        pass

    def tick(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass

    def _attach(self, entity: Entity) -> None:
        self.entity = entity

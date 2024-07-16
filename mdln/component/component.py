from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mdln.entity import Entity
    from mdln.util import Context

import pygame as pg

class Component():
    # public
    
    entity: Entity = None

    def init(self, ctx: Context) -> None:
        pass

    def tick(self, ctx: Context) -> None:
        pass

    def draw(self, ctx: Context) -> None:
        pass

    def _attach(self, entity: Entity) -> None:
        self.entity = entity

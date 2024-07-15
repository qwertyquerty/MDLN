from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mdln.stage import Stage
    import pygame as pg


class System():
    # public

    initialized: bool = False

    stage: Stage = None

    wait: int = 1

    priority: int = 0

    active: bool = True

    ticks: int = 0

    def init(self) -> None:
        pass

    def tick(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass

    def _attach(self, stage: Stage) -> None:
        self.stage = stage

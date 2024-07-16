from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mdln.stage import Stage
    from mdln.util import Context
    import pygame as pg


class System():
    # public

    initialized: bool = False

    stage: Stage = None

    wait: int = 1

    priority: int = 0

    active: bool = True

    ticks: int = 0

    def _init(self, ctx: Context) -> None:
        ctx.system = self
        self.init(ctx)
    
    def _tick(self, ctx: Context) -> None:
        ctx.system = self
        self.tick(ctx)

        self.ticks += 1

    def init(self, ctx: Context) -> None:
        pass

    def tick(self, ctx: Context) -> None:
        pass

    def draw(self, ctx: Context) -> None:
        pass

    def _attach(self, stage: Stage) -> None:
        self.stage = stage

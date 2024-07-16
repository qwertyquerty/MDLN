from __future__ import annotations
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from mdln.game import Game
    from mdln.stage import Stage
    from mdln.util import Context

from mdln.const import *


class Scene():
    # public

    initialized: bool = False

    stages: list[Stage] = None
    
    game: Game = None

    def __init__(self):
        self.stages = []

    def _init(self, ctx: Context) -> None:
        if not self.initialized:
            self.initialized = True

            ctx.scene = self

            self.init(ctx)

            for stage in self.stages:
                stage._init(ctx)

    def _tick(self, ctx: Context) -> None:
        ctx.scene = self
        self.tick(ctx)

        for stage in self.stages:
            stage._tick(ctx)

    def _draw(self, ctx: Context) -> None:
        ctx.scene = self
        self.draw(ctx)

        for stage in sorted(self.stages, key=lambda s: s.layer):
            stage._draw(ctx)
        
        self.post_draw(ctx)

    def init(self, ctx: Context) -> None:
        pass

    def tick(self, ctx: Context) -> None:
        pass

    def draw(self, ctx: Context) -> None:
        pass
    
    def post_draw(self, ctx: Context) -> None:
        pass

    def add_stage(self, stage) -> Self:
        self.stages.append(stage)
        stage.scene = self

        if self.game and self.game.running and not stage.initialized:
            stage._init(Context.from_scene(self))
        
        return self


from __future__ import annotations
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from mdln.game import Game
    from mdln.stage import Stage

from mdln.const import *


class Scene():
    # public

    initialized: bool = False

    stages: list[Stage] = None
    
    game: Game = None

    def __init__(self):
        self.stages = []

    def _init(self) -> None:
        if not self.initialized:
            self.initialized = True

            self.init()

            for stage in self.stages:
                stage._init()

    def _tick(self) -> None:
        self.tick()

        for stage in self.stages:
            stage._tick()

    def _draw(self, screen: pg.Surface) -> None:
        self.draw(screen)

        for stage in sorted(self.stages, key=lambda s: s.layer):
            stage._draw(screen)
        
        self.post_draw(screen)

    def init(self) -> None:
        pass

    def tick(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass
    
    def post_draw(self, screen: pg.Surface) -> None:
        pass

    def add_stage(self, stage) -> Self:
        self.stages.append(stage)
        stage.scene = self

        if self.game and self.game.running and not stage.initialized:
            stage._init()
        
        return self


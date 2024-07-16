from __future__ import annotations
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from mdln.game import Game
    from mdln.scene import Scene
    from mdln.stage import Stage
    from mdln.entity import Entity
    from mdln.component import Component
    from mdln.system import System
    import pygame as pg

class Context():
    game: Game
    scene: Scene
    stage: Stage
    entity: Entity
    component: Component
    system: System
    surface: pg.Surface

    @classmethod
    def from_game(cls, game: Game) -> Self:
        ctx = cls()
        ctx.game = game
        ctx.surface = ctx.game.screen
        return ctx

    @classmethod
    def from_scene(cls, scene: Scene) -> Self:
        ctx = cls()
        ctx.scene = scene
        ctx.game = ctx.scene.game
        ctx.surface = ctx.game.screen
        return ctx

    @classmethod
    def from_stage(cls, stage: Stage) -> Self:
        ctx = cls()
        ctx.stage = stage
        ctx.scene = ctx.stage.scene
        ctx.game = ctx.scene.game
        ctx.surface = ctx.game.screen
        return ctx

    @classmethod
    def from_entity(cls, entity: Entity) -> Self:
        ctx = cls()
        ctx.entity = entity
        ctx.stage = ctx.entity.stage
        ctx.scene = ctx.stage.scene
        ctx.game = ctx.scene.game
        return ctx

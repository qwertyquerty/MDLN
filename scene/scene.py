from mdln.const import *
from mdln.entity import Entity
from mdln.stage import Stage

class Scene():
    stages: list[Stage] = None
    game = None

    def __init__(self):
        self.stages = []

    def _tick(self):
        self.tick()

        for stage in self.stages:
            stage._tick()

    def _draw(self, screen):
        self.draw(screen)

        for stage in sorted(self.stages, key=lambda s: s.layer):
            stage._draw(screen)

    def _event(self, event):
        self.event(event)

        for stage in self.stages:
            stage._event(event)

    def add_stage(self, stage):
        self.stages.append(stage)
        stage.scene = self

    def tick(self):
        pass

    def draw(self, screen):
        pass

    def event(self, event):
        pass

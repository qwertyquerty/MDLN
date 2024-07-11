from mdln.const import *
from mdln.entity import Entity
from mdln.stage import Stage

class Scene():
    initialized: bool = False

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
        
        self.post_draw(screen)

    def _init(self):
        if not self.initialized:
            self.initialized = True

            self.init()

            for stage in self.stages:
                stage._init()

    def add_stage(self, stage):
        self.stages.append(stage)
        stage.scene = self

        if self.game and self.game.running and not stage.initialized:
            stage._init()

    def tick(self):
        pass

    def draw(self, screen):
        pass
    
    def post_draw(self, screen):
        pass

    def init(self):
        pass

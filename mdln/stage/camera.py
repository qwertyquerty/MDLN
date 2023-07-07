import pygame as pg

from mdln.entity import Entity
from mdln.stage import Stage

class CameraStage(Stage):
    camera_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)
    camera_target: Entity = None

    def _tick(self):
        _ = super()._tick()
    
        if self.camera_target is not None:
            self.camera_pos.update(self.camera_target.rect.center)

        return _

    def _draw(self, screen):
        self.draw(screen)

        for entity in sorted(self.entities, key=lambda e: e.layer):
            if entity.visible:
                surf = entity.draw()

                if surf is not None:
                    screen.blit(surf, entity.rect.topleft - self.camera_pos + self.scene.game.screen.get_rect().center)

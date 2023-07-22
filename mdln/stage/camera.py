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

        display_rect = self.scene.game.display.get_rect()

        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            if entity.visible:
                image_rect = entity.draw()

                scale = self.scene.game.pixel_scaling
                dest = pg.Rect(
                    (entity.rect.left - self.camera_pos.x) * scale + display_rect.centerx,
                    (entity.rect.top - self.camera_pos.y) * scale + display_rect.centery,
                    image_rect.width * scale,
                    image_rect.height * scale
                )
                
                entity.icon.texture.draw(srcrect=image_rect, dstrect=dest)

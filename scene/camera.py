import pygame as pg

from mdln.scene import Scene

class CameraScene(Scene):
    camera_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)

    def _draw(self):
        self.draw()

        for entity in sorted(self.entities, key=lambda e: e.layer):
            if entity.visible:
                surf = entity.draw()

                if surf is not None:
                    self.game.screen.blit(surf, entity.position - self.camera_pos)

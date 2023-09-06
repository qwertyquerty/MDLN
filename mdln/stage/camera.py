import pygame as pg

from mdln.entity import Entity
from mdln.stage import Stage

class CameraStage(Stage):
    camera_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)
    camera_target: Entity = None

    def tick(self):
        if self.camera_target is not None:
            self.camera_pos.update(self.camera_target.rect.center)
    
    def draw_entities(self, screen):
        screen_center = screen.get_rect().center
        screen_size = screen.get_size()

        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            surf = entity.draw()

            if surf is not None:
                dest = entity.rect.topleft - self.camera_pos + screen_center
                surf_size = surf.get_size()

                if dest.x < screen_size[0] and dest.x + surf_size[0] > 0 and dest.y < screen_size[1] and dest.y + surf_size[1] > 0:
                    screen.blit(surf, dest)

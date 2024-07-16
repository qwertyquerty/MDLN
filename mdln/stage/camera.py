from mdln.entity import Entity
from mdln.stage import Stage
from mdln.geometry import Vec2, Rect

class CameraStage(Stage):
    # public
    
    camera_pos: Vec2 = Vec2(0, 0)
    
    camera_target: Entity = None

    def tick(self, ctx):
        if self.camera_target is not None:
            self.camera_pos.set(self.camera_target.rect.center())
    
    def draw_entities(self, ctx):
        screen_rect = Rect.from_pg(ctx.surface.get_rect())

        self.entities.sort(key=lambda e: e.layer)

        for entity in self.entities:
            surf = entity.draw(ctx)

            if surf is not None:
                surf_rect = Rect(
                    entity.rect.topleft() - self.camera_pos + screen_rect.center(),
                    Vec2(*surf.get_size())
                )

                if screen_rect.intersects_rect(surf_rect):
                    ctx.surface.blit(surf, surf_rect.to_tuple())

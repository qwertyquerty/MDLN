import pygame as pg

from mdln.const import *
from mdln.scene import Scene

class Game():
    clock: pg.time.Clock = None

    window: pg.Surface = None

    running: bool = False

    screen_size = SCREEN_SIZE_DEFAULT

    pixel_scaling = PIXEL_SCALE_DEFAULT

    event_handlers: dict = None

    title: str = TITLE_DEFAULT

    icon: pg.Surface = ICON_DEFAULT

    display_flags: int = DISPLAY_FLAGS_DEFAULT

    background_color: tuple = COLOR_BACKGROUND_DEFAULT

    _scene: Scene = None

    def __init__(self,
        screen_size = SCREEN_SIZE_DEFAULT,
        fps: int = FPS_DEFAULT,
        pixel_scaling: int = PIXEL_SCALE_DEFAULT,
        title: str = TITLE_DEFAULT,
        icon: pg.Surface = ICON_DEFAULT,
        display_flags: int = DISPLAY_FLAGS_DEFAULT,
        background_color: tuple = COLOR_BACKGROUND_DEFAULT
    ):
        self.screen_size = screen_size
        self.fps = fps
        self.pixel_scaling = int(pixel_scaling)
        self.display_flags = display_flags
        self.background_color = background_color

        self.event_handlers = {}

        self.screen = pg.Surface(screen_size)

        self.window = pg.display.set_mode(((self.screen_size[0] * self.pixel_scaling), (self.screen_size[1] * self.pixel_scaling)), self.display_flags)
        self.clock = pg.time.Clock()

        self.title = title
        pg.display.set_caption(self.title)

        self.icon = icon
        pg.display.set_icon(icon)

        self.running = False

    def start(self):
        self.running = True

        while self.running:
            for event in pg.event.get():
                self._event(event)
            self._tick()
            self._draw()
            self.clock.tick(self.fps)

    def _event(self, event):
        self.event(event)

        if event.type in self.event_handlers:
            for handler in self.event_handlers[event.type]:
                handler(event)
        
        if self._scene is not None:
            self._scene._event(event)

    def _tick(self):
        self.tick()

        if self._scene is not None:
            self._scene._tick()

    def _draw(self):
        self.draw()

        self.screen.fill(self.background_color)

        if self._scene is not None:
            self._scene._draw()

        if self.pixel_scaling != 1:
            pg.transform.scale_by(self.screen, self.pixel_scaling, self.window)
        else:
            self.window.blit(self.screen, (0,0))

        pg.display.flip()

    def handler(self, event_type):
        def decorator(handler):
            if event_type in self.event_handlers:
                self.event_handlers[event_type].append(handler)
            else:
                self.event_handlers[event_type] = [handler]

        return decorator

    def set_scene(self, scene: Scene):
        self._scene = scene
        self._scene.game = self
    
    def get_scene(self):
        return self._scene

    def event(self, event):
        pass

    def tick(self):
        pass

    def draw(self):
        pass


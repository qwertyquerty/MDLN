import pygame as pg
import pygame._sdl2

from mdln.const import *
from mdln.scene import Scene
from mdln.util import load_all_entities_from_path

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

    frame = 0

    def __init__(self,
        screen_size = SCREEN_SIZE_DEFAULT,
        fps: int = FPS_DEFAULT,
        pixel_scaling: int = PIXEL_SCALE_DEFAULT,
        title: str = TITLE_DEFAULT,
        icon: pg.Surface = ICON_DEFAULT,
        display_flags: int = DISPLAY_FLAGS_DEFAULT,
        background_color: tuple = COLOR_BACKGROUND_DEFAULT,
        window: pg.Surface = None,
        entity_path: str = None
    ):
        self.screen_size = screen_size
        self.fps = fps
        self.pixel_scaling = int(pixel_scaling)
        self.display_flags = display_flags
        self.background_color = background_color

        self.event_handlers = {}

        self.display = pg.display.set_mode(((self.screen_size[0] * self.pixel_scaling), (self.screen_size[1] * self.pixel_scaling)), self.display_flags)
        self.window = pygame._sdl2.video.Window.from_display_module()
        self.screen = pygame._sdl2.video.Renderer(self.window, accelerated=1, index=1)

        self.clock = pg.time.Clock()

        self.title = title
        pg.display.set_caption(self.title)

        self.icon = icon
        pg.display.set_icon(icon)

        self.frame = 0

        self.running = False

        if entity_path != None:
            load_all_entities_from_path(entity_path)

    def start(self):
        self.init()
        
        self.running = True

        while self.running:
            for event in pg.event.get():
                self._event(event)
            self._tick()
            self._draw()
            
            self.clock.tick(self.fps)

            self.frame += 1

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
        self.screen.draw_color = self.background_color
        self.screen.fill_rect(self.display.get_rect())

        self.draw(self.screen)

        if self._scene is not None:
            self._scene._draw(self.screen)

        self.screen.present()

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
        scene.init()
    
    def get_scene(self):
        return self._scene

    def get_fps(self):
        return self.clock.get_fps()

    def event(self, event):
        pass

    def tick(self):
        pass

    def draw(self, screen):
        pass

    def init(self):
        pass

import pygame as pg

from mdln.const import *
from mdln.glob import event_handlers
from mdln.geometry import Vec2
from mdln.scene import Scene
from mdln.util import load_all_entities_from_path

class Game():
    clock: pg.time.Clock = None

    window: pg.Surface = None

    running: bool = False

    screen_size: Vec2 = SCREEN_SIZE_DEFAULT

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
        entity_path: str = None,
        tick_interval: int = 1
    ):
        self.screen_size = screen_size
        self.fps = fps
        self.pixel_scaling = int(pixel_scaling)
        self.display_flags = display_flags
        self.background_color = background_color

        self.event_handlers = {}

        self.screen = pg.Surface(screen_size)

        if window:
            self.window = window
        else:
            self.window = pg.display.set_mode(((self.screen_size[0] * self.pixel_scaling), (self.screen_size[1] * self.pixel_scaling)), self.display_flags)
    
        self.clock = pg.time.Clock()

        self.set_title(title)
        
        self.icon = icon
        pg.display.set_icon(icon)

        self.frame = 0

        self.running = False

        self.tick_interval = tick_interval

        if entity_path != None:
            load_all_entities_from_path(entity_path)

    def set_title(self, title: str):
        self._title = title
        pg.display.set_caption(self._title)

    def start(self):
        self._init()

        self.running = True

        while self.running:
            for event in pg.event.get():
                self._event(event)

            if self.frame % self.tick_interval == 0:
                self._tick()
            
            self._draw()
            
            self.clock.tick(self.fps)

            self.frame += 1

    def _event(self, event):
        if event.type in event_handlers:
            for handler in event_handlers[event.type]:
                handler(event)

    def _tick(self):
        self.tick()

        if self._scene is not None:
            self._scene._tick()

    def _draw(self):
        self.draw(self.screen)

        self.screen.fill(self.background_color)

        if self._scene is not None:
            self._scene._draw(self.screen)

        if self.pixel_scaling != 1:
            pg.transform.scale_by(self.screen, self.pixel_scaling, self.window)
        else:
            self.window.blit(self.screen, (0,0))

        pg.display.flip()
    
    def _init(self):
        self.init()

        if self._scene:
            self._scene._init()

    def set_scene(self, scene: Scene):
        self._scene = scene
        self._scene.game = self
        scene.init()
    
    def get_scene(self):
        return self._scene

    def get_fps(self):
        return self.clock.get_fps()

    def tick(self):
        pass

    def draw(self, screen):
        pass

    def init(self):
        pass

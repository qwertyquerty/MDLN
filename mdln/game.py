import pygame as pg

from mdln.const import *
from mdln.glob import event_handlers
from mdln.geometry import Vec2
from mdln.scene import Scene
from mdln.util import load_all_entities_from_path

from typing import Self

class Game():
    # public
    
    scene: Scene = None

    initialized: bool = False

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

    tick: int = 0

    def __init__(self,
        screen_size: Vec2 = SCREEN_SIZE_DEFAULT,
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

        self.ticks = 0

        self.running = False

        self.tick_interval = tick_interval

        if entity_path != None:
            load_all_entities_from_path(entity_path)

    def _event(self, event):
        if event.type in event_handlers:
            for handler in event_handlers[event.type]:
                handler(event)
    
    def _init(self):
        if not self.initialized:
            self.initialized = True

            self.init()

            if self.scene:
                self.scene._init()

    def _tick(self):
        self.tick()

        if self.scene is not None:
            self.scene._tick()

    def _draw(self):
        self.draw(self.screen)

        self.screen.fill(self.background_color)

        if self.scene is not None:
            self.scene._draw(self.screen)

        if self.pixel_scaling != 1:
            pg.transform.scale_by(self.screen, self.pixel_scaling, self.window)
        else:
            self.window.blit(self.screen, (0,0))

        pg.display.flip()

    def init(self) -> None:
        pass

    def tick(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass

    def start(self):
        self._init()

        self.running = True

        while self.running:
            for event in pg.event.get():
                self._event(event)

            if self.ticks % self.tick_interval == 0:
                self._tick()
            
            self._draw()
            
            self.clock.tick(self.fps)

            self.ticks += 1

    def set_title(self, title: str) -> Self:
        self._title = title
        pg.display.set_caption(self._title)
        return self

    def set_scene(self, scene: Scene) -> Self:
        self.scene = scene
        self.scene.game = self

        if self.running and not scene.initialized:
            scene._init()
        
        return self

    def get_fps(self) -> int:
        return self.clock.get_fps()

    def get_pixel_mouse_pos(self) -> Vec2:
        return (Vec2(*pg.mouse.get_pos()) / self.pixel_scaling).floored()

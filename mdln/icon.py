from collections import namedtuple
import pygame as pg
import pygame._sdl2

from mdln.const import *
from mdln.resource import load_icon, try_convert_surface, RESOURCE_CACHE_ICON

IconState = namedtuple("IconState", "row col length wait loop always_reset")

texture_cache = None

class Icon():
    sprite_map: pg.Surface = None
    metadata: dict = {}
    size: pg.math.Vector2 = None
    states: dict = {}

    has_alpha = True

    _state_name = None
    _state = None
    _animation_start_frame = 0
    _state_just_changed = False

    _converted = False

    def __init__(self, resource, icon_state=None):
        self.resource = resource

        self.sprite_map, self.metadata, self._converted = load_icon(self.resource)

        self.texture = None

        self.size = pg.math.Vector2(*(self.metadata.get("size") or ICON_SIZE_DEFAULT))

        self.has_alpha = self.metadata.get("has_alpha", True)

        self.states = {}

        if self.metadata.get("states"):
            for name in self.metadata.get("states"):
                state = IconState(
                    row = self.metadata["states"][name].get("row", 0),
                    col = self.metadata["states"][name].get("col", 0),
                    length = self.metadata["states"][name].get("length", 1),
                    wait = self.metadata["states"][name].get("wait", 1),
                    loop = self.metadata["states"][name].get("loop", True),
                    always_reset = self.metadata["states"][name].get("always_reset", True)
                    # TODO: after complete, switch to different state idea
                )

                self.states[name] = state
        
        self.set_state(icon_state)

    def get_state(self):
        return self._state

    def set_state(self, icon_state: str, restart=True):
        if icon_state not in self.states and icon_state != None:
            raise ValueError(f"nonexistent icon state {icon_state}")
    
        if self._state_name != icon_state:
            self._state_name = icon_state
            self._state = self.states[icon_state]

            if restart:
                self._state_just_changed = True

    def get_image(self, frame, screen):
        if not self.texture:
            self.texture = pygame._sdl2.video.Texture.from_surface(screen, self.sprite_map)
            
        if self._state_just_changed:
            self._state_just_changed = False
            if self._state.always_reset:
                self._animation_start_frame = frame

        if self._state:
            row = self._state.row

            if self._state.loop:
                col = self._state.col + ((frame - self._animation_start_frame) // self._state.wait) % self._state.length
            else:
                col = self._state.col + min((frame - self._animation_start_frame) // self._state.wait, self._state.length - 1)

        else:
            row = 0
            col = 0
    
        return pg.Rect(self.size.x*col, self.size.y*row, self.size.x, self.size.y)

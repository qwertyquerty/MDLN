import pygame as pg
import os
import sys

from mdln.geometry import Vec2

LAYER_BOTTOM = -sys.maxsize - 1
LAYER_DEFAULT = 0
LAYER_TOP = sys.maxsize

FPS_UNLIMITED = -1
FPS_DEFAULT = 60

PIXEL_SCALE_DEFAULT = 1

SCREEN_SIZE_DEFAULT = Vec2(640, 480)

TITLE_DEFAULT = "MDLN Window"

ICON_DEFAULT = pg.Surface((0,0))

DISPLAY_FLAGS_DEFAULT = pg.DOUBLEBUF | pg.HWACCEL

COLOR_BACKGROUND_DEFAULT = pg.Color(128, 128, 128, 255)

RESOURCE_PATH = os.path.join(".", "resource")
DATA_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "data")
ICON_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "icon")
SOUND_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "sound")


ICON_SIZE_DEFAULT = (16, 16)

RECT_SIZE_DEFAULT = (16, 16)

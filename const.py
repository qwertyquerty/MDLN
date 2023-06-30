import pygame as pg
import os
import sys

LAYER_BOTTOM = -sys.maxsize - 1
LAYER_DEFAULT = 0
LAYER_TOP = sys.maxsize


FPS_DEFAULT = 60

PIXEL_SCALE_DEFAULT = 1

SCREEN_SIZE_DEFAULT = (640, 480)

TITLE_DEFAULT = "MDLN Window"

ICON_DEFAULT = pg.Surface((0,0))

DISPLAY_FLAGS_DEFAULT = pg.DOUBLEBUF | pg.HWACCEL


BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLOR_BACKGROUND_DEFAULT = GRAY

RESOURCE_PATH = os.path.join(".", "resource")
DATA_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "data")
ICON_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "icon")
SOUND_RESOURCE_PATH = os.path.join(RESOURCE_PATH, "sound")


ICON_SIZE_DEFAULT = (16, 16)

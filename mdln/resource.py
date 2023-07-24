import pygame as pg
import pygame._sdl2.video

import yaml

from mdln.const import *
from mdln.util import resource_to_path

RESOURCE_CACHE_SOUND = {}
RESOURCE_CACHE_ICON = {}
RESOURCE_CACHE_TEXTURE = {}

def load_icon(resource, use_cache=True):
    if resource in RESOURCE_CACHE_ICON and use_cache:
        return RESOURCE_CACHE_ICON[resource]

    image_path = os.path.join(ICON_RESOURCE_PATH, resource_to_path(resource)+".png")
    meta_path = os.path.join(ICON_RESOURCE_PATH, resource_to_path(resource)+".yml")

    surface = pg.image.load(image_path)
    metadata = yaml.safe_load(open(meta_path))

    if use_cache:
        RESOURCE_CACHE_ICON[resource] = (surface, metadata)

    return (surface, metadata)

def load_texture(resource, renderer, use_cache=True):
    if resource in RESOURCE_CACHE_TEXTURE and use_cache:
        return RESOURCE_CACHE_TEXTURE[resource]
    
    icon, meta = load_icon(resource)

    texture = pygame._sdl2.video.Texture.from_surface(renderer, icon)

    if use_cache:
        RESOURCE_CACHE_TEXTURE[resource] = texture
    
    return texture

def load_sound(resource, use_cache=True):
    if resource in RESOURCE_CACHE_SOUND and use_cache:
        return RESOURCE_CACHE_SOUND[resource]


    path = os.path.join(SOUND_RESOURCE_PATH, resource_to_path(resource))
    sound = pg.mixer.Sound(file=path)

    if use_cache:
        RESOURCE_CACHE_SOUND[resource] = sound

    return sound

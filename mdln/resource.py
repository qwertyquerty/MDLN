import pygame as pg

import yaml

from mdln.const import *
from mdln.util import resource_to_path

RESOURCE_CACHE_SOUND = {}
RESOURCE_CACHE_ICON = {}

def load_icon(resource, use_cache=True):
    if resource in RESOURCE_CACHE_ICON and use_cache:
        # TODO: named tuple maybe
        if not RESOURCE_CACHE_ICON[resource][2]:
            new_surface = try_convert_surface(RESOURCE_CACHE_ICON[resource][0], RESOURCE_CACHE_ICON[resource][1])

            if new_surface:
                RESOURCE_CACHE_ICON[resource][0] = new_surface
                RESOURCE_CACHE_ICON[resource][2] = True

        return RESOURCE_CACHE_ICON[resource]

    image_path = os.path.join(ICON_RESOURCE_PATH, resource_to_path(resource)+".png")
    meta_path = os.path.join(ICON_RESOURCE_PATH, resource_to_path(resource)+".yml")

    surface = pg.image.load(image_path)
    metadata = yaml.safe_load(open(meta_path))
    converted = False

    new_surface = try_convert_surface(surface, metadata)

    if new_surface:
        surface = new_surface
        converted = True

    if use_cache:
        RESOURCE_CACHE_ICON[resource] = [surface, metadata, converted]

    return [surface, metadata, converted]

def try_convert_surface(surface, metadata):
    try:
        if metadata.get("has_alpha", True):
            return surface.convert_alpha()
        else:
            return surface.convert()
        
    except pg.error:
        return False

def load_sound(resource, use_cache=True):
    if resource in RESOURCE_CACHE_SOUND and use_cache:
        return RESOURCE_CACHE_SOUND[resource]


    path = os.path.join(SOUND_RESOURCE_PATH, resource_to_path(resource))
    sound = pg.mixer.Sound(file=path)

    if use_cache:
        RESOURCE_CACHE_SOUND[resource] = sound

    return sound

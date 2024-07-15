import pygame as pg

from mdln.glob import event_handlers

from typing import Callable

Event = pg.event.Event

def ON_EVENT(event_type: int, handler: Callable):
    if event_type in event_handlers:
        event_handlers[event_type].append(handler)
    else:
        event_handlers[event_type] = [handler]

def SEND_EVENT(event: int) -> None:
    pg.event.post(event)

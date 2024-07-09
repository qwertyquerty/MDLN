import pygame as pg

from mdln.glob import event_handlers

Event = pg.event.Event

def ON_EVENT(event_type, handler):
    if event_type in event_handlers:
        event_handlers[event_type].append(handler)
    else:
        event_handlers[event_type] = [handler]

def SEND_EVENT(event):
    pg.event.post(event)

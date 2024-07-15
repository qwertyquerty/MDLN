import math
from typing import Iterator, Self, Union
from numbers import Number
import pygame as pg

from .vector import Vec2

class Rect():
    # public
    
    origin: Vec2 = None

    size: Vec2 = None

    def __init__(self, origin: Vec2, size: Vec2):
        self.origin: Vec2 = origin
        self.size: Vec2 = size
    
    @classmethod
    def from_pg(cls, rect: pg.Rect):
        return cls(Vec2(rect.top, rect.left), Vec2(rect.left, rect.right))
    
    def to_pg(self) -> pg.Rect:
        return pg.Rect(self.origin.x, self.origin.y, self.size.x, self.size.y)

    def topleft(self) -> Vec2: return self.origin.copy()
    
    def set_topleft(self, point: Vec2):
        self.origin.x = point.x
        self.origin.y = point.y
    
    def topright(self) -> Vec2: return self.origin + Vec2(self.size.x, 0)

    def set_topright(self, point: Vec2):
        self.origin.x = point.x - self.size.x
        self.origin.y = point.y

    def botleft(self) -> Vec2: return self.origin + Vec2(0, self.size.y)

    def set_botleft(self, point: Vec2):
        self.origin.x = point.x
        self.origin.y = point.y - self.size.y

    def botright(self) -> Vec2: return self.origin + self.size

    def set_botright(self, point: Vec2):
        self.origin.x = point.x - self.size.x
        self.origin.y = point.y - self.size.y

    def center(self) -> Vec2: return self.origin + (self.size / 2)

    def set_center(self, point: Vec2):
        self.origin.x = point.x - self.size.x / 2
        self.origin.y = point.y - self.size.y / 2

    def topcenter(self) -> Vec2: return self.origin + Vec2(self.size.x / 2, 0)
    
    def set_topcenter(self, point: Vec2):
        self.origin.x = point.x - self.size.x / 2
        self.origin.y = point.y

    def botcenter(self) -> Vec2: return self.origin + Vec2(self.size.x / 2, self.size.y)

    def set_botcenter(self, point: Vec2):
        self.origin.x = point.x - self.size.x / 2
        self.origin.y = point.y - self.size.y

    def leftcenter(self) -> Vec2: return self.origin + Vec2(0, self.size.y / 2)

    def set_leftcenter(self, point: Vec2):
        self.origin.x = point.x
        self.origin.y = point.y - self.size.y / 2

    def rightcenter(self) -> Vec2: return self.origin + Vec2(self.size.x, self.size.y / 2)

    def set_rightcenter(self, point: Vec2):
        self.origin.x = point.x - self.size.x
        self.origin.y = point.y - self.size.y / 2

    def left(self) -> Number: return self.origin.x
    
    def set_left(self, value: Number):
        self.origin.x = value

    def right(self) -> Number: return self.origin.x + self.size.x

    def set_right(self, value: Number):
        self.origin.x = value - self.size.x
    
    def top(self) -> Number: return self.origin.y

    def set_top(self, value: Number):
        self.origin.y = value

    def bottom(self) -> Number: return self.origin.y + self.size.y

    def set_bottom(self, value: Number):
        self.origin.y = value - self.size.y

    def area(self) -> Number:
        return self.size.x * self.size.y
    
    def perimeter(self):
        return self.size.x * 2 + self.size.y * 2

    def contains_vector(self, other: Vec2, inclusive: bool = False) -> bool:
        if inclusive:
            return other.x >= self.left() and other.x <= self.right() and other.y >= self.top() and other.y <= self.bottom()
        else:
            return other.x > self.left() and other.x < self.right() and other.y > self.top() and other.y < self.bottom()

    def contains_rect(self, other: Self, inclusive: bool = False) -> bool:
        if inclusive:
            return other.left() >= self.left() and other.right() <= self.right() and other.top() >= self.top() and other.bottom() <= self.bottom()
        else:
            return other.left() > self.left() and other.right() < self.right() and other.top() > self.top() and other.bottom() < self.bottom()

    def intersects_rect(self, other: Self, inclusive: bool = False) -> bool:
        if inclusive:
            return self.left() <= other.right() and self.right() >= other.left() and self.top() <= other.bottom() and self.bottom() >= other.top()
        else:
            return self.left() < other.right() and self.right() > other.left() and self.top() < other.bottom() and self.bottom() > other.top()

    def is_square(self) -> bool:
        return self.size.x == self.size.y

    def to_tuple(self) -> tuple:
        return (self.origin.x, self.origin.y, self.size.x, self.size.y)
    
    def floored(self) -> Self:
        return Rect(self.origin.floored(), self.size.floored())

    def copy(self) -> Self:
        return Rect(self.origin.copy(), self.size.copy())

    def __str__(self) -> str:
        return f"Rect[{str(self.origin)}, {str(self.size)}]"
    
    def __repr__(self) -> str:
        return str(self)
    
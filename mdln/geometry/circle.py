import math
from typing import Iterator, Self, Union
from numbers import Number

from .rect import Rect
from .vector import Vec2

class Circle():
    # public
    
    center: Vec2 = None

    radius: Number = None

    def __init__(self, center: Vec2, radius: Number):
        self.center = center
        self.radius = radius
    
    def area(self) -> Number:
        return math.pi * self.radius**2
    
    def circumference(self) -> Number:
        return math.pi * self.radius * 2
    
    def contains_vector(self, point: Vec2, inclusive: bool = False) -> bool:
        if inclusive:
            return self.radius**2 >= (self.center - point).sq_mag()
        else:
            return self.radius**2 > (self.center - point).sq_mag()
        
    def intersects_circle(self, other: Self, inclusive: bool = False) -> bool:
        if inclusive:
            return (self.radius + other.radius)**2 >= (self.center - other.center).sq_mag()
        else:
            return (self.radius + other.radius)**2 > (self.center - other.center).sq_mag()

    def contains_circle(self, other: Self, inclusive: bool = False) -> bool:
        if inclusive:
            return (self.radius-other.radius)**2 >= (self.center - other.center).sq_mag()
        else:
            return (self.radius-other.radius)**2 > (self.center - other.center).sq_mag()

    def bounding_box(self) -> Rect:
        return Rect(
            self.center.copy() - self.radius,
            Vec2(self.radius * 2, self.radius * 2)
        )

    def point_at_angle(self, angle: Number) -> Self:
        return Vec2(self.center.x + math.cos(angle) * self.radius, self.center.y + math.sin(angle) * self.radius)
    
    def copy(self) -> Self:
        return Circle(self.center.copy(), self.radius)

    def __str__(self) -> str:
        return f"Circle[{str(self.center)}, {self.radius}]"
    
    def __repr__(self) -> str:
        return str(self)
    
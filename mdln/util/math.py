import math
from typing import Iterator, Self, Union
from numbers import Number

class Vec2():
    """2 dimensional vector"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            return Vec2(self.x+other, self.y+other)
        elif isinstance(other, Vec2):
            return Vec2(self.x+other.x, self.y+other.y)
        else:
            raise TypeError(f"cant add {type(self)} and {type(other)}")

    def __sub__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            return Vec2(self.x-other, self.y-other)
        elif isinstance(other, Vec2):
            return Vec2(self.x-other.x, self.y-other.y)
        else:
            raise TypeError(f"cant subtract {type(self)} and {type(other)}")

    def __mul__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            return Vec2(self.x*other, self.y*other)
        elif isinstance(other, Vec2):
            return Vec2(self.x*other.x, self.y*other.y)
        else:
            raise TypeError(f"cant multiply {type(self)} and {type(other)}")

    def __truediv__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            return Vec2(self.x/other, self.y/other)
        elif isinstance(other, Vec2):
            return Vec2(self.x/other.x, self.y/other.y)
        else:
            raise TypeError(f"cant divide {type(self)} and {type(other)}")

    def __pow__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            return Vec2(self.x**other, self.y**other)
        elif isinstance(other, Vec2):
            return Vec2(self.x**other.x, self.y**other.y)
        else:
            raise TypeError(f"cant exponentiate {type(self)} and {type(other)}")

    def __iadd__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            self.x += other
            self.y += other
        elif isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
        else:
            raise TypeError(f"cant add {type(self)} and {type(other)}")

        return self

    def __isub__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            self.x -= other
            self.y -= other
        elif isinstance(other, Vec2):
            self.x -= other.x
            self.y -= other.y
        else:
            raise TypeError(f"cant subtract {type(self)} and {type(other)}")
        
        return self

    def __imul__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            self.x *= other
            self.y *= other
        elif isinstance(other, Vec2):
            self.x *= other.x
            self.y *= other.y
        else:
            raise TypeError(f"cant multiply {type(self)} and {type(other)}")
        
        return self

    def __rmul__(self, other: Union[Self, Number]) -> Self:
        return self.__mul__(other)

    def __idiv__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            self.x /= other
            self.y /= other
        elif isinstance(other, Vec2):
            self.x /= other.x
            self.y /= other.y
        else:
            raise TypeError(f"cant divide {type(self)} and {type(other)}")
    
        return self

    def __ipow__(self, other: Union[Self, Number]) -> Self:
        if isinstance(other, (float, int)):
            self.x **= other
            self.y **= other
        elif isinstance(other, Vec2):
            self.x **= other.x
            self.y **= other.y
        else:
            raise TypeError(f"cant exponentiate {type(self)} and {type(other)}")

        return self

    def __neg__(self) -> Self:
        return Vec2(-self.x, -self.y)

    def __pos__(self) -> Self:
        return Vec2(self.x, self.y)

    def __eq__(self, other: Self) -> bool:
        return isinstance(other, Vec2) and self.x == other.x and self.y == other.y

    def __ne__(self, other: Self) -> bool:
        return not isinstance(other, Vec2) or self.x != other.x or self.y != other.y

    def mag(self) -> float:
        """magnitude of vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def dot(self, other: Self) -> float:
        """self dot other"""
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: Self) -> float:
        """self cross other"""
        return self.x * other.y - self.y * other.x
    
    def project(self, other: Self) -> Self:
        """vector projection of other onto self"""
        return self * (other.dot(self) / (self.x ** 2 + self.y ** 2))

    def angle(self) -> float:
        """arctangent in radians"""
        return math.atan2(self.y, self.x)
    
    def copy(self) -> Self:
        """copy of this vector"""
        return Vec2(self.x, self.y)
    
    def set(self, other: Union[Self, tuple, list]) -> Self:
        """assume the value of another vector or vector-like"""
        if isinstance(other, Vec2):
            self.x = other.x
            self.y = other.y
        elif isinstance(other, (tuple, list)):
            self.x = other[0]
            self.y = other[1]
        else:
            raise TypeError(f"cannot set to {type(other)}")
        
        return self

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"
    
    def __repr__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterator[int]:
        yield self.x
        yield self.y
    
    def __len__(self) -> int:
        return 2

    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0


def clamp(val: float, minimum: float, maximum: float) -> float:
    return min(max(val, minimum), maximum)

def lerp(start: float, end: float, t: float) -> float:
    return start * (1 - t) + end * t

def inverse_lerp(start: float, end: float, v: float) -> float:
    return (-start + v) / (end - start)

def smoothstep(start: float, end: float, t: float) -> float:
    return t * t * (3 - (2 * t)) * (end - start) + start


def lerp(start: float, end: float, t: float) -> float:
    return (1 - t) * start + t * end

def inverse_lerp(start: float, end: float, v: float) -> float:
    return (v - start) / (end - start)

def clamp(val: float, minimum: float, maximum: float) -> float:
    return min(max(val, minimum), maximum)



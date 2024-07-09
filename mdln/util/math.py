def clamp(val: float, minimum: float, maximum: float) -> float:
    return min(max(val, minimum), maximum)

def lerp(start: float, end: float, t: float) -> float:
    return start * (1 - t) + end * t

def inverse_lerp(start: float, end: float, v: float) -> float:
    return (-start + v) / (end - start)

def smoothstep(start: float, end: float, t: float) -> float:
    return t * t * (3 - (2 * t)) * (end - start) + start


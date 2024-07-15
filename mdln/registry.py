from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mdln.entity import Entity

# map from entity path to type
ENTITY_REGISTRY = {}

def get_entity_type(type_path: str) -> Entity:
    t = ENTITY_REGISTRY.get(type_path.lower())

    if t is None:
        raise Exception(f"Invalid type path: {type_path}")

    return t

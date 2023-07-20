# map from entity path to type
ENTITY_REGISTRY = {}

def get_entity_type(type_path):
    t = ENTITY_REGISTRY.get(type_path.lower())

    if t is None:
        raise Exception(f"Invalid type path: {type_path}")

    return t

import os
from pathlib import Path

def resource_to_path(resource: str) -> str:
    return os.path.join(*resource.split("."))

def load_all_entities_from_path(path: str) -> None:
    for root, dirs, files in os.walk(os.path.join(*Path(path).parts)):
        for file_path in files:
            if file_path.endswith('.py'):
                tree = (os.path.join(root, file_path)).split(os.sep)
                tree[-1] = tree[-1].split(".")[0]
                __import__(".".join(tree))

import os

def resource_to_path(resource):
    return os.path.join(*resource.split("."))

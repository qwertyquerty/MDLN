class Component():
    entity = None

    def __init__(self, entity=None):
        self.entity = entity

    def tick(self):
        pass

    def draw(self, screen):
        pass

    def attach(self, entity):
        self.entity = entity

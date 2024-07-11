class System():
    initialized: bool = False
    
    stage = None

    wait: int = 1

    priority: int = 0

    active: bool = True

    ticks: int = 0

    def __init__(self, stage=None):
        self.stage = stage

    def init(self):
        pass

    def tick(self):
        pass

    def attach(self, stage):
        self.stage = stage

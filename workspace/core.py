import os


class WorkSpace:
    def __init__(self, name):
        self.name = name
        self.created = False

    def build(self):
        if not os.path.exists(self.name):
            os.mkdir(self.name)
            self.created = True

    @property
    def was_created(self):
        return self.created

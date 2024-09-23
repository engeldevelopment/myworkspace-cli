import os
from os import mkdir
from os.path import exists, join
from typing import List

from .exceptions import ThisIsNotAWorkspace


class Workspace:
    def __init__(self, name):
        self.name = name
        self.created = False
        self.children: List[Workspace] = []
        self.parent = None

    def build(self):
        if not exists(self.path):
            mkdir(self.path)
            self.build_my_children()
            self.created = True

    def build_my_children(self):
        for child in self.children:
            child.build()

    def add_child(self, child):
        if not isinstance(child, Workspace):
            raise ThisIsNotAWorkspace()
        child.parent = self
        self.children.append(child)
    
    def __str__(self) -> str:
        return self.name

    @property
    def path(self):
        if self.parent is None:
            return join(os.getcwd(), self.name)
        return join(self.parent.path, self.name)

    @property
    def was_created(self):
        return self.created

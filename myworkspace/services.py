import os
from typing import List
import json

from .core import Workspace


class WorkspaceRepository:
    def __init__(self, path: str, name: str = "myworkspace.json") -> None:
        self.path = path
        self.name = name

    def all(self) -> List[Workspace]:
        workspaces = []
        path = os.path.join(self.path, self.name)
        with open(path, "r") as f:
            data = json.load(f)
            for workspace in data:
                workspaces.append(Workspace(name=workspace["name"]))
        return workspaces


class WorkspaceService:
    def __init__(self, name: str):
        self.name = name
        self.repository = WorkspaceRepository()

    def build(self) -> Workspace:
        workspace = Workspace(name=self.name)
        workspaces = self.repository.all()

        for work in workspaces:
            workspace.add_child(child=work) 

        workspace.build()
        return workspace


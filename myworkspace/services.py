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
                work = Workspace(name=workspace["name"])
                if "children" in workspace:
                    for child in workspace["children"]:
                        work.add_child(Workspace(name=child["name"]))
                workspaces.append(work)
        return workspaces


class WorkspaceService:
    def __init__(self, name: str):
        self.name = name
        self.repository = WorkspaceRepository(path=os.getcwd())

    def build(self) -> Workspace:
        workspace = Workspace(name=self.name)
        workspaces = self.repository.all()

        for work in workspaces:
            workspace.add_child(child=work) 

        workspace.build()
        return workspace


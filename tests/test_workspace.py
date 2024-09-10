from myworkspace.core import Workspace
from myworkspace.exceptions import ThisIsNotAWorkspace

import pytest


@pytest.fixture
def workspace():
    return Workspace(name="dev")


def test_da_error_si_intento_agregar_un_child_que_no_es_un_workspace(workspace):
    with pytest.raises(ThisIsNotAWorkspace):
        workspace.add_child("child")

    with pytest.raises(ThisIsNotAWorkspace):
        workspace.add_child(None)


def test_se_puede_crear_el_workspace(mocker, workspace):
    exists_mock = mocker.patch("myworkspace.core.exists")
    mkdir_mock = mocker.patch("myworkspace.core.mkdir")
    exists_mock.return_value = False

    workspace.add_child(Workspace(name="python"))
    workspace.add_child(Workspace(name="js"))
    workspace.add_child(Workspace(name="ruby"))

    workspace.build()

    assert workspace.was_created
    assert mkdir_mock.call_count == 4


def test_si_existe_no_podra_crearse(workspace, mocker):
    exists_mock = mocker.patch("myworkspace.core.exists")
    mkdir_mock = mocker.patch("myworkspace.core.mkdir")
    exists_mock.return_value = True

    workspace.build()

    assert not workspace.was_created
    mkdir_mock.assert_not_called()


def test_el_path_de_un_workspace_sera_la_concatenacion_de_su_nombre(mocker):
    env = mocker.patch("os.getcwd")
    env.return_value = "/user"
    workspace = Workspace(name="development")
    python = Workspace(name="python")
    workspace.add_child(python)

    assert "development" in workspace.path
    assert "python" in python.path

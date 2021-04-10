import pytest

from pytest_mock import mocker

from workspace.core import WorkSpace
from workspace.exceptions import ThisIsNotAWorkspace


@pytest.fixture
def workspace():
    return WorkSpace(name="dev")


def test_da_error_si_intento_agregar_un_child_que_no_es_un_workspace(workspace):
    with pytest.raises(ThisIsNotAWorkspace):
        workspace.add_child("child")

    with pytest.raises(ThisIsNotAWorkspace):
        workspace.add_child(None)


def test_se_puede_crear_el_workspace(mocker, workspace):
    exists_mock = mocker.patch("workspace.core.exists")
    mkdir_mock = mocker.patch("workspace.core.mkdir")
    exists_mock.return_value = False

    workspace.add_child(WorkSpace(name="python"))
    workspace.add_child(WorkSpace(name="js"))
    workspace.add_child(WorkSpace(name="ruby"))

    workspace.build()

    assert workspace.was_created
    assert mkdir_mock.call_count == 4


def test_si_existe_no_podra_crearse(workspace, mocker):
    exists_mock = mocker.patch('workspace.core.exists')
    mkdir_mock = mocker.patch('workspace.core.mkdir')
    exists_mock.return_value = True

    workspace.build()

    assert not workspace.was_created
    mkdir_mock.assert_not_called()


def test_el_path_de_un_workspace_sera_la_concatenacion_de_su_nombre(mocker):
    env = mocker.patch("os.getcwd")
    env.return_value = "/user"
    workspace = WorkSpace(name="development")
    python = WorkSpace(name="python")
    workspace.add_child(python)

    assert workspace.path == "/user/development"
    assert python.path == "/user/development/python"

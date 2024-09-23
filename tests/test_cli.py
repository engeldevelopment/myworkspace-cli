from click.testing import CliRunner

from myworkspace.scripts.cli import workspace

import pytest


@pytest.fixture
def runner():
    return CliRunner()


def test_se_puede_crear_el_workspace(runner, mocker):
    
    reposiotry_mock = mocker.patch("myworkspace.services.WorkspaceRepository")
    reposiotry_mock.path = "tests"
    
    with runner.isolated_filesystem():
        result = runner.invoke(workspace, ["build"])

    assert "Se creó exitosamente!" in result.output


def test_se_puede_crear_el_workspace_dado_un_nombre(runner, mocker):
    reposiotry_mock = mocker.patch("myworkspace.services.WorkspaceRepository")
    reposiotry_mock.path = "tests"

    with runner.isolated_filesystem():
        result = runner.invoke(workspace, ["build", "--name", "development"])

    assert "Se creó exitosamente!" in result.output

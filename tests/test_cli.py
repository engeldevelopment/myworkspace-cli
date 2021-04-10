from click.testing import CliRunner

import pytest

from workspace.scripts.cli import workspace


@pytest.fixture
def runner():
    return CliRunner()


def test_se_puede_crear_el_workspace(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(workspace, ["build"])

    assert "Se creó exitosamente!" in result.output


def test_se_puede_crear_el_workspace_dado_un_nombre(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(workspace, ["build", "--name", "development"])

    assert "Se creó exitosamente!" in result.output

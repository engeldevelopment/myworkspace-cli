from unittest import TestCase

from click.testing import CliRunner

from workspace.scripts.cli import workspace


class TestCliWorkSpace(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_se_puede_crear_el_workspace(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(workspace, ["build"])

        self.assertIn("Se creó exitosamente!", result.output)

    def test_se_puede_crear_el_workspace_dado_un_nombre(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(workspace, ["build", "--name", "development"])

        self.assertIn("Se creó exitosamente!", result.output)

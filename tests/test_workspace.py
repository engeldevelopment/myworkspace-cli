import os
from unittest import TestCase
from unittest.mock import patch

from workspace.core import WorkSpace


class TestWorkSpace(TestCase):
    def setUp(self):
        self.workspace = WorkSpace(name="dev")

    @patch("workspace.core.os")
    def test_se_puede_crear_el_workspace(self, os_mock):
        os_mock.path.exists.return_value = False
        self.workspace.build()

        self.assertTrue(self.workspace.was_created)
        os_mock.mkdir.assert_called()

    @patch("workspace.core.os")
    def test_si_existe_no_podra_crearse(self, os_mock):
        os_mock.path.exists.return_value = True

        self.workspace.build()

        self.assertFalse(self.workspace.was_created)
        os_mock.mkdir.assert_not_called()
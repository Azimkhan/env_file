import unittest
from env_file import setup_env_from_file
import os


class EnvFileTestCase(unittest.TestCase):
    def test_setup_env_with_file(self):
        setup_env_from_file()
        self.assertEqual('settings.prod', os.environ.get('APP_SETTINGS_MODULE'))
        self.assertEqual('localhost', os.environ.get('DB_HOST'))
        self.assertEqual('', os.environ.get('SPECIAL_MODE'))

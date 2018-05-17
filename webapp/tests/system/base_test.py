from unittest import TestCase
from webapp import app


class BaseTest(TestCase):
    def setUp(self):
        self.app.testing = True
        self.app = app.app.test_client()
from django.test import TestCase
from contact import views


class TestViews(TestCase):
    def setUp(self):
        pass

    def test_ContactListView(self):
        self.assertEqual(1 + 1, 2)
        self.assertEqual()
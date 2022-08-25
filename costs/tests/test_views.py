from django.test import TestCase
from django.urls import reverse

COST_LIST_URL = reverse("costs:cost_list")


class PublicListViewsTest(TestCase):
    def test_cost_login_required(self):
        response = self.client.get(COST_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

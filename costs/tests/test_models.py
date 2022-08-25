import unittest
from django.urls import reverse
from costs.models import Cost


class ModelsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.username = "TestUser"
        self.first_name = "Test_firstname"
        self.last_name = "Test_last_name"
        self.password = "test1234"

        self.cost = Cost.objects.create(
            data="2012-01-12",
            category="Odeja",
            price=255.5
        )

    def test_manufacturer_string(self):
        self.assertEqual(str(self.cost), "2012-01-12 Odeja 255.5")


COST_LIST_URL = reverse("costs:cost_list")


class PublicListViewsTest(unittest.TestCase):
    def test_cost_login_required(self):
        response = self.client.get(COST_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

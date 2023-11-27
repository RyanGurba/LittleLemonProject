from django.test import TestCase
from rest_framework import status

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

# class MenuItemTest(TestCase):
#     def test_get_item(self):
#         item = MenuItem.objects.create(title="IceCreame", price=80, inventory=100)
#         itemstr = item.get_item()
#         self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):
    def setup(self):

        item2 = MenuItem.objects.create(title='lobster', price=12.99, inventory=200)
        item3 = MenuItem.objects.create(title='Chicken', price=1.99, inventory=5)

    def test_getall(self):
        url = '/restaurant/menu/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = MenuItemSerializer(MenuItem.objects.all(),many=True).data
        self.assertEqual(response.data, serialized_data)
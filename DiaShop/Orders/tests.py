from django.test import TestCase
from .models import Order
from django.contrib.auth.models import User

class OrderTestCase(TestCase):
    def setUp(self):
        """Tạo dữ liệu mẫu trước khi chạy test"""
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.order = Order.objects.create(Customer=self.user, TotalPrice=1000)

    def test_order_creation(self):
        """Kiểm tra xem Order có được tạo đúng không"""
        self.assertEqual(self.order.Customer.username, "testuser")
        self.assertEqual(self.order.TotalPrice, 1000)
# Create your tests here.

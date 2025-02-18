from django.test import TestCase, Client
from django.contrib.auth.models import User
from Products.models import Product
from Cart.models import Order, OrderItem, ShoppingAddress
from django.urls import reverse

class CartTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.product = Product.objects.create(name="Diamond Ring", price=5000.00, stock=10)
        self.order = Order.objects.create(customer=self.user, complete=False)

    def test_cart_view(self):
        """Kiểm tra trang giỏ hàng"""
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_checkout_view(self):
        """Kiểm tra trang thanh toán"""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        """Kiểm tra thêm sản phẩm vào giỏ hàng"""
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse('add_to_cart'), {"product_id": self.product.id, "quantity": 2})
        self.assertEqual(response.status_code, 200)

    def test_add_order_item(self):
        """Kiểm tra thêm sản phẩm vào giỏ hàng"""
        order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.get_total, 10000.00)

    def test_get_cart_items(self):
        """Kiểm tra tổng số lượng sản phẩm trong giỏ hàng"""
        OrderItem.objects.create(order=self.order, product=self.product, quantity=2)
        self.assertEqual(self.order.get_cart_items, 2)

    def test_get_cart_total(self):
        """Kiểm tra tổng giá trị đơn hàng"""
        OrderItem.objects.create(order=self.order, product=self.product, quantity=2)
        self.assertEqual(self.order.get_cart_total, 10000.00)

    def test_create_shopping_address(self):
        """Kiểm tra tạo địa chỉ giao hàng"""
        address = ShoppingAddress.objects.create(
            customer=self.user,
            order=self.order,
            address="123 Diamond Street",
            phone_number="0123456789",
            note="Giao hàng vào buổi sáng"
        )
        self.assertEqual(address.address, "123 Diamond Street")
        self.assertEqual(address.phone_number, "0123456789")

from django.test import TestCase
from django.contrib import admin

from .admin import CustomerAdmin
from .models import Customer


class CustomerTest(TestCase):
    def test_customer_model_should_have_email_field(self):
        expected = 'wow@doge.wow'
        customer = Customer.objects.create(email='wow@doge.wow')
        self.assertEqual(customer.email, expected)


class CustomerAdminTest(TestCase):
    def test_customer_should_be_registed_to_admin(self):
        self.assertIsInstance(
            admin.site._registry[Customer],
            CustomerAdmin
        )
    def test_customer_admin_should_set_list_display(self):
        expected = (
            'email',
        )
        self.assertEqual(CustomerAdmin.list_display, expected)

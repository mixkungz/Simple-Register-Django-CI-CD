from django.test import TestCase

from ..models import Customer


class CustomerTest(TestCase):
    def test_customer_model_should_have_email_field(self):
        expected = 'wow@doge.wow'
        customer = Customer.objects.create(email='wow@doge.wow')
        self.assertEqual(customer.email, expected)

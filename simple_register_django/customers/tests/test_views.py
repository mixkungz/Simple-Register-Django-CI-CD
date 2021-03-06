from django.test import TestCase

from ..models import Customer


class LandingPageViewTest(TestCase):
    def test_view_should_have_form_with_email_field_and_submit_button(self):
        response = self.client.get('/')
        
        expected = '<h1>Doge wow wow Doge</h1>'
        self.assertContains(response, expected, status_code=200)
        expected = '<form action="." method="post">'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type="hidden" name="csrfmiddlewaretoken"'
        self.assertContains(response, expected, status_code=200)
        expected = '<input type="email" name="email">'
        self.assertContains(response, expected, status_code=200)
        expected = '<button type="submit">Submit</button>'
        self.assertContains(response, expected, status_code=200)
        expected = '</form>'
        self.assertContains(response, expected, status_code=200)

    def test_view_should_save_customer_when_submit_form(self):
        email = 'wow@doge.wow'
        data={
            'email': email
        }

        response = self.client.post('/', data=data)
        self.assertEqual(response.status_code, 200)

        count = Customer.objects.filter(email=email).count()
        self.assertEqual(count, 1)

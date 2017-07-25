from django.test import TestCase
from django.test.client import Client

import dot_and_circle.views as view
from rest_framework import status

client = Client()


class DotAndCircleTestCase(TestCase):

    # distance = 14.142.. radius = 15
    def test_if_dot_is_inside_the_circle(self):
        self.assertTrue(view.is_the_dot_inside_the_circle(100, 100, 110, 110, 15))

    # distance = 25 radius = 25
    def test_if_dot_is_on_the_circle(self):
        self.assertFalse(view.is_the_dot_inside_the_circle(100, 150, 125, 150, 25))

    # distance = 25 radius = 20
    def test_if_dot_is_outside_the_circle(self):
        self.assertFalse(view.is_the_dot_inside_the_circle(100, 150, 125, 150, 20))

    def test_request_with_proper_parameters(self):
        path = '/dot_and_circle/check/'
        params = '?xCircle=100&yCircle=150&xPoint=125&yPoint=150&radius=20'
        response = client.get(path + params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_with_improper_parameters(self):
        path = '/dot_and_circle/check/'
        params = '?xCircle=100&yCircle=150'
        response = client.get(path + params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

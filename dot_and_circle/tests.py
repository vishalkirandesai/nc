from django.test import TestCase
import dot_and_circle.views as view

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


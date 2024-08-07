from django.test import TestCase
from ablog.forms import PostForm

# Create your tests here.

class TestaBlogPostForm(TestCase):
    """ Unit Test for blog post form"""

    def test_title_is_required(self):
        form = PostForm(({'title': ''}))
        self.assertFalse(form.is_valid())

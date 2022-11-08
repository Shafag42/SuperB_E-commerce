from django.test import TestCase


from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import blog

# Create your tests here.
class TestModels(TestCase):
    def create_object(self):
        
        user1= User.objects.create(useraname='shefeq', password='abcde')
        self.data1={
            "author": self.user1,
            "title" : "hsghdfh",
            "description" : "hsdfgj",
            "blog_short" :"hdgkj",
            "img": "blog1",
            "user_img" : "blog_2",
            "read_count" : "2",
        }
        blog1=blog.objects.create(**self.data1)

    def test_title(self):
        self.create_object()
        self.assertEqual(self.data1['title'],self.blog1.title)
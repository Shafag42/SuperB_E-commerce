from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
#from django.utils.encoding import python_2_unicode_compatible
from django.utils.six import python_2_unicode_compatible
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    blog_short=models.TextField()
    created_at=models.DateField(auto_now_add=True)  
    img = models.ImageField(upload_to = "images/")
    user_img=models.ImageField(upload_to="user_images/")
    #read_count=models.PositiveIntegerField(default=0)
    category_blog=models.ForeignKey(Category, on_delete=models.CASCADE)
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogpost_connected=self).count()



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100, blank=False)
    comment_field = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    blogpost_connected = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comments')
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True)

    class Meta:
        ordering = ['date_created']
        
    def __str__(self):
        return self.name

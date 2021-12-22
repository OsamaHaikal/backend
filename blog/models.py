from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import URLField
from django_quill.fields import QuillField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')

    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = QuillField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
     
        permissions = [
            ("change_post_status", "Can change the status of posts"),
            ("close_post", "Can remove a post by setting its status as closed"),
        ]

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_comments')

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    body = QuillField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Referece(models.Model):
    posts = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='references')
    text = models.CharField(max_length=250)
    links = models.URLField()
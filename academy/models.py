from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string

# Create your models here.
from ckeditor.fields import RichTextField 

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    slug = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    program = models.ForeignKey('Program',on_delete=models.PROTECT,null=True,blank=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    slug = models.CharField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    video = models.FileField()


    def __str__(self):
        return self.title

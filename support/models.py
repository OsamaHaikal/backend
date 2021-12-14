from django.db import models
from django_quill.fields import QuillField

# Create your models here.



class Tag(models.Model):
    title = models.CharField(max_length=120,unique=True)
    slug = models.SlugField(max_length=120,unique=True)

class Faq(models.Model):
    cats = models.ManyToManyField(Tag)
    qeustion = models.CharField(max_length=350)
    answer = QuillField()

    def __str__(self):
        return self.qeustion

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=350)
    subject = models.CharField(max_length=250)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " "+ self.subject

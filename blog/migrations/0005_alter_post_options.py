# Generated by Django 4.0 on 2021-12-20 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_referece'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on'], 'permissions': [('change_post_status', 'Can change the status of posts'), ('close_post', 'Can remove a post by setting its status as closed')]},
        ),
    ]
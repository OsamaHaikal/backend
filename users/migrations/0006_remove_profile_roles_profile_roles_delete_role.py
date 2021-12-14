# Generated by Django 4.0 on 2021-12-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roles',
        ),
        migrations.AddField(
            model_name='profile',
            name='roles',
            field=models.CharField(choices=[(1, 'user'), (2, 'teacher'), (3, 'bloger'), (4, 'employee'), (5, 'admin')], default='USER', max_length=120),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
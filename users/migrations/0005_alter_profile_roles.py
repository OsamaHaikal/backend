# Generated by Django 4.0 on 2021-12-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roles',
            field=models.ManyToManyField(default='USER', to='users.Role'),
        ),
    ]

# Generated by Django 4.0 on 2021-12-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='faq',
            name='cats',
            field=models.ManyToManyField(to='support.Category'),
        ),
    ]

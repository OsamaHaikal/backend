# Generated by Django 4.0 on 2021-12-14 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('links', models.URLField()),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='blog.post')),
            ],
        ),
    ]

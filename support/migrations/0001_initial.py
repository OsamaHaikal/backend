# Generated by Django 4.0 on 2021-12-14 14:16

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qeustion', models.CharField(max_length=350)),
                ('answer', django_quill.fields.QuillField()),
            ],
        ),
    ]

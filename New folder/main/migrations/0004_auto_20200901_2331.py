# Generated by Django 3.1 on 2020-09-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_author_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

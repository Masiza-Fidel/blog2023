# Generated by Django 5.0 on 2023-12-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_blog_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='full_content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

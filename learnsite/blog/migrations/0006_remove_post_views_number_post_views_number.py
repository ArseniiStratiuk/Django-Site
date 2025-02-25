# Generated by Django 4.1.5 on 2023-01-23 16:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_post_views_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="views_number",
        ),
        migrations.AddField(
            model_name="post",
            name="views_number",
            field=models.ManyToManyField(
                related_name="views_rating", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]

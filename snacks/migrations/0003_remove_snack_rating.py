# Generated by Django 4.2 on 2023-04-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("snacks", "0002_snack_delete_movie"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="snack",
            name="rating",
        ),
    ]

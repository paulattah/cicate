# Generated by Django 4.2.5 on 2023-10-29 15:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="Username",
            new_name="username",
        ),
    ]
# Generated by Django 4.2.2 on 2023-10-05 16:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("archive_auth", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="archiveuser",
            name="name",
        ),
    ]

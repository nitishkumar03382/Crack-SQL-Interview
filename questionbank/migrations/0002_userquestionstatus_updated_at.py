# Generated by Django 4.2.17 on 2024-12-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questionbank", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userquestionstatus",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
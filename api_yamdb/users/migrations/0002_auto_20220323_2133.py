# Generated by Django 2.2.16 on 2022-03-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "admin"),
                    ("moderator", "moderator"),
                    ("user", "user"),
                ],
                default="user",
                max_length=50,
            ),
        ),
    ]

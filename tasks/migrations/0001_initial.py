# Generated by Django 4.2.3 on 2023-08-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(null=True)),
                ("due_date", models.DateField(null=True, verbose_name="due date")),
                ("completed", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]

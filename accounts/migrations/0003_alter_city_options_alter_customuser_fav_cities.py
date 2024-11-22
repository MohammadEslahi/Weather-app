# Generated by Django 5.1.3 on 2024-11-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_city_alter_customuser_age_customuser_fav_cities"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"verbose_name_plural": "cities"},
        ),
        migrations.AlterField(
            model_name="customuser",
            name="fav_cities",
            field=models.ManyToManyField(
                blank=True, related_name="users", to="accounts.city"
            ),
        ),
    ]

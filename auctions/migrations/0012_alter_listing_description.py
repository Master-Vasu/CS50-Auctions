# Generated by Django 5.0.6 on 2024-06-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0011_bid_bid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="description",
            field=models.CharField(max_length=500),
        ),
    ]

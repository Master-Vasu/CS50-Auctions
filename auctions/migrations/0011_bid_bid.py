# Generated by Django 5.0.6 on 2024-06-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_remove_bid_bid"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="bid",
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.1.14 on 2022-01-24 17:11

import pytz
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0019_change_config_datetime_rules"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="default_timezone",
            field=models.TextField(
                choices=[(x, x) for x in pytz.all_timezones],
                default="UTC",
            ),
        ),
    ]

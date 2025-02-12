# Generated by Django 4.2rc1 on 2023-04-07 19:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0043_alter_photo_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cluster",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clusters",
                to="api.person",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="cluster_owner",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Info", "0005_famoussentencestasks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routinetasks",
            name="mode",
            field=models.IntegerField(),
        ),
    ]

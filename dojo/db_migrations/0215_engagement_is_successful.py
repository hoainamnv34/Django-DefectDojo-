# Generated by Django 4.1.13 on 2024-05-26 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0214_alter_engagement_evaluate_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='is_successful',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.1.13 on 2024-05-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0213_engagement_evaluate_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement_evaluate',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

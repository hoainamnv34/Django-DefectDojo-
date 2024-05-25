# Generated by Django 2.2.16 on 2020-11-08 08:01

from django.db import migrations
import logging

logger = logging.getLogger(__name__)


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0064_jira_refactor_populate'),
    ]

    def delete_empty_jira_project_configs(apps, schema_editor):
        logger.info('removing JIRA_Projects with empty instance and empty project key created due to bugs in 1.10.0')
        logger.info('details in https://github.com/DefectDojo/django-DefectDojo/issues/3354')
        # querying on null or blank or whatever can get the wrong results, so just iterate over all configs to be reliable
        JIRA_Project = apps.get_model('dojo', 'JIRA_Project')
        for jira_project in JIRA_Project.objects.all():
            if not jira_project.jira_instance and not jira_project.project_key:
                product = jira_project.product
                product_id = product.id if product else 0
                engagement = jira_project.engagement
                engagement_id = engagement.id if engagement else 0

                logger.info('removing empty JIRA_Project %i for product %i:%s engagement %i:%s', jira_project.id, product_id, product, engagement_id, engagement)
                jira_project.delete()

    operations = [
        migrations.RunPython(delete_empty_jira_project_configs, migrations.RunPython.noop),
    ]

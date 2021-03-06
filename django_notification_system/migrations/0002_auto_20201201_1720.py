# Generated by Django 3.1.3 on 2020-12-03 21:28

from django.db import migrations


def create_initial_targets(apps, schema_editor):
    """
    Initialize the database with the Targets that we have functions available for.
    """
    NotificationTarget = apps.get_model('django_notification_system', 'NotificationTarget')
    NotificationTarget.objects.get_or_create(
        name="Twilio",
        notification_module_name="twilio")
    NotificationTarget.objects.get_or_create(
        name="Email",
        notification_module_name="email")
    NotificationTarget.objects.get_or_create(
        name="Expo",
        notification_module_name="expo")


class Migration(migrations.Migration):

    dependencies = [
        ('django_notification_system', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_targets),
    ]

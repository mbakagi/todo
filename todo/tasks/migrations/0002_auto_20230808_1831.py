# Generated by Django 3.0 on 2023-08-08 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complet',
            new_name='complete',
        ),
    ]

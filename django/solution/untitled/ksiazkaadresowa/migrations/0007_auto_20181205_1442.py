# Generated by Django 2.1.1 on 2018-12-05 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ksiazkaadresowa', '0006_person_firends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='firends',
            new_name='friends',
        ),
    ]

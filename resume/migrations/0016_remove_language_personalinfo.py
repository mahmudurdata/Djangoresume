# Generated by Django 2.0.2 on 2018-02-27 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_remove_education_degree'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='personalinfo',
        ),
    ]

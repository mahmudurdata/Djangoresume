# Generated by Django 2.0.2 on 2018-03-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20180304_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programminglanguage',
            name='level',
            field=models.IntegerField(choices=[(5, 'Expert'), (4, 'Advanced'), (3, 'Intermediate'), (2, 'Novice'), (1, 'Fundamental Awareness')], help_text='Choice between 1 and 5'),
        ),
    ]

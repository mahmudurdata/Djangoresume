# Generated by Django 2.0.3 on 2018-03-31 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0037_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='resume/img/'),
        ),
    ]

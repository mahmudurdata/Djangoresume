# Generated by Django 2.0.3 on 2018-03-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0036_delete_ongoingproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile_hovercolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='day',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='month',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-30 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_profile_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='habit',
            field=models.CharField(max_length=150),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='color',
        ),
    ]
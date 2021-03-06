# Generated by Django 4.0.4 on 2022-06-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_record_weekcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='week',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='weekcolor',
            field=models.JSONField(verbose_name={'Friday': '#808080', 'Monday': '#808080', 'Saturday': '#808080', 'Sunday': '#808080', 'Thursday': '#808080', 'Tuesday': '#808080', 'Wednesday': '#808080'}),
        ),
    ]

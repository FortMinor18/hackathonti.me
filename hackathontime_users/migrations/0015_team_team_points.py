# Generated by Django 2.2.7 on 2019-12-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0014_auto_20191205_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_points',
            field=models.FloatField(default=0.0),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-10 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0016_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

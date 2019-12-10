# Generated by Django 2.2.7 on 2019-12-10 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathontime_users', '0017_team_team_slug'),
        ('hackathontime_main', '0013_auto_20191210_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='hackathon_won',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='hackathontime_users.Team'),
        ),
    ]
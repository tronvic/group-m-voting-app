# Generated by Django 5.0.2 on 2024-02-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='vote',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

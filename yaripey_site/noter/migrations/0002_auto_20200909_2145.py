# Generated by Django 3.1.1 on 2020-09-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notebook',
            name='desc',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]

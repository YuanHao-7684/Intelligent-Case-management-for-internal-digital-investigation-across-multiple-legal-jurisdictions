# Generated by Django 3.2.5 on 2022-07-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_setupcases'),
    ]

    operations = [
        migrations.AddField(
            model_name='setupcases',
            name='caseUserId',
            field=models.CharField(default=123, max_length=32),
            preserve_default=False,
        ),
    ]

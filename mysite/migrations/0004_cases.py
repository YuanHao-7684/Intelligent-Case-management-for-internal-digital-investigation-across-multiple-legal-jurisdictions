# Generated by Django 3.2.5 on 2022-07-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20220714_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('caseId', models.BigAutoField(primary_key=True, serialize=False)),
                ('caseUser', models.CharField(max_length=32)),
                ('caseContent', models.CharField(max_length=1024)),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-07 10:59

import apps.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
    ]

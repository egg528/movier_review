# Generated by Django 2.2.5 on 2021-02-03 08:11

from django.db import migrations
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210203_1236'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.CustomModelManager()),
            ],
        ),
    ]
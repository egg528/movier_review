# Generated by Django 2.2.5 on 2021-02-03 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='movies.Movie'),
        ),
    ]
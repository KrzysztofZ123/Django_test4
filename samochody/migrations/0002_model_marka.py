# Generated by Django 4.1.7 on 2023-03-26 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='marka',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='samochody.marka'),
            preserve_default=False,
        ),
    ]

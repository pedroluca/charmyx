# Generated by Django 5.0.4 on 2024-09-02 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proprietario', '0001_initial'),
        ('salao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salao',
            name='proprietario_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proprietario.proprietario'),
            preserve_default=False,
        ),
    ]

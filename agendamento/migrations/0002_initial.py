# Generated by Django 5.0.4 on 2024-09-02 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamento', '0001_initial'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='servico_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servico.servico'),
        ),
    ]

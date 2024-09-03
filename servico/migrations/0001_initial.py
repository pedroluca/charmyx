# Generated by Django 5.0.4 on 2024-09-02 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salao', '0002_salao_proprietario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracao', models.DurationField()),
                ('salao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salao.salao')),
            ],
        ),
    ]

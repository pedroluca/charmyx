# Generated by Django 5.0.4 on 2024-09-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='salao_id',
            new_name='salao',
        ),
    ]

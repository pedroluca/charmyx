# Generated by Django 5.0.4 on 2024-09-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='url_image',
            field=models.ImageField(blank=True, default='produto/default-product.jpg', null=True, upload_to='produto/'),
        ),
    ]

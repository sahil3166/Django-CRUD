# Generated by Django 5.0.4 on 2024-05-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0013_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]

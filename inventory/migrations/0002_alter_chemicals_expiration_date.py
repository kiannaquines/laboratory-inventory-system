# Generated by Django 5.0.7 on 2024-08-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicals',
            name='expiration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

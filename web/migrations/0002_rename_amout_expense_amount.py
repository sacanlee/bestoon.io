# Generated by Django 4.2.2 on 2023-07-01 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='amout',
            new_name='amount',
        ),
    ]

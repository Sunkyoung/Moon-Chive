# Generated by Django 2.1.5 on 2019-11-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 2.1.5 on 2019-10-05 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20191005_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='pr_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]

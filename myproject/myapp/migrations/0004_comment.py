# Generated by Django 2.1.5 on 2019-10-03 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191004_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_author', models.CharField(default='익명', max_length=200)),
                ('c_content', models.TextField()),
                ('c_date', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.Board')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-08 17:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empcode', models.IntegerField()),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('is_active', models.IntegerField(null=True)),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]

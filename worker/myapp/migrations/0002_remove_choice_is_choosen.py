# Generated by Django 2.2.1 on 2019-05-31 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='is_choosen',
        ),
    ]

# Generated by Django 2.2.6 on 2020-06-07 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='is_answer',
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-15 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answers_count',
            new_name='answers_number',
        ),
    ]

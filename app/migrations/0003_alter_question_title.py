# Generated by Django 4.1.3 on 2022-12-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_answers_count_question_answers_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]

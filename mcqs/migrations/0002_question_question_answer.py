# Generated by Django 3.1.4 on 2020-12-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_answer',
            field=models.IntegerField(default=-1),
        ),
    ]

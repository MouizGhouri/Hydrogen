# Generated by Django 3.1.4 on 2020-12-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0002_question_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_approved',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpwild', '0003_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Quizz',
        ),
        migrations.AddField(
            model_name='donate',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='donate',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

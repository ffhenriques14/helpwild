# Generated by Django 4.0.5 on 2022-07-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpwild', '0016_rename_nomesddad_quiz_nomes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='nomes',
            new_name='nome',
        ),
    ]

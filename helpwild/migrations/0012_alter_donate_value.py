# Generated by Django 4.0.5 on 2022-07-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpwild', '0011_alter_donate_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='value',
            field=models.IntegerField(default='0'),
        ),
    ]

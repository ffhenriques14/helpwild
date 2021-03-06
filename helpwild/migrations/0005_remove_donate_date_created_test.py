# Generated by Django 4.0.5 on 2022-07-05 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpwild', '0004_rename_quiz_quizz_donate_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='date_created',
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano_realizado', models.IntegerField(default=0)),
                ('ects', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=0)),
                ('donation', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='helpwild.Donate.projeto+', to='helpwild.donate')),
            ],
        ),
    ]

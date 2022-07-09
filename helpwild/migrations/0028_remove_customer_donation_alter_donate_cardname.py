# Generated by Django 4.0.5 on 2022-07-08 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpwild', '0027_remove_donate_customer_customer_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='donation',
        ),
        migrations.AlterField(
            model_name='donate',
            name='cardname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helpwild.customer'),
        ),
    ]
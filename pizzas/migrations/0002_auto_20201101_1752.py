# Generated by Django 3.1.2 on 2020-11-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='name',
            field=models.CharField(blank=True, choices=[('hawajska', 'hawajska'), ('miesna', 'miesna')], max_length=10),
        ),
        migrations.AddField(
            model_name='topping',
            name='toppings',
            field=models.CharField(blank=True, choices=[('ananas', 'ananas'), ('bekon', 'bekon'), ('sos', 'sos')], max_length=10),
        ),
    ]
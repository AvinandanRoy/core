# Generated by Django 5.0.4 on 2024-09-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_car_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikeName', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-21 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210321_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='order_id',
            field=models.CharField(blank=True, editable=False, max_length=120, unique=True),
        ),
    ]

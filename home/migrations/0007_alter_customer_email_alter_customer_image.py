# Generated by Django 4.0.1 on 2022-02-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order_expectedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=101, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/profile'),
        ),
    ]
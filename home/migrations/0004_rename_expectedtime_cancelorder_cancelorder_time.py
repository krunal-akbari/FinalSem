# Generated by Django 4.0.1 on 2022-02-22 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_cancelorder_complate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancelorder',
            old_name='expectedtime',
            new_name='cancelorder_time',
        ),
    ]
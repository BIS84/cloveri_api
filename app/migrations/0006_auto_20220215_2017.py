# Generated by Django 2.2.6 on 2022-02-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220215_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='children',
            field=models.CharField(blank=True, default=0, max_length=255),
        ),
    ]
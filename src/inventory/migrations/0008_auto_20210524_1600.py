# Generated by Django 3.1.7 on 2021-05-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20210524_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='address1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='address2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
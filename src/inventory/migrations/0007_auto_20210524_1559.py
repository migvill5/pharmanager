# Generated by Django 3.1.7 on 2021-05-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20210524_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='movil',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='ruc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
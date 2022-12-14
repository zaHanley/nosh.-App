# Generated by Django 4.1.3 on 2022-12-09 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nosh_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='quantity',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]

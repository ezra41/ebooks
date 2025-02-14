# Generated by Django 4.1.7 on 2023-05-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_shopping_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopping',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='price',
            field=models.FloatField(),
        ),
    ]

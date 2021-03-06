# Generated by Django 3.1.3 on 2020-11-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='product name')),
                ('url', models.CharField(max_length=255, verbose_name='openfoodfacts url')),
                ('nutriscore', models.CharField(max_length=1, verbose_name='product nutriscore')),
                ('description', models.TextField(verbose_name='product description')),
                ('image_url', models.CharField(max_length=255, verbose_name='product image url')),
                ('image_nutrition_url', models.CharField(max_length=255, verbose_name='product nutrition image url')),
                ('categories', models.ManyToManyField(related_name='products', to='categories.Category')),
            ],
            options={
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
        ),
    ]

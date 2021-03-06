# Generated by Django 3.1.6 on 2021-02-12 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='product name')),
                ('description', models.CharField(max_length=4096, verbose_name='product description')),
                ('photo', models.ImageField(upload_to='', verbose_name='photo')),
                ('price', models.PositiveIntegerField(verbose_name='product price')),
                ('stock_amount', models.PositiveIntegerField(verbose_name='amount in stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
            options={
                'ordering': ['name', 'price', 'stock_amount'],
            },
        ),
    ]

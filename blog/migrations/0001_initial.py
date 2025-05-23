# Generated by Django 5.1 on 2025-05-13 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=255)),
                ('price', models.BigIntegerField()),
                ('services_of_categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('ordered_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='blog.service')),
            ],
        ),
    ]

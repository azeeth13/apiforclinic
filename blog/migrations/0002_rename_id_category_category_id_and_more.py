# Generated by Django 5.1 on 2025-05-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='services_of_categ',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='category',
            name='print_api',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='printer_name',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=11, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='DeletedOrders',
            fields=[
                ('deleted_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField()),
                ('services', models.ManyToManyField(to='blog.service')),
            ],
        ),
    ]

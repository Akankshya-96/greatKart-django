# Generated by Django 3.2 on 2021-04-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('New', 'New'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]

# Generated by Django 3.2.9 on 2022-06-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('pass1', models.CharField(max_length=30)),
                ('pass2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('pass1', models.CharField(max_length=30)),
                ('pass2', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='reservationb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('cname', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=15)),
                ('cemail', models.CharField(max_length=50)),
                ('cphone', models.CharField(max_length=10)),
                ('ctime', models.CharField(max_length=10)),
                ('cperson', models.CharField(max_length=3)),
                ('aphone', models.CharField(default='', max_length=12)),
                ('room', models.CharField(default='1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='user_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('qty', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=12)),
                ('qty', models.CharField(max_length=30)),
                ('payment', models.CharField(default='', max_length=20)),
                ('status', models.CharField(default='Processing...', max_length=20)),
            ],
        ),
    ]

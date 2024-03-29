# Generated by Django 4.2.2 on 2023-06-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_form_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('descrion', models.CharField(max_length=250)),
                ('member', models.BooleanField()),
            ],
        ),
    ]

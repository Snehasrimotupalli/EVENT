# Generated by Django 4.2.2 on 2023-06-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_logform_rename_form_regform_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
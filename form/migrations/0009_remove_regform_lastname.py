# Generated by Django 4.2.2 on 2023-06-28 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_alter_regform_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regform',
            name='lastname',
        ),
    ]

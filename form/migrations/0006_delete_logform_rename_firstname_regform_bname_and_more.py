# Generated by Django 4.2.2 on 2023-06-28 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_orders_delete_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logForm',
        ),
        migrations.RenameField(
            model_name='regform',
            old_name='firstname',
            new_name='bname',
        ),
        migrations.RenameField(
            model_name='regform',
            old_name='lastname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='regform',
            old_name='password',
            new_name='lname',
        ),
    ]

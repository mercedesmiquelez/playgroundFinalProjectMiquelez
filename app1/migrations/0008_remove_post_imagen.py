# Generated by Django 4.2.4 on 2023-09-05 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_vendedor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
    ]

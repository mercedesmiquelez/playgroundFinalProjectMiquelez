# Generated by Django 4.2.3 on 2023-08-31 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='email',
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_post_subtitle_servicio_subtitle_servicio_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='servicios'),
        ),
    ]

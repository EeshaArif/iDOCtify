# Generated by Django 2.2.5 on 2019-12-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20191208_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

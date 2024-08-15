# Generated by Django 3.1.5 on 2021-11-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spectools', '0029_datatype_description_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='description_format',
            field=models.SmallIntegerField(choices=[(1, 'Plain text'), (2, 'Raw HTML')], default=1),
        ),
    ]
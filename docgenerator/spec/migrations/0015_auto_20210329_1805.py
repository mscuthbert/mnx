# Generated by Django 3.1.5 on 2021-03-29 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0014_auto_20210329_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='xmlrelationship',
            name='child_order',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='xmlelement',
            name='children_type',
            field=models.SmallIntegerField(choices=[(1, 'Unordered'), (2, 'Sequence'), (3, 'Choice')], default=1, help_text='This specifies the requirement for child elements.'),
        ),
    ]

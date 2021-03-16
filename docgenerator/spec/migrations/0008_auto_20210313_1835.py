# Generated by Django 3.1.5 on 2021-03-13 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0007_auto_20210302_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatype',
            name='base_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spec.datatype'),
        ),
        migrations.AddField(
            model_name='datatype',
            name='union_types',
            field=models.ManyToManyField(blank=True, help_text='If this data type is a union of multiple other types, list them here.', related_name='_datatype_union_types_+', to='spec.DataType'),
        ),
        migrations.AddField(
            model_name='datatype',
            name='xsd_name',
            field=models.CharField(blank=True, help_text='Use this field if this data type is a native XSD type such as string.', max_length=80, verbose_name='XSD name'),
        ),
        migrations.AlterField(
            model_name='xmlelement',
            name='attribute_groups',
            field=models.ManyToManyField(blank=True, to='spec.XMLAttributeGroup'),
        ),
    ]
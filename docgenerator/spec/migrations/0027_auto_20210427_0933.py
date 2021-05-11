# Generated by Django 3.1.5 on 2021-04-27 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spec', '0026_siteoptions_sidebar_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmlelement',
            name='disambiguation',
            field=models.CharField(blank=True, help_text='This is displayed next to the element name in parentheses in order to disambiguate it. E.g., "timewise" for part elements.', max_length=80),
        ),
        migrations.AlterField(
            model_name='xmlelement',
            name='schema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spec.xmlschema'),
        ),
    ]
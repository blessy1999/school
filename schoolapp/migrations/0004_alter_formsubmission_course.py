# Generated by Django 4.2.6 on 2023-10-18 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_material_formsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsubmission',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.course'),
        ),
    ]

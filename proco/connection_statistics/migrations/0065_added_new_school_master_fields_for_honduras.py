# Generated by Django 2.2.28 on 2024-09-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection_statistics', '0064_added_qos_mongolia_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='computer_availability',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='device_availability',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_robotic_equipment',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_students_boys',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_students_girls',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_students_other',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_tablets',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_teachers_female',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='num_teachers_male',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='sustainable_business_model',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='schoolweeklystatus',
            name='teachers_trained',
            field=models.NullBooleanField(default=None),
        ),
    ]

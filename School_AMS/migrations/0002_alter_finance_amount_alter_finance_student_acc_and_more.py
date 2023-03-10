# Generated by Django 4.1.5 on 2023-01-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_AMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='finance',
            name='student_acc',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_personnel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

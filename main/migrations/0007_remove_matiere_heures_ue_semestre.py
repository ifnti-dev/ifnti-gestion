# Generated by Django 4.1.7 on 2023-06-15 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_semestre_anneescolaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matiere',
            name='heures',
        ),
        migrations.AddField(
            model_name='ue',
            name='semestre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.semestre', verbose_name='Semestre'),
            preserve_default=False,
        ),
    ]

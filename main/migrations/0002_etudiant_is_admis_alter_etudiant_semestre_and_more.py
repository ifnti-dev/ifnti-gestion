# Generated by Django 4.0.1 on 2023-05-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='is_admis',
            field=models.BooleanField(default=False, verbose_name='Admis'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='semestre',
            field=models.ManyToManyField(to='main.Semestre'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='etudiants',
            field=models.ManyToManyField(through='main.Note', to='main.Etudiant', verbose_name='Étudiants'),
        ),
        migrations.AlterField(
            model_name='tuteur',
            name='etudiants',
            field=models.ManyToManyField(blank=True, to='main.Etudiant', verbose_name='Étudiants'),
        ),
    ]

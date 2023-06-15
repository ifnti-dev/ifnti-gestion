# Generated by Django 4.2.2 on 2023-06-15 09:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_etudiant_is_admis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FicheDePaie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.IntegerField(default=40, verbose_name='B.P')),
                ('telephone', models.IntegerField(default=90918141, verbose_name='Téléphone')),
                ('dateDebut', models.DateField(verbose_name='Date de début')),
                ('dateFin', models.DateField(verbose_name='Date de fin')),
                ('matiere', models.CharField(max_length=100, verbose_name='Matière')),
                ('nombreHeure', models.IntegerField(verbose_name="Nombre d'heure")),
                ('prixUnitaire', models.IntegerField(verbose_name='Prix unitaire')),
                ('montant', models.IntegerField(verbose_name='Montant')),
                ('montantAvance', models.IntegerField(verbose_name='Montant avance')),
                ('montantAPayer', models.IntegerField(verbose_name='Montant à payer')),
                ('montantEnLettre', models.CharField(max_length=100, verbose_name='Montant en lettre')),
                ('numero', models.IntegerField(verbose_name='Numéro')),
                ('niveau1', models.CharField(choices=[('semstre1', 'S1'), ('semstre2', 'S2')], max_length=30)),
                ('niveau2', models.CharField(choices=[('semstre3', 'S3'), ('semstre4', 'S4')], max_length=30)),
                ('niveau3', models.CharField(choices=[('semstre5', 'S5'), ('semstre6', 'S6')], max_length=30)),
                ('heureL1', models.IntegerField(verbose_name='Heure L1')),
                ('heureL2', models.IntegerField(verbose_name='Heure L2')),
                ('heureL3', models.IntegerField(verbose_name='Heure L3')),
                ('montantL1', models.IntegerField(verbose_name='Montant L1')),
                ('montantL2', models.IntegerField(verbose_name='Montant L2')),
                ('montantL3', models.IntegerField(verbose_name='Montant L3')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.enseignant', verbose_name='Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomDirecteur', models.CharField(max_length=100, verbose_name='Nom du directeur')),
                ('prenomDirecteur', models.CharField(max_length=100, verbose_name='Prénom du directeur')),
                ('nomEnseignant', models.CharField(max_length=100, verbose_name="Nom de l'enseignant")),
                ('prenomEnseignant', models.CharField(max_length=100, verbose_name="Prénom de l'enseignant")),
                ('numeroSecurite', models.IntegerField(verbose_name='Numéro de sécurité sociale')),
                ('discipline', models.CharField(max_length=100, verbose_name='Discipline')),
                ('niveau', models.CharField(max_length=100, verbose_name='Niveau')),
                ('dateDebut', models.DateField(verbose_name='Date de début')),
                ('dateFin', models.DateField(verbose_name='Date de fin')),
                ('duree', models.CharField(max_length=100, verbose_name='Durée')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('scolarite', 'Frais de scolarité')], max_length=30)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montant versé')),
                ('fraisconcours', models.IntegerField(default=10000, verbose_name='Frais de concours')),
                ('fraisinscription', models.IntegerField(default=30000, verbose_name='Frais de concours')),
                ('dateversement', models.DateField(default=django.utils.timezone.now, verbose_name='Date de versement')),
                ('nombreTranche', models.IntegerField(verbose_name='Nombre de tranche')),
                ('debit', models.IntegerField(default=590000, verbose_name='Débit')),
                ('credit', models.IntegerField(default=0, verbose_name='Crédit')),
                ('numerobordereau', models.CharField(max_length=30, verbose_name='Numéro de bordereau')),
                ('bordereau', models.FileField(null=True, upload_to='bordereau/', verbose_name='Bordereau de paiement')),
                ('comptable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comptable', verbose_name='Comptable')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.etudiant', verbose_name='Etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='anneeuniversitaire',
            name='anneeUnivCourante',
            field=models.BooleanField(default=False, null=True, verbose_name='Année universitaire acutuelle'),
        ),
        migrations.DeleteModel(
            name='Versement',
        ),
    ]

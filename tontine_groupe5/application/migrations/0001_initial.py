# Generated by Django 5.1.1 on 2025-04-15 07:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequence', models.CharField(choices=[('M', 'Mensuelle'), ('T', 'Trimestrielle'), ('A', 'Annuelle')], max_length=1)),
                ('date_debut', models.DateField(default=django.utils.timezone.now)),
                ('est_active', models.BooleanField(default=True)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=12)),
                ('type_don', models.CharField(choices=[('ESP', 'Espèces'), ('MTN', 'Mobile Money'), ('BNQ', 'Virement Bancaire')], max_length=3)),
                ('date_don', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
                ('anonyme', models.BooleanField(default=False)),
                ('donateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=12)),
                ('motif', models.TextField()),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
                ('date_approbation', models.DateTimeField(blank=True, null=True)),
                ('statut', models.CharField(choices=[('DEM', 'Demande en cours'), ('ACC', 'Accepté'), ('REF', 'Refusé'), ('REM', 'Remboursé')], default='DEM', max_length=3)),
                ('emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prets', to=settings.AUTH_USER_MODEL)),
                ('garant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prets_garantis', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Remboursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_demande', models.DateField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('P', 'En attente'), ('A', 'Approuvé'), ('R', 'Rejeté')], default='P', max_length=1)),
                ('cotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.cotisation')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

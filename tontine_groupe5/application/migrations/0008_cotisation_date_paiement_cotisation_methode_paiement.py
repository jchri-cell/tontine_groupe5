# Generated by Django 5.1.1 on 2025-04-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_remove_don_nature_don_don_nature'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotisation',
            name='date_paiement',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cotisation',
            name='methode_paiement',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

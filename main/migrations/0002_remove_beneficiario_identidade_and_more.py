# Generated by Django 5.0.3 on 2024-03-20 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiario',
            name='identidade',
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='comprovante_de_residencia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='cpf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='nome_mae',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='nome_pai',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='numero_carteira_trabalho',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='pis',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='quantidade_filhos',
            field=models.IntegerField(),
        ),
    ]
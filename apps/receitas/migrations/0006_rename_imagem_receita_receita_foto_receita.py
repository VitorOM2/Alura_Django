# Generated by Django 3.2.15 on 2022-09-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_receita_imagem_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='imagem_receita',
            new_name='foto_receita',
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='foto/%d/%m/%y/'),
        ),
    ]

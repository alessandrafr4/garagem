# Generated by Django 4.1.7 on 2023-03-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_acessorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='acessorio',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]

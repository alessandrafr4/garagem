# Generated by Django 4.2.4 on 2023-08-25 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0002_veiculo_capa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="acessorio",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="Modelo",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=255)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="modelo", to="garagem.categoria"
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="modelo", to="garagem.marca"
                    ),
                ),
            ],
            options={
                "verbose_name": "modelo",
                "verbose_name_plural": "modelos",
            },
        ),
    ]
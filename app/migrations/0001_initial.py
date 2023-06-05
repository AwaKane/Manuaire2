# Generated by Django 4.1.5 on 2023-06-04 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("firstName", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                (
                    "genre",
                    models.CharField(
                        choices=[("Homme", "Homme"), ("Femme", "Femme")], max_length=10
                    ),
                ),
                ("nation", models.CharField(max_length=50)),
                ("staff", models.BooleanField(default=False)),
                ("admin", models.BooleanField(default=False)),
                ("personnel", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Etablissement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom_etablissement", models.CharField(max_length=50)),
                ("adresse", models.CharField(max_length=100)),
                ("localisation", models.CharField(max_length=500)),
                ("heureDebut", models.CharField(max_length=10)),
                ("heureFin", models.CharField(max_length=10)),
                ("phone", models.CharField(max_length=10)),
                (
                    "typeEtablissement",
                    models.CharField(
                        choices=[("Clinique", "Clinique"), ("Hopital", "Hopital")],
                        max_length=50,
                    ),
                ),
                ("prix", models.IntegerField(default=0)),
                (
                    "specialites",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "user_etablissement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RendezVous",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("objet", models.CharField(max_length=35)),
                ("detail", models.TextField()),
                ("date", models.DateField()),
                (
                    "etablissement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.etablissement",
                    ),
                ),
                (
                    "specialite",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_etablissement_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='logo',
            field=models.ImageField(default='app/logo.jpg', upload_to='etablissements/'),
        ),
    ]
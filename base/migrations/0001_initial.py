# Generated by Django 3.0.4 on 2021-08-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stripe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(blank=True, max_length=255)),
                ('secret_key', models.CharField(max_length=255)),
            ],
        ),
    ]
# Generated by Django 5.2.4 on 2025-07-05 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
        ('user_data', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='user_data.userprofile'),
        ),
    ]

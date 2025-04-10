# Generated by Django 5.1.7 on 2025-03-26 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_schedule', models.CharField(default='22-26 March', max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('heart_rate', models.IntegerField(default=72)),
                ('athlete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.athlete')),
            ],
        ),
    ]

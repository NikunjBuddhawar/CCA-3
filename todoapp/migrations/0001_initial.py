# Generated by Django 5.0.3 on 2024-08-09 15:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

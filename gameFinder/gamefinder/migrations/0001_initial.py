# Generated by Django 4.0.10 on 2023-04-07 20:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopingCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('developingCompany', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gamefinder.developingcompany')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('developingCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamefinder.developingcompany')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamefinder.genre')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamefinder.platform')),
            ],
        ),
    ]

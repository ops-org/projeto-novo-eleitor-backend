# Generated by Django 2.0.6 on 2018-06-25 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('abbreviation', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_site', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=128)),
                ('name_full', models.CharField(max_length=254)),
                ('sex', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='politicians', to='politician.Party')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fetch_time', models.DateTimeField()),
                ('cehap_sum', models.PositiveIntegerField(default=0)),
                ('secretary_sum', models.PositiveIntegerField(default=0)),
                ('politician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stats', to='politician.Politician')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-11-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pumedid', models.IntegerField()),
                ('first_author', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('journal', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('study', models.CharField(max_length=255)),
                ('disease', models.CharField(blank=True, max_length=255, null=True)),
                ('initial_sample_size', models.CharField(max_length=255)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('chr_id', models.IntegerField(blank=True, null=True)),
                ('chr_pos', models.IntegerField(blank=True, null=True)),
                ('strongest_snp_id_risks', models.CharField(blank=True, max_length=255, null=True)),
                ('snps', models.CharField(blank=True, max_length=255, null=True)),
                ('snp_id_current', models.IntegerField(blank=True, null=True)),
                ('context', models.CharField(blank=True, max_length=255, null=True)),
                ('risk_allele_frequency', models.FloatField(blank=True, null=True)),
                ('p_value', models.FloatField()),
                ('p_valueLog', models.FloatField()),
            ],
        ),
    ]

from django.db import models

# Create your models here.

class Database(models.Model):
    pumedid = models.IntegerField()
    first_author = models.CharField(max_length = 255)
    date = models.DateField()
    journal = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    study = models.CharField(max_length = 255)
    disease = models.CharField(max_length = 255, blank = True, null = True)
    initial_sample_size = models.CharField(max_length = 255)
    region = models.CharField(max_length = 255, blank = True, null = True)
    chr_id = models.IntegerField(null=True, blank=True)
    chr_pos = models.IntegerField(null=True, blank=True)
    strongest_snp_id_risks = models.CharField(max_length = 255, blank = True, null = True)
    snps = models.CharField(max_length = 255, blank = True, null = True)
    snp_id_current = models.IntegerField(null = True, blank = True)
    context = models.CharField(max_length = 255, null = True, blank = True)
    risk_allele_frequency = models.FloatField(null=True, blank=True)
    p_value = models.FloatField()
    p_valueLog = models.FloatField()

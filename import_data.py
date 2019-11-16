from SNP_site.models import Database

import csv
import pandas as pd
count = 0

CSV_PATH = "gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000(1).tsv"
#
# df = pd.read_csv(CSV_PATH, sep='\t', encoding='utf-8')
# # print(df.dtypes)
# df.DATE= pd.to_datetime(df.DATE)
# df.LINK = df.LINK.to_string()
# print(list(df.columns))
# Database.objects.create(pumedid= df['PUBMEDID'], first_author= df['FIRST AUTHOR'], date= df['DATE'], journal = df['JOURNAL'], link= df['LINK'], study = df['STUDY'], disease= df['DISEASE/TRAIT'],
# initial_sample_size= df['INITIAL SAMPLE SIZE'], region= df['REGION'], chr_id= df['CHR_ID'], chr_pos= df['CHR_POS'], snp_id_risks= df['STRONGEST SNP-RISK ALLELE'], snp_id = df['SNPS'], snp_id_current= df['SNP_ID_CURRENT'], context= df['CONTEXT'], risk_allele_frequency= df['RISK ALLELE FREQUENCY'],
# p_value = df['P-VALUE'],  p_valueLog = df['PVALUE_MLOG'] )

# for i in df:
#     print(df[i].head(2))
#     print(df[i].dtypes)
# accumulateur_data = []

# Ouvertur du fichier tsv
with open(CSV_PATH, newline ="") as csvfile:

    reader = csv.reader(csvfile, delimiter= "\t", quotechar = "'")
    print("Loading database...")
    next(reader,None)

    for row in reader:
        # print(row)

        if(row[9] == 'X'):
            row[9] = row[9].replace('X', '55') # conversion du chromosome X par 55

        if(row[15] == 'NR'):
            row[15] = row[15].replace('NR', '-1') # Conversion de NR (fréquence non renseigné) par rien (1)
        if(row[15] == ''):
            row[15] = row[15].replace('' , '-9999') # -9999 for empty data
        if(row[13] == ''):
            row[13] = row[13].replace('', '-9999') # -9999 for empty data
        if(row[14] == ''):
            row[14] = row[14].replace('', 'Empty_Data')
        if(row[8] == ''):
            row[8] = row[8].replace('', '-9999')  # -9999 for empty data
        if(row[9] == ''):
            row[9] = row[9].replace('', '-9999') # -9999 for empty data
        if(row[10] == ''):
            row[10] = row[10].replace('', '-9999') # -9999 for empty data
        Database.objects.create(pumedid= int(row[0]), first_author= row[1], date= row[2], journal = row[3], link= row[4], study = row[5], disease= row[6],
        initial_sample_size= row[7], region= row[8], chr_id= int(row[9]), chr_pos= int(row[10]), strongest_snp_id_risks= row[11], snps = row[12], snp_id_current= int(row[13]) , context= row[14], risk_allele_frequency= float(row[15]),
        p_value = float(row[16]),  p_valueLog = float(row[17]) )
        # print(row)
        # accumulateur_data += [row[9]]
#     print(f"{str(count)} succès d'insertion")
        # print(row[0])
# print(len(accumulateur_data))
# print(row[0])

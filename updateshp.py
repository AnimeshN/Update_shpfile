from dbfpy import dbf
import csv
db = dbf.Dbf("covid_hospitals.dbf")


# open csv file and make dictionary according to fid
with open('21may_health_facility.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    dict_csv = dict()
    for row in csv_reader:
        info = {'SNO': row['sno'],
                'STATE': row['state'],
                'DISTRICT': row['district'],
                'FACLTY_NAM': row['faclty_nam'],	
                'TYPE': row['type'],		
                'ISO_MINUS_': row['iso_minus_'],	
                'ISO_CONFM_': row['iso_confm_'],	
                'ISO_SUSPEC': row['iso_suspec'],	
                'O2SUPORTED': row['o2suported'],	
                'TOTAL_ICU':row['total_icu'],	
                'VENTILATOR': row['ventilator'],	
                'O2_MANIFOL': row['o2_manifol'],	
                'PPE': row['PPE'],	
                'N95': row['N95'],	
                'BIO_MED_WA': row['bio_med_wa'],	
                'ADDRESS': row['address'],	
                'PLACE_ID': row['place_id'],	
                'LATLONG': row['latlong'],	
                'CATEGORY': row['category'],	
                'ROW_NUMBER': row['row_number']}
        dict_csv[row['Facility_i']]=info
    

    #update the shpfile
    for rec in db:
        fid = rec['FACILITY_I']
        rec['ISO_MINUS_'] = float(dict_csv[fid]['ISO_MINUS_'])
        rec['ISO_MINUS_'] = float(dict_csv[fid]['ISO_MINUS_'])
        rec['ISO_CONFM_'] = float(dict_csv[fid]['ISO_CONFM_']) 	
        rec['ISO_SUSPEC'] = float(dict_csv[fid]['ISO_SUSPEC']) 
        rec['O2SUPORTED'] = float(dict_csv[fid]['O2SUPORTED']) 
        rec['TOTAL_ICU'] = float(dict_csv[fid]['TOTAL_ICU'])  	
        rec['VENTILATOR'] = float(dict_csv[fid]['VENTILATOR']) 	
        rec['O2_MANIFOL'] = float(dict_csv[fid]['O2_MANIFOL']) 	
        rec['PPE'] = float(dict_csv[fid]['PPE']) 	
        rec['N95'] = float(dict_csv[fid]['N95']) 	
        rec.store()



from dbfpy import dbf
import csv
db = dbf.Dbf("covid_hospitals.dbf")

csvfacility = set()
shpfacility = set()
dict_csv = dict()

# open csv file and make dictionary according to fid
with open('CatFacility30May2020.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        info = {'SNO': row['sno'],
                'STATE': row['state'],
                'DISTRICT': row['district'],
                'FACLTY_NAM': row['faclty_nam'],
                'CATEGORY': row['category'],	
                'TYPE': row['type'],		
                'FACILITY_I':row['Facility_i'],	
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
                }
        csvfacility.add(row['Facility_i'])
        dict_csv[row['Facility_i']]=info
    
    removedFacility = [] 
    #update the shpfile
    for rec in db:
        fid = rec['FACILITY_I']
        shpfacility.add(fid)
        if(dict_csv.get(fid)):
            rec['ISO_MINUS_'] = float(dict_csv[fid]['ISO_MINUS_'])
            rec['ISO_MINUS_'] = float(dict_csv[fid]['ISO_MINUS_'])
            rec['ISO_CONFM_'] = float(dict_csv[fid]['ISO_CONFM_']) 	
            rec['ISO_SUSPEC'] = float(dict_csv[fid]['ISO_SUSPEC']) 
            rec['O2SUPORTED'] = float(dict_csv[fid]['O2SUPORTED']) 
            rec['TOTAL_ICU'] = float(dict_csv[fid]['TOTAL_ICU'])  	
            rec['VENTILATOR'] = float(dict_csv[fid]['VENTILATOR']) 	
            rec['O2_MANIFOL'] = float(dict_csv[fid]['O2_MANIFOL']) 	
            rec['BIO_MED_WA'] = float(dict_csv[fid]['BIO_MED_WA']) 	
            rec['PPE'] = float(dict_csv[fid]['PPE']) 	
            rec['N95'] = float(dict_csv[fid]['N95']) 	
            rec.store()
        else:
            rec['FACILITY_I'] = 0
            rec.store()

    

removedFacilityID = shpfacility.difference(csvfacility)
addedFacilityID = csvfacility.difference(shpfacility)
print('Added facility: {}'.format(len(addedFacilityID)))
print('Removed facility: {}'.format(len(removedFacilityID)))
newFacility = []
for newfac in addedFacilityID:
    newFacility.append(dict_csv[newfac])

# print(newFacility)
csv_file = "newFacility.csv"
# csv_columns = ['sno','state','district','faclty_nam','category','type','Facility_i','iso_minus_','iso_confm_','iso_suspec',	'o2suported','total_icu','ventilator','o2_manifol','PPE','N95','bio_med_wa']
csv_columns = ['SNO','STATE','DISTRICT','FACLTY_NAM','CATEGORY','TYPE','FACILITY_I','ISO_MINUS_','ISO_CONFM_','ISO_SUSPEC',	'O2SUPORTED','TOTAL_ICU','VENTILATOR','O2_MANIFOL','PPE','N95','BIO_MED_WA']


with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in newFacility:
        writer.writerow(data)

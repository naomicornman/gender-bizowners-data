from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
thefilename = join(DATA_DIR, 'BizOwners.csv')

#WRANGLED_HEADERS = ['caseNumber','sentence','registrationDate','Expiration_Date','category','firstName','middleName','lastName','Date_Of_Birth','age','sex','race','SID_Number','district','post','neighborhood','Location 1']
WRANGLED_HEADERS = ['Owner_First_Name','Owner_Last_Name', 'Title']

# 'committee_name','filing_number','form_type','line_type','superseded_by_amendment','filer_committee_id_number','transaction_id','back_reference_tran_id_number','back_reference_sched_name','entity_type,contributor_name','contributor_organization_name','contributor_last_name','contributor_first_name','contributor_middle_name','contributor_prefix','contributor_suffix','contributor_street_1','contributor_street_2','contributor_city','contributor_state','contributor_zip','election_code','election_other_description','contribution_date','contribution_date_formatted','contribution_amount','contribution_aggregate','contribution_purpose_code','contribution_purpose_descrip','contributor_employer','contributor_occupation','donor_committee_fec_id','donor_committee_name','donor_candidate_fec_id','donor_candidate_name','donor_candidate_last_name','donor_candidate_first_name','donor_candidate_middle_name','donor_candidate_prefix','donor_candidate_suffix','donor_candidate_office','donor_candidate_state','donor_candidate_district','conduit_name','conduit_street1','conduit_street2','conduit_city','conduit_state','conduit_zip','memo_code','memo_text_description','reference_code']
# ['contributor_last_name', 'contributor_first_name', 'contributor_city' , 'contributor_state' , 'contributor_zip', 'contribution_amount']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangle_Biz.csv')


newlist = []
with open(thefilename, 'r') as thefile:
    for line in thefile:
        commas=line.count(',')
        if commas == 7:
            Account_Number,Legal_Name,Owner_First_Name,Owner_Middle_Initial,Owner_Last_Name,Suffix,Legal_Entity_Owner,Title = line.split(',')[:8]
        else:
            Account_Number,Legal_Name,Extra,Owner_First_Name,Owner_Middle_Initial,Owner_Last_Name,Suffix,Legal_Entity_Owner,Title = line.split(',')[:9]
            Legal_Name=Legal_Name+', '+Extra        
        namesdict = {}
        if (Owner_First_Name != "") or (Owner_Last_Name != ""):
            namesdict['Owner_First_Name'] = Owner_First_Name
            namesdict['Owner_Last_Name'] = Owner_Last_Name
            namesdict['Title'] = Title
            newlist.append(namesdict)

thefile.close()

wfile = open(WRANGLED_DATA_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# wcsv.writeheader()

def titlerank(xdict):
    return (xdict['Title'])
my_final_list=newlist
#my_final_list = sorted(newlist, key=titlerank)
for row in my_final_list:
    wcsv.writerow(row)
wfile.close()

finalfile = open(WRANGLED_DATA_FILENAME, 'r')
thestupidlines = finalfile.readlines()[0:5]
for line in thestupidlines:
     print(line.strip())

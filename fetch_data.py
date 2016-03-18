from os import makedirs
from os.path import basename, join

import requests
DATADIR = 'tempdata'
makedirs(DATADIR, exist_ok=True)

URL = "https://data.cityofchicago.org/api/views/ezma-pppn/rows.csv?accessType=DOWNLOAD"
datapath = join(DATADIR, 'BizOwners.csv')

resp = requests.get(URL).text

datanames = open(datapath, 'w')
datanames.write(resp)
datanames.close()

print("Downloading", URL)

# # http://realtime.influenceexplorer.com/api/independent-expenditures/?ordering=-expenditure_date_formatted&candidate_id_checked=P80001571&clientkey=9bgzCVS4RFj9GpRk0PYEb75b6WLi7sfaFNvVODkMGrVU-Di-640ygJ&format=csv


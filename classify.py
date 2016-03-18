from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender

WRANGLED_DATA_FILE = join('tempdata', 'wrangle_Biz2.csv')
CLASSIFIED_DATA_FILE = join('tempdata', 'classifed_Biz.csv')
# makedirs(CLASSIFIED_DATA_DIR, exist_ok=True)
# DATA_HEADERS_FILENAME = join(ORIGINAL_DATA_DIR, 'indiv_header_file.csv')


def extract_usable_name(namestr):
    # split into two pieces, at most
    nameparts = namestr.split(' ')
    for n in nameparts:
        if '.' not in n:
            return n  # returns the first thing that has no period
    # if we get to this point...then...just return nothing
    return ""


with open(WRANGLED_DATA_FILE) as f:
    articles = list(DictReader(f))

classified_headers = list(articles[0].keys()) + ['usable name', 'gender', 'ratio']

# prepare the CSV
w = open(CLASSIFIED_DATA_FILE, 'w');
dw = DictWriter(w, fieldnames=classified_headers)
dw.writeheader()

with open(WRANGLED_DATA_FILE) as r:
    datarows = list(DictReader(r))
    ct = 0
    for row in datarows:
        usablename = extract_usable_name(row['Owner First Name'])
        ct += 1
        print("Row:", ct, "extracting --", usablename, "-- from:", row['Owner First Name'])
        gender_result = detect_gender(usablename)
        row['usable name'] = usablename
        row['gender'] = gender_result['gender']
        row['ratio'] = gender_result['ratio']
        dw.writerow(row)


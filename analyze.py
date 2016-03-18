from os.path import join
from csv import DictReader
CLASSIFIED_DATA_FILE = join('tempdata','classified_Biz.csv')
MIN_GENDER_RATIO = 95

print("Opening and reading", CLASSIFIED_DATA_FILE)
print("==============================================")
datarows = list(DictReader(open(CLASSIFIED_DATA_FILE)))

print("Total demographics")
totalPeeps=0
males=0
females=0
for d in datarows:
	gender = d['gender']
	totalPeeps+=1
	if gender == 'M':
		males+=1
	else:
		females+=1

print("Total = ", totalPeeps)
print("Males = ", males, ",", (round((males/totalPeeps)*100)), "%")
print("Females = ", females, ",", (round((females/totalPeeps)*100)), "%")


print("-----------------------------------------------")

print("Total leadership demographics")
leaders=0
nonLeaders=0
for d in datarows:
	Title = d['Title']
	if 'PRESIDENT' in Title or 'CEO' in Title or "SOLE PROPRIETOR" in Title:
		leaders+=1
	else:
		nonLeaders+=1

print("Leaders = ", leaders)
print("Non Leaders = ", nonLeaders)

print("-----------------------------------------------")

print("Gender of Leadership")
maleLeaders=0
femaleLeaders=0
for d in datarows:
	gender = d['gender']
	Title = d['Title']
	if gender == 'F':
		if 'PRESIDENT' in Title or 'CEO' in Title or "SOLE PROPRIETOR":
			femaleLeaders+=1
	if gender == 'M':
		if 'PRESIDENT' in Title or 'CEO' in Title or "SOLE PROPRIETOR":
			maleLeaders+=1

print("Female Leaders = ", femaleLeaders,",", (round((femaleLeaders/totalPeeps)*100)), "%")
print("Male Leaders = ", maleLeaders, ",",(round((maleLeaders/totalPeeps)*100)), "%")

print("---------------------------------------------")

print("Shareholder demographics")
shareholders=0
otherPeeps=0
for d in datarows:
	Title = d['Title']
	if 'SHAREHOLDER' in Title:
		shareholders+=1
	else:
		otherPeeps+=1

print("Shareholders = ", shareholders, ",", (round((shareholders/totalPeeps)*100)), "%")

Fshareholders=0
for d in datarows:
	Title = d['Title']
	if gender == 'F':
		if 'SHAREHOLDER' in Title:
			Fshareholders+=1
print("Female Shareholders =", Fshareholders)






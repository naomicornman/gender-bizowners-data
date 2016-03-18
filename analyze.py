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

print("---------------------------------------------")

print("Job Titles")

from collections import Counter

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
    	if value not in seen:
    		output.append(value)
    		seen.add(value)
    return output
# Remove duplicates from this list.
values = [datarows]
result = remove_duplicates(values)
print(result)


# for name, counts in 
# 	xdict['Title'] = Title
# # 	newlist.append(xdict)
# result = remove_duplicates(values)
# print(Counter(result))




# for k, v in items.items():
#     sorted_v = tuple(sorted((k2, v2) for k2, v2 in v.items()))
#     unique_items.add(sorted_v)
# unique_items = dict(unique_items)

# print (newdict)



#     for k, v in items.items():
#     sorted_v = tuple(sorted((k2, v2) for k2, v2 in v.items()))
#     unique_items.add(sorted_v)
# unique_items = dict(unique_items)

#     for value in values:
#         # If value has not been encountered yet,
#         # ... add it to both list and set.
#         if value not in seen:
#             output.append(value)
#             seen.add(value)
#     return output

# # Remove duplicates from this list.
# values = []
# result = remove_duplicates(values)
# print(Counter(result))


# unique_items = set()
# for k, v in items.items():
#     sorted_v = tuple(sorted((k2, v2) for k2, v2 in v.items()))
#     unique_items.add(sorted_v)
# unique_items = dict(unique_items)




# newlist = []
# for d in datarows:
# 	xdict = {}
# 	xdict['Title'] = Title
# 	newlist.append(xdict)

# newerlist = []
# for i in newlist:
# 	if i not in newerlist:
# 		newerlist.append(i)

# print (newerlist)





# unique_titles = {}
# for d in datarows:
# 	unique_titles.append(d[2])

# print (unique_titles)



#     unique_members[d['Title']] = d


# for Title in unique_members.items():
# 	gd = person['gender']
# 	genderdict[gd].append(person)

# unique_member_count = len(unique_members)
# print (unique_member_count)









import json
selyear = input("Select a year\n")


try:
    jfile = open("lodgingdb" + selyear + ".js")
except:
    print("That file does not exist")
    quit()

data = json.load(jfile)

dd=[]
for item in data["lodgingdb" + selyear]:
    fullname = item['Name']
    splitname = fullname.partition(" ")
    if fullname.find(" ") == -1:
        surname = fullname
        title = ''
    else:
        surname = splitname[2]
        title = splitname[0]
    dd.append(surname + ' ' + title)

#Sort names alphabetically 
ds = sorted(dd)

sd = []

for i in ds:
    sd.append((i, ds.count(i)))

#Remove duplicates
sd = list(dict.fromkeys(sd))

#Sort by count
sd.sort(key=lambda a: a[1], reverse=True)
for i in sd:
    print(i[0], i[1])
    

jfile.close()
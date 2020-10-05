
import json
import csv
tits=[]
all_data=[]
for item in range(0,3160):
    with open("bing_results_10_"+str(item)+".json","r") as fp:
        data=json.load(fp)
        print(len(data["value"]))
        for el in range(0,len(data["value"])):
            if data["value"][el]["name"] not in tits:
                tits.append(data["value"][el]["name"])
            try:
                all_data.append([data["value"][el]["name"],data["value"][el]["description"],data["value"][el]["url"],data["value"][el]["provider"][0]["name"],data["value"][el]["datePublished"]])
            except:
                all_data.append([data["value"][el]["name"],data["value"][el]["description"],"","",""])
with open('bing_file_10.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["title","desciption","url","provider","date"])
    for el in all_data:
        employee_writer.writerow(el)
print(len(tits))

import json
import csv

all_data=[]
for item in range(1,101):
    with open("bing_results_"+str(item)+".json","r") as fp:
        data=json.load(fp)
        for el in range(0,len(data["value"])):
            print(data["value"][el])
            try:
                all_data.append([data["value"][el]["name"],data["value"][el]["description"],data["value"][el]["url"],data["value"][el]["datePublished"]])
            except:
                all_data.append([data["value"][el]["name"],data["value"][el]["description"],"",""])
with open('bing_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["title","desciption","url","date"])
    for el in all_data:
        employee_writer.writerow(el)


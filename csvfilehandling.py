import csv

data = [['name','age','sal'],
        ['bhushan',20,199999],
        ['max',31,199999]]

with open('emp.csv','w') as f:
    write = csv.writer(f)
    write.writerows(data)

with open('emp.csv','r') as f:
    read = csv.DictReader(f)
    for rows in read:
        print(rows)





data = [
    ["Name", "Age", "City"],
    ["Bhushan", 22, "Bengaluru"],
    ["Alice", 25, "Delhi"]
]

with open("output.csv", mode="w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    file.seek(0)
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('output.csv', mode='a+',newline='') as file:
    writ = csv.writer(file)
    writ.writerow(['hi','hello','hy','bye'])
    writ.writerow(['hi'])
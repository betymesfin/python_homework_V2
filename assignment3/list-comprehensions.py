import csv
with open("csv/employees.csv", newline='') as file:
    reader = csv.reader(file)
    employees = [row for row in reader]


full_names = [row[1] + " " + row[2] for row in employees[1:]]

print(full_names)

names = [name for name in full_names if 'e' in name]

print("names with letter e:", names)

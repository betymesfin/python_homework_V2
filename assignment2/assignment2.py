import csv
import traceback
import os
import custom_module

from datetime import datetime
#Task Two

def read_employees():
        dict={}
        list=[]
        try:
            with open('../csv/employees.csv', 'r') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i == 0:
                        dict["fields"] = row 
                    else:
                        list.append(row) 

            dict["rows"] = list
            return dict 
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}") 


employees=read_employees()
print(employees)


#Task Three

def column_index(column_name):
        return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")
print(employee_id_column)



#Task Four

def first_name(row_number):
     first_name_column=column_index("first_name")
     row=employees["rows"][row_number]

     return row[first_name_column]
print(first_name(2))

#Task Five

def employee_find(employee_id):
     def employee_match(row):
        return int(row[employee_id_column]) == employee_id
     matches=list(filter(employee_match, employees["rows"]))
     return matches

print(employee_find(20))




#Task Six

def employee_find_2(employee_id): 
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"])) 
    return matches
print(employee_find_2(20))



#Task Seven
def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]
print(sort_by_last_name())


#Task Eight

def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[i]
    return result
print(employee_dict(employees["rows"][19]))


#Task Nine
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]  
        result[emp_id] = employee_dict(row)  
    return result

print(all_employees_dict())

#Task Ten

def get_this_value():
      return os.environ.get("THISVALUE")
print(get_this_value())


#Task Eleven

def set_that_secret(new_secret):
     custom_module.set_secret(new_secret)
     
set_that_secret("CTD")
print(custom_module.secret)



#Task Tweleve

def read_minutes_file(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}

def read_minutes():
     minutes1 = read_minutes_file("../csv/minutes1.csv")
     minutes2 = read_minutes_file("../csv/minutes2.csv")
     return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


#Task Thirteen 

def create_minutes_set():
     rows1 = minutes1["rows"]
     rows2 = minutes2["rows"]
    
 
     set1 = set(rows1)
     set2 = set(rows2)
    
   
     union = set1 | set2
    
     return union
print("****************************************************************************************************************************************")
minutes_set=create_minutes_set()
print(minutes_set)

#Task Fourteen 

def create_minutes_list():
     x = list(minutes_set)
     converted = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), x)
     return list(converted)

minutes_list = create_minutes_list()
print("****************************************************************************************************************************************")
print(minutes_list)


#Task Fifteen

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list
written_list = write_sorted_list()
print("****************************************************************************************************************************************")
print(written_list)
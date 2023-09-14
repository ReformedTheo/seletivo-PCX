import requests
import json


#api url
url = "http://127.0.0.1:8000/api/employees/"

#consume api to get data
request = requests.get(url)
data = request.json()

#store data in JSON
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

#functions to calculate requested infos

#this one will get the ones with highest and lowest salaries
def get_highest_lowest_salary_employees(data):
    highest_salary_employee = max(data, key=lambda x: x['salary'])
    lowest_salary_employee = min(data, key=lambda x: x['salary'])
    return highest_salary_employee, lowest_salary_employee

#this one will get the longest and short tenure employee
def get_longest_shortest_tenure_employees(data):
    longest_tenure_employee = min(data, key=lambda x: x['admission'])
    shortest_tenure_employee = max(data, key=lambda x: x['admission'])
    return longest_tenure_employee, shortest_tenure_employee

#obtain requested info
highest_salary_employee, lowest_salary_employee = get_highest_lowest_salary_employees(data)
longest_tenure_employee, shortest_tenure_employee = get_longest_shortest_tenure_employees(data)

#print info
print('Funcionário com maior salário:', highest_salary_employee['name'], highest_salary_employee['salary'])
print('Funcionário com menor salário:', lowest_salary_employee['name'], lowest_salary_employee['salary'])
print('Funcionário com maior tempo de empresa:', longest_tenure_employee['name'], longest_tenure_employee['admission'])
print('Funcionário com menor tempo de empresa:', shortest_tenure_employee['name'], shortest_tenure_employee['admission'])

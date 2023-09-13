import json
import random
from faker import Faker
import requests

fake = Faker('pt_BR')

def generate_employee():
    return {
        "name": fake.name(),
        "job": fake.random.choice(["DE", "MA", "AN", "TE", "SU"]),
        "salary": "{:.2f}".format(random.uniform(5000, 10000)),
        "admission": fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d"),
        "active": 0
    }

data = [generate_employee() for _ in range(15)]

with open('inactive_employees.json', 'w') as f:
    json.dump(data, f, indent=2)

# URL da sua API
url = 'http://127.0.0.1:8000/api/employees/'

# Ler os dados do arquivo
with open('inactive_employees.json', 'r') as f:
    data = json.load(f)

# Enviar os dados para a API um por um
for employee in data:
    response = requests.post(url, json=employee)

    # Verificar se os dados foram enviados com sucesso
    if response.status_code == 201:
        print('Dados enviados com sucesso!')
    else:
        print('Erro ao enviar os dados:', response.status_code, response.text)

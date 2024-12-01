import requests
from Tools.scripts.generate_opcode_h import header

url = 'http://127.0.0.1:8000/api/auth'


response = requests.post(url, data = {'username' : 'admin', 'password' : '12345678'})
print(response.text)

myToken = response.text

header = {'Authorization': 'Token' + myToken}
requests.get('http://127.0.0.1:8000/api/equipment_list', headers=header)
requests.get('http://127.0.0.1:8000/api/division_list', headers=header)
requests.get('http://127.0.0.1:8000/api/master_list', headers=header)
requests.get('http://127.0.0.1:8000/api/yard_list', headers=header)
requests.get('http://127.0.0.1:8000/api/site_list', headers=header)
requests.get('http://127.0.0.1:8000/api/transaction_list', headers=header)
requests.get('http://127.0.0.1:8000/api/driver_list', headers=header)

print(response)
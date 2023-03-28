import json
import requests

url = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data = {}
    if data is not None:
        data = {"id":id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=url, headers=headers ,data=json_data)
    print(r.json())

# get_data()

def post_data():
    data = {
        'name':'santosh',
        'roll':12,
        'city':'jaipur'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=url, headers=headers ,data=json_data)
    print(r.json())

post_data()
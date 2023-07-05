import requests
from datetime import datetime

#DOCUMENTATION: https://docs.pixe.la/entry/delete-graph

#Create your user account
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = 'henijo881'
USERNAME = 'henithedog'
GRAPH_ID = 'graph8'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
response = requests.post(pixela_endpoint, json=user_params)

#print(response.text)

#Create a graph definition
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': GRAPH_ID,
    'name': 'Python Graph',
    'unit': 'Hr',
    'type': 'float',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(graph_endpoint, json=graph_params, headers=headers)
#https://pixe.la/v1/users/henithedog/graphs/graph8.html

value_to_graph_enpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime(year=2023, month=7, day=1)
#print(today.strftime("%Y-%m-%d"))

value_to_graph = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '10.88'
}

response = requests.post(value_to_graph_enpoint, json=value_to_graph, headers=headers)

#print(response.text)

#UPDATE
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230704"

update_data = {
    'quantity': '20.88'
}

response = requests.put(update_endpoint, json=update_data, headers=headers)
print(response.text)

#DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230704"
response = requests.delete(delete_endpoint, headers=headers)
#print(response.text)
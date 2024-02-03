import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""

user_params = {
    "notMinor": "yes",
    "agreeTermsOfService": "yes"
}
# response = requests.post(url = pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
ID = "graph1"
graph_params={
    "id":ID,
    "name":"cycling",
    "unit":"kilometre",
    "type":"float",
    "color":"ajisai"
}
header = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_params,headers= header)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_data={
    "date":today,
    "quantity":"3",
}
# response = requests.post(url=post_endpoint,json=pixel_data,headers=header)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today}"
new_pixel_data = {
    "quantity":"5"
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=header)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today}"
response = requests.delete(url=delete_endpoint,headers=header)
print(response.text)
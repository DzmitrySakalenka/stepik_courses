import requests
import json

client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'

resp = requests.post("https://api.artsy.net/api/tokens/xapp_token", data={"client_id" : client_id, "client_secret" : client_secret}).text
token = json.loads(resp)["token"]

def get_json(url):
    headers = {"X-Xapp-Token" : token}
    resp = requests.get(url, headers=headers).text
    return json.loads(resp)

ans = []

with open("dataset_24476_4.txt") as inp:
    for id in inp:
        id = id.rstrip()
        js = get_json("https://api.artsy.net/api/artists/" + id)
        ans.append((js["birthday"], js["sortable_name"]))

ans.sort(key=lambda x: (int(x[0]), x[1]))
print("\n".join(map(lambda x: x[1], ans)))
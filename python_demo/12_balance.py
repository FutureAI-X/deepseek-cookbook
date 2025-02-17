import requests

url = "https://api.deepseek.com/user/balance"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer <API Key>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
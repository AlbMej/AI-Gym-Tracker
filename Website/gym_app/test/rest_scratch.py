import requests
url = 'http://127.0.0.1:8000/test-auth/'
headers = {'Authorization': 'Token 2a603ef3f7f20d7efcd2edbc28e77ff70e598d22'}
r = requests.get(url)
print(r.text)
r = requests.get(url, headers=headers)
# print(r.response)
print(r.text)

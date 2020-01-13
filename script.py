import requests

r = requests.get("https://tanipadu.id")
print(r.status_code)
print(r.ok)
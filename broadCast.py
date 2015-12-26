import http.client
import json

connection = http.client.HTTPSConnection('api.github.com')

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello world github/linguist#1 **cool**, and #1!'}
json_foo = json.dumps(foo)

connection.request('POST', '/markdown', json_foo, headers)

response = connection.getresponse()
print(response.read().decode())
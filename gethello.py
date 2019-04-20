import http.client
#import json
conn = http.client.HTTPConnection('rica.topedu.io:5000')
#conn = http.client.HTTPSConnection('www.python.org')

#conn.request('GET', '/')
conn.request('GET', '/v2/payments/oneTimeKeys')
r1 = conn.getresponse()
print(r1.read().decode())
print(r1.status, r1.reason)
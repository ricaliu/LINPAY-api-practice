#import httplib
import http.client
import json
conn = http.client.HTTPSConnection('sandbox-api-pay.line.me')
headers = {'Content-type': 'application/json',
           'X-LINE-ChannelId': '1649580251',
           'X-LINE-ChannelSecret': 'ddca54d0f3e50847af3f6ec4fcaef890'
}
payment = {
    "productName": "Demo",
    "productImageUrl": "https://via.placeholder.com/150",
    "amount": 168,
    "currency": "TWD",
    "confirmUrl": "http://localhost",
    'orderId': 'TW2019-LINE-00001'
}
json_data = json.dumps(payment)
conn.request('POST', '/v2/payments/request', json_data, headers)

response = conn.getresponse()
print(response.read().decode())
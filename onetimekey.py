import http.client
import json
conn = http.client.HTTPSConnection('sandbox-api-pay.line.me')
headers = {'Content-type': 'application/json',
 'X-LINE-ChannelId': '1649580251',
 'X-LINE-ChannelSecret': 'ddca54d0f3e50847af3f6ec4fcaef890'
}
payment = {
  "productName": "test product",    
  "amount": 100,    
  "currency": "TWD",    
  "orderId": "merchant_test_order_1",    
  "oneTimeKey": "385917470247977065"
}
json_data = json.dumps(payment)
conn.request('POST', '/v2/payments/oneTimeKeys/pay', json_data, headers)

response = conn.getresponse()
print(response.read().decode())
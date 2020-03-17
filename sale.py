import http.client, json, random, time, sys

conn = http.client.HTTPConnection('localhost:8082')

#headers = {'Content-type': 'application/vnd.kafka.avro.v2+json',
headers = {'Content-type': 'application/vnd.kafka.json.v2+json',
           'Accept': 'application/vnd.kafka.v2+json'}

i=0
total = 1037
#for i in range(1000):
while True:
  #s = {"value":"\"sku\":" + str(random.randint(1,100)) + ",\"quantity\":" + str(random.randint(1,3)) + ",\"price\":" + str(random.randint(1,20))}
  i+=1
  sku=random.randint(49,51)
  quantity=random.randint(1,3)
  total = total - quantity

  s = {"key":i,"value":{"txnid":i,"ts":round(time.time()),"sku":sku,"quantity":quantity,"price":random.randint(1,20)}}
  records = []
  records.append(s)
  #data = {"value_schema": "{\"name\":\"sku\",\"type\": \"int\",\"name\":\"quantity\",\"type\": \"int\",\"name\":\"price\",\"type\": \"int\"}","records":records}
  data = {"records":records}
  json_data = json.dumps(data)
  print(json_data)
  conn.request('POST', '/topics/sales', json_data, headers)
  response = conn.getresponse()
  l=response.read().decode()
  if response.status != 200:
    print(response.status,response.reason)
  time.sleep(1/int(sys.argv[1]))

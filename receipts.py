import sys, datetime, time, uuid
from json import dumps, loads
from confluent_kafka import Producer, Consumer

producer = Producer({'bootstrap.servers':'localhost:9092'})

c = Consumer({'bootstrap.servers':'localhost:9092',
              'group.id': str(uuid.uuid1())})

c.subscribe(["SOH"])

while True:
  message = c.poll(timeout=1.0)
  if message != None:
    j = loads(message.value())
    sku=list(j.items())[0][1]
    stock_on_hand=list(j.items())[1][1]
    if int(stock_on_hand) < 100:
      s = {"txnid":1,"sku":sku,"ts":round(time.time()),"quantity":200}
      producer.produce('receipts', dumps(s), str(sku))
      print("Inventory for SKU",sku,"was low at",stock_on_hand,"units, so we ordered and received 200 more")
      producer.flush()

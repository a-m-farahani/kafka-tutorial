from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))


while True:
    data = {"sensorID": "AI110", "value": random.random(),
            "timestamp": time.time()}
    print("[Sending]", data)
    producer.send('sensors', value=data)
    time.sleep(5)

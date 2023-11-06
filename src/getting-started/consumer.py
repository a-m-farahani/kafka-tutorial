from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'sensors',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(f"[recv] offset: {message.offset}, data: {message.value}")

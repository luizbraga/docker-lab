import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

TOPIC_NAME = 'test-topic'

# produce json messages
producer = KafkaProducer(
  bootstrap_servers=['localhost:9092'],
  value_serializer=lambda m: json.dumps(m).encode('ascii'))

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

# produce asynchronously with callbacks
record = producer.send(
  TOPIC_NAME,
  {'key': 'value'}
  ).add_callback(on_send_success)

# Wait until it is sent
producer.flush()

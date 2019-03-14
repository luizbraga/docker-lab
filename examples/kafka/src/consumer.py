import json
from kafka import KafkaConsumer

TOPIC_NAME = 'test-topic'

# To consume latest messages and auto-commit offsets
# You can desable auto-commit with enable_auto_commit=False flag
# consume json messages
consumer = KafkaConsumer(TOPIC_NAME,
                         group_id='test-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

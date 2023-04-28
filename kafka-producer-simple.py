# https://kafka-python.readthedocs.io/en/master/usage.html#kafkaproducer

import binascii

from kafka import KafkaProducer
from kafka.errors import KafkaError

import sample_pb2

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', compression_type='gzip')
# this serializer also works, but need to remove the "b" bytes type in the producer.send
# command and change the value_deserializer in the kafka-consumer.py consumer file
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092', compression_type='gzip',
#     value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')))

# want to convert to binary format here:
# b64encoded = base64.b64encode(msg.SerializeToString())
# KeySerializer to be an IntegerSerializer
# ValueSerializer to be StringSerializer
#
# https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
# Each Protocol Buffer class has methods for reading and writing messages using a
# Protocol Buffer-specific encoding, that encodes messages into binary format.
# Those two methods are SerializeToString() and ParseFromString().


future1 = producer.send('sample', b'{"a": 2, "b": 3}')
# future = producer.send('sample', '{"a": 2, "b": 3}')

# Block for 'synchronous' sends
try:
    record_metadata = future1.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    print(f"KafkaError: {KafkaError}")


# Successful result returns assigned partition and offset
print(f"topic: {record_metadata.topic}")
print(f"partition: {record_metadata.partition}")
print(f"offset: {record_metadata.offset}")

# producer.send('sample', b'Hello, World!')
# producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')

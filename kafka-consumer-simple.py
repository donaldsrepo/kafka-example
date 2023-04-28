from kafka import KafkaConsumer
import json
from google.protobuf.json_format import Parse, ParseDict
import binascii

import sample_pb2
# from google.protobuf.any_pb2 import Any


# use topic created earlier
consumer = KafkaConsumer('sample')
# this deserializer also works, but need to change the value_serializer in the kafka-producer.py file
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092', compression_type='gzip', value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')))

# consumer = KafkaConsumer(
#     'sample', value_deserializer=lambda v: binascii.unhexlify(v.decode('utf-8')))

for message in consumer:
    print(f"message in protobuf format: {message}")
    mv = json.loads(str(message.value.decode('utf-8')))

    # value = ParseFromString(message.value)  # example
    # print(f"parsed value {value}")

    # mv = {"a": 1, "b": 2}
    print(message)
    print(f"message value: { mv } ")
    message_out = ParseDict(mv, sample_pb2.Sample())
    # or
    message_out = Parse(json.dumps(mv), sample_pb2.Sample())

    print(f"value for a: {message_out.a}")  # "a string value"

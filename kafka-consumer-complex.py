from kafka import KafkaConsumer
import json
from google.protobuf.json_format import Parse, ParseDict, MessageToJson, MessageToDict
import binascii


import sample_pb2
# from google.protobuf.any_pb2 import Any


# use topic created earlier
# ref: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
# credentials ref: https://stackoverflow.com/questions/42987129/kafka-10-python-client-with-authentication-and-authorization
consumer = KafkaConsumer('sample', bootstrap_servers='localhost:9092')
consumer = KafkaConsumer()
# this deserializer also works, but need to change the value_serializer in the kafka-producer.py file
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092', compression_type='gzip', value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')))

# consumer = KafkaConsumer(
#     'sample', value_deserializer=lambda v: binascii.unhexlify(v.decode('utf-8')))

for message in consumer:
    my_msg = sample_pb2.Sample()
    print(f"original message.value {message.value}")
    value = my_msg.ParseFromString(message.value)
    print(f"parsed message.value {value}")

    print(f"my_msg: {my_msg}")
    '''
    my_msg
    a: 4
    b: 5
    '''
    print(f"message in protobuf format: {message}")

    my_keys = my_msg.DESCRIPTOR.fields_by_name.keys()
    print(f"keys: {my_keys}")
    print(f"value for a: {my_msg.a}")  # "a string value"

    my_msg_json = MessageToJson(my_msg).replace(
        '\r', '').replace('\n', '')  # '{\n  "a": 4,\n  "b": 5\n}'

    my_msg_dict = MessageToDict(my_msg)  # {'a': 4, 'b': 5}

    print(f"my_msg_json: {my_msg_json}")
    print(f"my_msg_dict: {my_msg_dict}")

    '''
    # mv = json.loads(str(my_msg))  # '{"a": 2, "b": 3}' my_msg in wrong format for json

    (Pdb) my_msg
a: 4
b: 5
    '''

    '''
    not working
    message_out = ParseDict(my_msg_json, sample_pb2.Sample())
    # or
    message_out = Parse(json.dumps(my_msg_json), sample_pb2.Sample())


    print(f"value for a: {message_out.a}")  # "a string value"
    '''

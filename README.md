Reference: ??

Related Reference:
https://www.linkedin.com/pulse/installing-kafka-windows-creating-factors-ganesh-m-j/?trk=read_related_article-card_title

this example includes the setup of a zookeeper and kafka service, a kafka
producer where you type in some json and a PYTHON KAFKA CONSUMER that signs up
for a topic, reads messages sent to the topic and converts the json messages to
protobuf format

run this command in a DOS prompt shell to get conda activated:
C:\Users\Don\anaconda3\Scripts\activate.bat C:\Users\Don\anaconda3

create environment to run kafka code:

> conda create -n kafka-env python=3.7 kafka-python

https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d

To select a specific environment, use the Python: Select Interpreter command
from the Command Palette (Ctrl+Shift+P).

to keep from upgrading conda, need to include it in each conda install command
conda install kafka-python conda=4.9.2

--for home only:start

install zookeeper and kafka
https://shaaslam.medium.com/installing-apache-kafka-on-windows-495f6f2fd3c8

install java jre from here:
https://www.oracle.com/java/technologies/javase/javase9-archive-downloads.html

install and setup zookeeper:
https://shaaslam.medium.com/installing-apache-zookeeper-on-windows-45eda303e835#.fgofwm6n6

startup zookeeper server:

> zkserver

default port is 2181, can change in config conf/zoo.cfg file

setup kafka server in new terminal - By default Apache Kafka will run on port
9092

> cd C:\Tools\kafka\kafka_2.13-3.2.3\
> .\bin\windows\kafka-server-start.bat .\config\server.properties

create a topic in new terminal

> cd C:\Tools\kafka\kafka_2.13-3.2.3\bin\windows

kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor
1 --partitions 1 --topic sample

start a kafka-producer

> kafka-console-producer.bat --broker-list localhost:9092 --topic sample

start a kafka consumer

> cd C:\Tools\kafka\kafka_2.13-3.2.3\bin\windows

kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic sample

type in messages in the producer window and you will see them show up in the
consumer window

> hello

create an example using a python based kafka-consumer: start a kafka-producer

create another topic

> cd C:\Tools\kafka\kafka_2.13-3.2.3\bin\windows

kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor
1 --partitions 1 --topic sample

start the producer with the new topic

> cd C:\Tools\kafka\kafka_2.13-3.2.3\bin\windows kafka-console-producer.bat
> --broker-list localhost:9092 --topic sample

--for home only:end

start the python-based consumer in an anaconda prompt window (need to run this
first: conda install kafka-python)

run this command in a DOS prompt shell to get conda activated:
C:\Users\Don\anaconda3\Scripts\activate.bat C:\Users\Don\anaconda3

conda activate kafka-env

do once:

to convert from json to protobuf:

conda install protobuf

install protobuf compiler:
https://github.com/protocolbuffers/protobuf/blob/main/src/README.md#c-installation---windows

https://github.com/protocolbuffers/protobuf/releases/tag/v21.6 for source code

https://github.com/protocolbuffers/protobuf/releases/latest for binary exe file

run this command to create .proto file:

cd C:\Tools\pb\protoc-21.6-win64\bin\

protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/sample.proto

protoc -I=C:\Users\Don\Projects\Kafka --python_out=C:\Users\Don\Projects\Kafka
C:\Users\Don\Projects\Kafka\sample.proto

This generates sample_pb2.py

add to python script:

import sample_pb2

python C:\Users\Don\Projects\Kafka\kafka-consumer.py

send messages like this from producer prompt:

> {"a": 1, "b": 2}

https://stackoverflow.com/questions/69131693/how-to-convert-protobuf-readable-request-to-proto-message
https://medium.com/@nathantnorth/protocol-buffers-text-format-14e0584f70a5

protoc example:

> cd C:\Tools\pb\protoc-21.6-win64\bin

to create binary form of protobuf message:

> echo 'addresses { name: "Mike", email: "mike@mike.us" }' | protoc
> --encode=AddressBook addresses.proto > addressbook.bin

or

> C:\Tools\pb\protoc-21.6-win64\bin\protoc --encode=main.Example main.proto <
> gen_main.txt > gen_example.bin

my example:

sample.txt

a: 1

b: 2

> C:\Tools\pb\protoc-21.6-win64\bin\protoc --encode=sample.Sample sample.proto <
> sample.txt > sample.bin

then decode file on consumer side by running through protoc:

> cat addressbook.bin | protoc --decode=AddressBook addresses.proto

addressbook.bin addresses { name: "Mike" email: "mike@mike.us" }

can view bin file: hexdump -C gen_example.bin

and decode back: protoc --decode=main.Example main.proto < gen_example.bin

my example: C:\Tools\pb\protoc-21.6-win64\bin\protoc --decode=sample.Sample
sample.proto < sample.bin

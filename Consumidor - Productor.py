{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab708
\pard\pardeftab708\ri522\partightenfactor0

\f0\fs24 \cf0 import json, time\
from kafka import KafkaConsumer, KafkaProducer\
from kafka.errors import KafkaError\
from random import uniform\
\
consumer = KafkaConsumer(bootstrap_servers=[172.24.41.216:8081],\
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))\
consumer.subscribe(pattern='Disponibilidad')\
\
producer = KafkaProducer(bootstrap_servers=[172.24.41.216:8081], \
             value_serializer=lambda v: json.dumps(v).encode('utf-8'))\
\
temp_list1 = 'El parqueadero con nombre: '\
\
for message in consumer:\
\
    temp_list1+=(message.value[\'93nombre\'94])\
    temp_list1+=' tiene '\
    temp_list1+=(message.value[\'93disponibles\'94])\
    temp_list1+=' parqueaderos disponibles y tiene  '\
    temp_list1+=(message.value['place'] == "ocupadosClientesNidoo")\
    temp_list1+='  ocupados por clients nidoo en la hora: '\
    temp_list1+=(message.value['time'])\
\
      producer.send('clientes', \{'Mensaje':temp_list1\})\
      producer.flush()\
      temp_list1 = 'El parqueadero con nombre: '\
     \
}
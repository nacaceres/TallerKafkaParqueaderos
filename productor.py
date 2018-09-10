{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab708
\pard\pardeftab708\ri522\partightenfactor0

\f0\fs24 \cf0 import json, time\
from kafka import KafkaProducer\
from kafka.errors import KafkaError\
from random import uniform\
\
producer = KafkaProducer(bootstrap_servers=[172.24.41.216:8081], \
						 value_serializer=lambda v: json.dumps(v).encode('utf-8'))\
\
while True:\
	producer.send('Disponibilidad', \{'time': time.strftime("%X"), 'disponibles': 5 'ocupadosClientesNidoo': 8, 'nombre' : 'Tenquendama' \})\
	producer.flush()\
	time.sleep(5)\
}
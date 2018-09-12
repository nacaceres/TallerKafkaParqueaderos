import json, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from random import uniform

producer = KafkaProducer(bootstrap_servers=['172.24.41.216:8081'], 
						 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
	producer.send('Disponibilidad', {'time': time.strftime("%X"), 'disponibles': 5, 'ocupadosClientesNidoo': 8, 'nombre' : 'Tenquendama' })
	producer.flush()
	time.sleep(5)

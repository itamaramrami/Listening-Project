from kafka import KafkaProducer,KafkaConsumer
import json



class kafka:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"))

        self.consumer = KafkaConsumer(
                "moazin_data",
                bootstrap_servers='localhost:9092',
                auto_offset_reset='earliest', 
                enable_auto_commit=True,
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )


    def get_message(self):
        msgs = self.consumer
        return msgs















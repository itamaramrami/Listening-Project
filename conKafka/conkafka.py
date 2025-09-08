from kafka import KafkaProducer,KafkaConsumer
import json
from Loger_loges.loger import Logger_log


loger=Logger_log()

class kafka:
    def __init__(self):

        try:
            self.producer = KafkaProducer(
                bootstrap_servers="localhost:9092",
                value_serializer=lambda v: json.dumps(v).encode("utf-8"))
            loger.get_logger().info("producer connection succeeded")
        except Exception as e:
            print(f"producer connection failed: {e}")
            loger.get_logger().error(f"producer connection failed: {e}")
        try:
            self.consumer = KafkaConsumer(
                    "moazin_metadata",
                    bootstrap_servers='localhost:9092',
                    auto_offset_reset='earliest', 
                    enable_auto_commit=True,
                    value_deserializer=lambda x: json.loads(x.decode('utf-8')))
            loger.get_logger().info("Consumer connection succeeded")
        except Exception as e:
            print(f"Consumer connection failed: {e}")
            loger.get_logger().error(f"Consumer connection failed: {e}")

            

    def get_message(self):
        try:
            msgs = self.consumer
            loger.get_logger().info("get messag succeeded")
            return msgs
        except Exception as e:
            print(f"get messag failed: {e}")
            loger.get_logger().error(f"get messag failed: {e}")

            















# clickstream-consumer/app/consumer.py

from kafka import KafkaConsumer
from data_store.app.data_store import DataStore
from clickstream_processor import process_clickstream_data

def consume_clickstream_data():
    consumer = KafkaConsumer('clickstream_topic', bootstrap_servers='localhost:9092')
    data_store = DataStore()
    for message in consumer:
        clickstream_data = message.value
        processed_data = process_clickstream_data(clickstream_data)
        data_store.store_clickstream_data(processed_data)



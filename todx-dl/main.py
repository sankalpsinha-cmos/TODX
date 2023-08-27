import json
import os
import tomllib
import uuid
import time
from typing import Dict

from kafka import KafkaConsumer, KafkaProducer



def create_kafka_consumer(config: Dict) -> KafkaConsumer:
    consumer : KafkaConsumer = KafkaConsumer(
        config['topic_name'],
        bootstrap_servers=config['kafka_consumer']['bootstrap_servers'],
        auto_offset_reset=config['kafka_consumer']['auto_offset_reset'],
        group_id=config['kafka_consumer']['group_id'],
        enable_auto_commit=config['kafka_consumer']['enable_auto_commit'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )
    return consumer


def create_kafka_producer(config: Dict) -> KafkaProducer:
    producer : KafkaProducer = KafkaProducer(
        bootstrap_servers=config['kafka_producer']['bootstrap_servers'],
    )
    return producer

def load_kafka_config() -> Dict:
    with open(os.path.join('/shared', 'configs', 'kafka-config.toml'), 'rb') as kafka_config_file:
        kafka_config : Dict = tomllib.load(kafka_config_file)
    return kafka_config


def send_request(request_data : Dict | bytes, producer : KafkaProducer, kafka_config : Dict) -> bool:
    if isinstance(request_data, dict):
        request_data = json.dumps(request_data).encode('utf-8') 
    try:
        producer.send(kafka_config['topic_name'], request_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        producer.flush()
        producer.close()
        

def process_request(request_data : Dict) -> None:
    print(request_data)


def listen(kafka_consumer : KafkaConsumer, kafka_producer : KafkaProducer) -> None:
    print('DB-Handeller up and listening...')
    while True:
        for request_message in kafka_consumer:
            process_request(request_message)
            

def main() -> None:
    kafka_config : Dict = load_kafka_config()
    consumer : KafkaConsumer = create_kafka_consumer(kafka_config)
    producer : KafkaProducer = create_kafka_producer(kafka_config)

    for i in range(100):
        request_data = {'body':{
        'request_uuid': str(uuid.uuid4())}}
        print(i, flush=True)
        send_request(request_data, producer, kafka_config)
        time.sleep(5)
    producer.close()

if __name__ == '__main__':
    main()
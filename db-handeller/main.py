import json
import os
import tomllib
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


def process_request(request_data : Dict) -> None:
    print(request_data, flush=True)


def listen(kafka_consumer : KafkaConsumer, kafka_producer : KafkaProducer) -> None:
    print('DB-Handeller up and listening...')
    while True:
        for request_message in kafka_consumer:
            process_request(request_message)
            

def main() -> None:
    kafka_config : Dict = load_kafka_config()
    consumer : KafkaConsumer = create_kafka_consumer(kafka_config)
    producer : KafkaProducer = create_kafka_producer(kafka_config)
    listen(consumer, producer)


if __name__ == '__main__':
    main()
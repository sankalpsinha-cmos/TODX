import json
import os
import tomllib
from typing import Dict

from utils.messaging import load_kafka_config, create_kafka_consumer, create_kafka_producer, KafkaConsumer, KafkaProducer


def process_request(request_data : Dict) -> None:
    print(request_data)


def listen(kafka_consumer : KafkaConsumer, kafka_producer : KafkaProducer) -> None:
    print('TODX-DL up and listening...')
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

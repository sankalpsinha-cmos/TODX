import json
import os
import tomllib
from typing import Dict
from box import Box

from kafka import KafkaConsumer, KafkaProducer


def create_kafka_consumer(config: Box) -> KafkaConsumer:
    """
    Create a Kafka consumer using the provided configuration.

    Args:
        config (dict): Kafka configuration as a dictionary.

    Returns:
        kafka.KafkaConsumer: An instance of KafkaConsumer configured with the settings from the config.
    """
    consumer : KafkaConsumer = KafkaConsumer(
        config.topic_name,
        bootstrap_servers=config.kafka_consumer.bootstrap_servers,
        auto_offset_reset=config.kafka_consumer.auto_offset_reset,
        group_id=config.kafka_consumer.group_id,
        enable_auto_commit=config.kafka_consumer.enable_auto_commit,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    )
    return consumer


def create_kafka_producer(config: Box) -> KafkaProducer:
    """
    Create a Kafka producer using the provided configuration.

    Args:
        config (dict): Kafka configuration as a dictionary.
    
    Returns:
        KafkaProducer: A KafkaProducer instance ready for producing messages.
    """
    producer : KafkaProducer = KafkaProducer(
        bootstrap_servers=config.kafka_producer.bootstrap_servers,
    )
    return producer


def load_kafka_config() -> Box:
    """
    Load a TOML kafka config file and return its contents as a Box object.

    This function reads a TOML configuration file and parses its contents into a Box object.

    Args:
        config_file_path (str): Path to the TOML config file to be loaded.

    Returns:
        Box: A Box object containing the parsed contents of the TOML config file.

    Raises:
        FileNotFoundError: If the specified config file does not exist.
        toml.TomlDecodeError: If there is an issue decoding the TOML content.
    """
    kafka_config_file_path = os.path.join('/shared', 'configs', 'kafka-config.toml')
    if not os.path.exists(kafka_config_file_path):
        raise FileNotFoundError(f"Config file not found: {kafka_config_file_path}")
    try:
        with open(kafka_config_file_path, 'rb') as kafka_config_file:
            kafka_config : Dict = tomllib.load(kafka_config_file)
            kafka_config_box = Box(kafka_config)
            return kafka_config_box
    except tomllib.TOMLDecodeError as e:
        raise tomllib.TOMLDecodeError(f"Error decoding TOML file: {str(e)}")


def send_request(request_data : Dict | bytes, producer : KafkaProducer, kafka_config : Dict) -> bool:
    if isinstance(request_data, dict):
        request_data = json.dumps(request_data).encode('utf-8') 
    try:
        producer.send(kafka_config['topic_name'], request_data)
    except Exception as e:
        print(f"An error occurred: {e}")
        producer.flush()
        producer.close()


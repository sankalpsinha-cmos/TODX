import uuid
import time
from typing import Dict

from utils.messaging import load_kafka_config, create_kafka_consumer, create_kafka_producer, send_request, KafkaConsumer, KafkaProducer


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

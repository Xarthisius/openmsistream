# imports
from openmsistream.utilities.config import RUN_CONST
from openmsistream.kafka_wrapper.openmsistream_producer import OpenMSIStreamProducer
from openmsistream.kafka_wrapper.openmsistream_consumer import OpenMSIStreamConsumer
from openmsistream.kafka_wrapper.producer_group import ProducerGroup
from openmsistream.kafka_wrapper.consumer_group import ConsumerGroup
from config import TEST_CONST  # pylint: disable=import-error,wrong-import-order

# pylint: disable=import-error,wrong-import-order
from test_base_classes import TestWithLogger, TestWithEnvVars


class TestCreateOpenMSIStreamKafkaObjects(TestWithLogger, TestWithEnvVars):
    """
    Class for testing that objects in openmsistream.kafka_wrapper can
    be instantiated using default configs
    """

    def test_create_openmsistream_producer(self):
        """
        Create a producer from a config file
        """
        producer = OpenMSIStreamProducer.from_file(
            TEST_CONST.TEST_CFG_FILE_PATH, logger=self.logger
        )
        self.assertTrue(producer is not None)
        producer.close()

    def test_create_openmsistream_producer_encrypted(self):
        """
        Create an encrypted producer from a config file
        """
        producer = OpenMSIStreamProducer.from_file(
            TEST_CONST.TEST_CFG_FILE_PATH_ENC, logger=self.logger
        )
        self.assertTrue(producer is not None)
        producer.close()

    def test_create_openmsistream_consumer(self):
        """
        Create a consumer from a config file
        """
        consumer = OpenMSIStreamConsumer.from_file(
            TEST_CONST.TEST_CFG_FILE_PATH, logger=self.logger
        )
        self.assertTrue(consumer is not None)
        consumer.close()

    def test_create_openmsistream_consumer_encrypted(self):
        """
        Create a encrypted consumer from a config file
        """
        consumer = OpenMSIStreamConsumer.from_file(
            TEST_CONST.TEST_CFG_FILE_PATH_ENC_2, logger=self.logger
        )
        self.assertTrue(consumer is not None)
        consumer.close()

    def test_create_producer_group(self):
        """
        Create a producer group
        """
        prod_group = ProducerGroup(TEST_CONST.TEST_CFG_FILE_PATH, logger=self.logger)
        self.assertTrue(prod_group is not None)
        prod_group.close()

    def test_create_producer_group_encrypted(self):
        """
        Create an encrypted producer group
        """
        prod_group = ProducerGroup(TEST_CONST.TEST_CFG_FILE_PATH_ENC, logger=self.logger)
        self.assertTrue(prod_group is not None)
        prod_group.close()

    def test_create_consumer_group_kafka(self):
        """
        Create a consumer group
        """
        con_group = ConsumerGroup(
            TEST_CONST.TEST_CFG_FILE_PATH,
            RUN_CONST.DEFAULT_TOPIC_NAME,
            consumer_group_id=f"test_create_consumer_group_{TEST_CONST.PY_VERSION}",
            logger=self.logger,
        )
        self.assertTrue(con_group is not None)
        con_group.close()

    def test_create_consumer_group_encrypted_kafka(self):
        """
        Create an encrypted consumer group
        """
        con_group = ConsumerGroup(
            TEST_CONST.TEST_CFG_FILE_PATH_ENC_2,
            RUN_CONST.DEFAULT_TOPIC_NAME,
            consumer_group_id=f"test_create_consumer_group_encrypted_{TEST_CONST.PY_VERSION}",
            logger=self.logger,
        )
        self.assertTrue(con_group is not None)
        con_group.close()

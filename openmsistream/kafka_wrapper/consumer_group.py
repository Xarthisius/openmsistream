#imports
from ..utilities import LogOwner
from .openmsistream_consumer import OpenMSIStreamConsumer

class ConsumerGroup(LogOwner) :
    """
    Class for working with a group of consumers sharing a single :class:`kafkacrypto.KafkaCrypto` instance

    :param config_path: Path to the config file that should be used to define Consumers in the group
    :type config_path: :class:`pathlib.Path`
    :param topic_name: The name of the topic to which the Consumers should be subscribed
    :type topic_name: str
    :param consumer_group_ID: The ID string that should be used for each Consumer in the group. 
        "create_new" will create a new UID to use.
    :type consumer_group_ID: str
    """

    @property
    def topic_name(self) :
        return self.__topic_name

    def __init__(self,config_path,topic_name,*,consumer_group_ID='create_new',**kwargs) :
        """
        arguments:
        config_path = path to the config file that should be used to define the consumer group
        topic_name  = name of the topic to consume messages from

        keyword arguments:
        consumer_group_ID = ID to use for all consumers in the group (a new & unique ID is created by default)
        """
        super().__init__(**kwargs)
        
        from confluent_kafka.admin import AdminClient
        from .config_file_parser import KafkaConfigFileParser
        cfp = KafkaConfigFileParser(config_path)
        admin_client = AdminClient(cfp.broker_configs)
        cluster_metadata = admin_client.list_topics(topic=topic_name)
        n_partitions = len(cluster_metadata.topics[topic_name].partitions)
        import kafka
        kac_kwargs = {}
        for k,v in cfp.broker_configs.items() :
            if k in ('sasl.username','sasl.password') :
                key = k.replace('.','_plain_')
            else :
                key = k.replace('.','_')
            kac_kwargs[key]=v
        kac = kafka.KafkaAdminClient(**kac_kwargs)
        parts = [kafka.TopicPartition(topic_name,pi) for pi in range(n_partitions)]
        tp_offsets=kac.list_consumer_group_offsets(group_id=consumer_group_ID,partitions=parts)
        for tp,om in tp_offsets.items() :
            print(f'{consumer_group_ID} GROUP OFFSET FOR {tp.topic} PARTITION {tp.partition} = {om.offset}')
        
        
        
        self.__topic_name = topic_name
        self.__c_args, self.__c_kwargs = OpenMSIStreamConsumer.get_consumer_args_kwargs(config_path,
                                                                                        group_id=consumer_group_ID,
                                                                                        logger=self.logger)

    def get_new_subscribed_consumer(self) :
        """
        Return a new Consumer, subscribed to the topic and with the shared group ID.
        Call this function from a child thread to get thread-independent Consumers.

        Note: This function just creates and subscribes the Consumer. Polling it, closing 
        it, and everything else must be handled by whatever calls this function.

        :return: a Consumer created using the configs set in the constructor, subscribed to the topic
        :rtype: :class:`~OpenMSIStreamConsumer`
        """
        consumer = OpenMSIStreamConsumer(*self.__c_args,**self.__c_kwargs)
        consumer.subscribe([self.__topic_name])
        return consumer

    def close(self) :
        """
        Wrapper around :func:`kafkacrypto.KafkaCrypto.close`. 
        """
        try :
            self.__c_kwargs['kafkacrypto'].close()
        except :
            pass
        finally :
            self.__c_kwargs['kafkacrypto'] = None

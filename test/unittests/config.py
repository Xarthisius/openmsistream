#imports
import os, pathlib
from openmsistream.utilities.config import RUN_CONST
from openmsistream.data_file_io.config import RUN_OPT_CONST

class TestRoutineConstants :
    """
    constants used in running tests
    """
    
    #names of topics on the test cluster to use for each test
    TEST_TOPIC_NAMES = {
            'test_data_file_directories':'test_data_file_directories',
            'test_data_file_directories_encrypted':'test_oms_encrypted',
            'test_data_file_stream_processor_kafka':'test_data_file_stream_processor',
            'test_data_file_stream_processor_restart_kafka':'test_data_file_stream_processor_2',
            'test_data_file_stream_processor_restart_encrypted_kafka':'test_data_file_stream_processor_encrypted',
            'test_s3_transfer_stream_processor':'test_s3_transfer_stream_processor',
            'test_serialization':'test_oms_encrypted',
            'test_metadata_reproducer':'test_metadata_extractor',
        }

    #Paths to locations inside the code base
    TEST_DIR_PATH = (pathlib.Path(__file__).parent.parent).resolve()
    PACKAGE_ROOT_DIR = TEST_DIR_PATH.parent / 'openmsistream'
    TEST_DATA_DIR_PATH = TEST_DIR_PATH / 'data'
    
    #S3 connection information
    TEST_ENDPOINT_URL = os.environ['ENDPOINT_URL'] # the endpoint_url for s3 bucket connection
    TEST_BUCKET_NAME = os.environ['BUCKET_NAME'] # the bucket name to upload data to (S3Client)
    TEST_ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID'] # the access_key_id for s3 Authentication
    TEST_SECRET_KEY_ID = os.environ['SECRET_KEY_ID'] # the secret_key_id for s3 Authentication
    TEST_REGION = os.environ['REGION'] # the region for the testing s3 bucket

    #different config files used in tests
    TEST_CONFIG_FILE_PATH = RUN_CONST.CONFIG_FILE_DIR/f'{RUN_OPT_CONST.DEFAULT_CONFIG_FILE}{RUN_CONST.CONFIG_FILE_EXT}'
    # Same as above except it includes a node_id to test encryption
    TEST_CONFIG_FILE_PATH_ENCRYPTED = TEST_CONFIG_FILE_PATH.with_stem('test_encrypted')
    TEST_CONFIG_FILE_PATH_ENCRYPTED_2 = TEST_CONFIG_FILE_PATH.with_stem('test_encrypted_2')
    # Same as above except it includes S3 transfer configs
    TEST_CONFIG_FILE_PATH_S3_TRANSFER = TEST_CONFIG_FILE_PATH.with_stem('test_s3_transfer')
    # The path to the "prod" Kafka config file to use in making sure that the prod environment variables are not set
    PROD_CONFIG_FILE_PATH = TEST_CONFIG_FILE_PATH.with_stem('prod')
    FAKE_PROD_CONFIG_FILE_PATH = TEST_DATA_DIR_PATH/f'fake_prod{RUN_CONST.CONFIG_FILE_EXT}'
    #the config file to use for the final consumer in the metadata reproducer test
    TEST_CONFIG_FILE_PATH_METADATA_CONSUMER = TEST_CONFIG_FILE_PATH.with_stem('test_metadata_reproducer_consumer')

    #Names of and paths to directories and files used in testing
    TEST_DATA_FILE_ROOT_DIR_NAME = 'test_file_root_dir'
    TEST_DATA_FILE_SUB_DIR_NAME = 'test_file_sub_dir'
    TEST_DATA_FILE_NAME = '1a0ceb89-b5f0-45dc-9c12-63d3020e2217.dat'
    TEST_DATA_FILE_2_NAME = '4ceee043-0b99-4f49-8527-595d93ddc487.dat'
    TEST_DATA_FILE_ROOT_DIR_PATH = TEST_DATA_DIR_PATH / TEST_DATA_FILE_ROOT_DIR_NAME
    TEST_DATA_FILE_PATH = ( TEST_DATA_DIR_PATH / TEST_DATA_FILE_ROOT_DIR_NAME / 
                            TEST_DATA_FILE_SUB_DIR_NAME / TEST_DATA_FILE_NAME )
    TEST_DATA_FILE_2_PATH = TEST_DATA_DIR_PATH / TEST_DATA_FILE_2_NAME
    TEST_WATCHED_DIR_PATH = TEST_DIR_PATH / 'test_watched_dir'
    TEST_WATCHED_DIR_PATH_ENCRYPTED = TEST_DIR_PATH / 'test_watched_dir_encrypted'
    TEST_STREAM_PROC_WATCHED_DIR_PATH_ENCRYPTED = TEST_DIR_PATH / 'test_watched_dir_stream_processor_encrypted'
    TEST_WATCHED_DIR_PATH_S3_TRANSFER = TEST_DIR_PATH / 'test_watched_dir_s3_transfer'
    TEST_DIR_SERVICES_TEST = TEST_DIR_PATH / 'test_dir_services'
    TEST_DIR_CUSTOM_RUNNABLE_SERVICE_TEST = TEST_DIR_PATH / 'test_dir_custom_runnable_service'
    TEST_DIR_CUSTOM_SCRIPT_SERVICE_TEST = TEST_DIR_PATH / 'test_dir_custom_script_service'
    TEST_RECO_DIR_PATH = TEST_DIR_PATH / 'test_reco'
    TEST_RECO_DIR_PATH_ENCRYPTED = TEST_DIR_PATH / 'test_reco_encrypted'
    TEST_STREAM_PROCESSOR_OUTPUT_DIR = TEST_DIR_PATH / 'test_stream_processor'
    TEST_STREAM_PROCESSOR_OUTPUT_DIR_RESTART = TEST_DIR_PATH / 'test_stream_processor_restart'
    TEST_STREAM_PROCESSOR_OUTPUT_DIR_RESTART_ENCRYPTED = TEST_DIR_PATH / 'test_stream_processor_restart_encrypted'
    TEST_S3_TRANSFER_STREAM_PROCESSOR_OUTPUT_DIR = TEST_DIR_PATH / 'test_s3_transfer_stream_processor_output_dir'
    TEST_METADATA_REPRODUCER_OUTPUT_DIR = TEST_DIR_PATH / 'test_metadata_reproducer_output_dir'
    TEST_METADATA_DICT_PICKLE_FILE = TEST_DATA_DIR_PATH / 'test_metadata_dict.pickle'
    
    # size (in bytes) of chunks to use in tests
    TEST_CHUNK_SIZE = 16384 
    
TEST_CONST=TestRoutineConstants()
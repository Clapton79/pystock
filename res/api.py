
from datetime import datetime
import yaml_handler as y
import requests
import itertools
import tools
import json
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(filename = 'log/main.log', level = logging.DEBUG)
logging.Formatter(LOG_FORMAT, TIME_FORMAT)

logger = logging.getLogger()

logging.getLogger("requests").setLevel(logging.CRITICAL)


def load_config(name, filename, reindex = True):
    """
    loads a configuration file then filters for the given configuration by the api_name
    all yaml configuration files have to have a unique name property
    """
    config = y.yaml_load('config/'+ filename +'.yaml')
    if reindex==1:
        config = tools.reindex_with_name(config)
    config = config[name]
    return config

class ApiService():
    def __init__(self,service_name):
        self.name = service_name
        self.status = 'Initializing'
        logger.debug('Initializing {0}'.format(service_name))
        self.data = ''
        self.error_message =''

        service_config = load_config(service_name, 'service', True)
        self.data_content_meta_key = service_config['data_content_meta_key']
        self.api = service_config['api']
        self.data_folder = service_config['data_folder']
        api_config = load_config(self.api, 'api')
        srv_fn_cols = service_config['functions']
        api_args = tools.concat_dict_list_recursive(srv_fn_cols)
        srv_fn_cols = tools.web_concat_dict_list(srv_fn_cols)
        self.request = api_config['url'] + api_config['query_tag'] + srv_fn_cols
        self.request_status = 0
        self.function = api_args['function']
        self.symbol = api_args['symbol']

        self.status = 'Initialized'
        logger.debug('{0} intialized.'.format(service_name))

    def Run(self):
        if (self.status)=='Initialized':
            self.status = 'Running'

            response = requests.get(self.request)
            response_json = response.json()
            self.request_status = response.status_code

            if 'Error Message' in response_json:
                self.status = 'Error'
                self.error_message = response_json['Error Message']
            else:
                self.status = 'Completed'
                self.data = response_json
        else:
            raise Exception('Service was not initialized successfully.')



service_name = 'Service 1'

c = ApiService(service_name)
c.Run()

print(c.request)

#c.Savedata()

#c = ApiService('Service 1')

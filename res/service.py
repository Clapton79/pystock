import tools
import threading
import api
import yaml_handler as y


config_loaded = False
config ={}


def init():
    global config
    global config_loaded
    if config_loaded==False:
        config = load_config()
        config = tools.concat_dict_list_recursive(config)
        config_loaded=True

def load_config ():
    print("loading service config")
    config =  y.yaml_load('config/service.yaml')
    return config

class ServiceRunner():
    def __init__(self, service_name):
        self.status = 'New'
        self.service_name = service_name
        self.api = config[service_name]['api']
        self.function = config[service_name]['functions']['function']
        self.symbols = config[service_name]['functions']['symbol']
        self.max_threads = config[service_name]['max_threads']
        self.api_key = config[service_name]['apikey']

"""
k = ServiceRunner('Service 1')
print (k.status)
print (k.service_name)
print (k.api)
print (k.function)
print (k.symbols)
print (k.max_trheads)
print (k.apikey)
"""

init()
config = load_config()
print (config)
k = ServiceRunner('Service 1')
 

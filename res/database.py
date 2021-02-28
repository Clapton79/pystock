import os
import yaml_handler as y
import pandas as pd
import api
import tools

"""
    1. dump data
    2. index data
    3. fileinfo data

"""

config_loaded = False
db_config ={}
db_init()

def db_init():
    global db_config
    global config_loaded
    if config_loaded==False:
        db_config = db_load_config()
        db_config = tools.concat_dict_list_recursive(db_config)
        config_loaded=True

def db_load_config ():
    db_config =  y.yaml_load('config/database.yaml')
    return db_config

def db_filename(function, symbol, profile):
    target_folder = db_config['profiles'][profile]['folder']
    filename = target_folder +'/'+ function + '_' + symbol

    return filename + '.dmp'


def db_update_database(stream, data_content_meta_key,function, symbol):

    data = stream[data_content_meta_key]

    file_name = db_filename(function, symbol, profile)
    print('opening {0} for update'.format(file_name))
    #load the files
    db_data = y.yaml_load(file_name)

    db_data.update(data)
    y.yaml_dump(file_name, db_data)


service_name = 'Service 1'
data_content_meta_key = 'Time Series (Daily)'

c = api.ApiService(service_name)
c.Run()


db_update_database(c.data,data_content_meta_key,'TIME_SERIES_DAILY', 'MSFT','profile1' )

#print(db_config)

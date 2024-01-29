"""
Created on 15-may-2017

@author: shrinivasan pulyadi
"""
import os.path
import yaml
import logging.config
logger = None


def setup_custom_logger():
    try:
        with open(os.path.join(os.getcwd(),'src', 'logging.yml'), 'r') as (f):
            config = yaml.safe_load(f.read())
        config.setdefault('version', 1)
        logging.config.dictConfig(config)
        logger = logging.getLogger('ml_logger')
        return logger
    except yaml.YAMLError as exc:
        print('Error in parsing logging file. Yaml Error - ', exc)
    except Exception as ex:
        print('Error in parsing logging file - ', ex)


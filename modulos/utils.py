from typing import List
from dataclasses import dataclass, field
import logging

def singleton(the_class):
    instances = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class

def raise_log(class_error: Exception, message_error: str, message_log: str='') -> None:
    class_name = class_error.__name__
    class_name = class_name.replace('Error', '')
    message_log = message_log if message_log else message_error
    logging.error(f'{class_name}: {message_log}')
    raise class_error(message_error)

def fix_register_values(register) -> List[str]:
    register = list(register)
    register[0] = str(register[0])
    return register

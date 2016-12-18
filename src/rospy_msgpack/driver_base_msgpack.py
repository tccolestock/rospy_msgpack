
"""
Privides a method to convert driver_base_msgs into serializable structures for
 msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

from rospy_msgpack import interpret


encode = interpret.Encode()
decode = interpret.Decode()


class Encode():
    def __init__(self):
        pass

    def config_string(cls, obj):
        msg = {}
        msg['name'] = obj.name
        msg['value'] = obj.value
        return(msg)

    def config_value(cls, obj):
        msg = {}
        msg['name'] = obj.name
        msg['value'] = obj.value
        return(msg)


class Decode():
    def __init__(self):
        pass

    def config_string(cls, msg, obj):
        obj.name = msg['name']
        obj.value = msg['value']
        return(obj)

    def config_value(cls, msg, obj):
        obj.name = msg['name']
        obj.value = msg['value']
        return(obj)

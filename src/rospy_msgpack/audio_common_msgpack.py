
"""
Privides a method to convert audio_common_msgs serializable structures for
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

    def audio_data(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)


class Decode():
    def __init__(self):
        pass

    def audio_data(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

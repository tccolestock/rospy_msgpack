
"""
Privides a method to convert controller_manager_msgs into serializable
 structures for msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

from rospy_msgpack import interpret
from controller_manager_msgs.msg import ControllerStatistics


encode = interpret.Encode()
decode = interpret.Decode()


class Encode():
    def __init__(self):
        pass

    def controller_state(cls, obj):
        msg = {}
        msg['name'] = obj.name
        msg['state'] = obj.state
        msg['type'] = obj.type
        msg['hardware_interface'] = obj.hardware_interface
        msg['resources'] = obj.resources
        return(msg)

    def controller_statistics(cls, obj):
        msg = {}
        s = encode.controller_statistics(obj, "")
        msg.update(s)
        return(msg)

    def controllers_statistics(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['_length'] = len(obj.controller)
        for i in range(msg['_length']):
            s = encode.controller_statistics(obj.controller[i], i)
            msg.update(s)
        return(msg)


class Decode():
    def __init__(self):
        pass

    def controller_state(cls, msg, obj):
        obj.name = msg['name']
        obj.state = msg['state']
        obj.type = msg['type']
        obj.hardware_interface = msg['hardware_interface']
        obj.resources = msg['resources']
        return(obj)

    def controller_statistics(cls, msg, obj):
        obj = decode.controller_statistics(msg, obj, "")
        return(obj)

    def controllers_statistics(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(msg['_length']):
            cs = ControllerStatistics()
            cs = decode.controller_statistics(msg, cs, i)
            obj.controller.append(cs)
        return(obj)


"""
Privides a method to convert diagnostic_msgs into serializable structures for
 msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"


from diagnostic_msgs.msg import KeyValue, DiagnosticStatus
from rospy_msgpack import interpret


class Encode():
    def __init__(self):
        pass

    def diagnostic_array(cls, obj):
        msg = {}
        h = interpret.Encode().header(obj.header, "")
        msg.update(h)
        msg['_length_s'] = len(obj.status)
        for i in range(msg['_length_s']):
            msg['%s_length_v' % i] = len(obj.status[i].values)
            for j in range(msg['%s_length_v' % i]):
                msg['%s_%s_key' % (i, j)] = obj.status[i].values[j].key
                msg['%s_%s_value' % (i, j)] = obj.status[i].values[j].value
        return(msg)

    def diagnostic_status(cls, obj):
        msg = {}
        msg['_length'] = len(obj.values)
        for i in range(msg['_length']):
            msg['%s_key' % i] = obj.values[i].key
            msg['%s_value' % i] = obj.values[i].value
        return(msg)

    def key_value(self, data):
        msg = {}
        msg['key'] = data.key
        msg['value'] = data.value
        return(msg)


class Decode():
    def __init__(self):
        pass

    def diagnostic_array(cls, msg, obj):
        obj.header = interpret.Decode().header(msg, obj.header, "")
        for i in range(msg['_length_s']):
            ds = DiagnosticStatus()
            for j in range(msg['%s_length_v' % i]):
                kv = KeyValue()
                kv.key = msg['%s_%s_key' % (i, j)]
                kv.value = msg['%s_%s_value' % (i, j)]
                ds.values.append(kv)
            obj.status.append(ds)
        return(obj)

    def diagnostic_status(cls, msg, obj):
        for i in range(msg['_length']):
            kv = KeyValue()
            kv.key = msg['%s_key' % i]
            kv.value = msg['%s_value' % i]
            obj.values.append(kv)
        return(obj)

    def key_value(self, msg, obj):
        obj.key = msg['key']
        obj.value = msg['value']
        return(obj)

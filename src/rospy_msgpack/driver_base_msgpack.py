
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

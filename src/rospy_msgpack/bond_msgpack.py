
from rospy_msgpack import interpret

encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def status(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['id'] = obj.id
        msg['instance_id'] = obj.instance_id
        msg['active'] = obj.active
        msg['heartbeat_timeout'] = obj.heartbeat_timeout
        msg['heartbeat_period'] = obj.heartbeat_period
        return(msg)

class Decode():
    def __init__(self):
        pass

    def status(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.id = msg['id']
        obj.instance_id = msg['instance_id']
        obj.active = msg['active']
        obj.heartbeat_timeout = msg['heartbeat_timeout']
        obj.heartbeat_period = msg['heartbeat_period']
        return(obj)

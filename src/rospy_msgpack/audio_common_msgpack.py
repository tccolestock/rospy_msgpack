
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

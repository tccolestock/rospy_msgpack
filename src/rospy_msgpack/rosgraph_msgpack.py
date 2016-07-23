
from rospy_msgpack import interpret

encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def clock(cls, obj):
        msg = {}
        msg['clock'] = obj.clock
        return(msg)

    def log(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['level'] = obj.level
        msg['name'] = obj.name
        msg['msg'] = obj.msg
        msg['file'] = obj.file
        msg['function'] = obj.function
        msg['line'] = obj.line
        msg['topics'] = obj.topics
        return(msg)

    def topic_statistics(cls, obj):
        msg = {}
        msg['topic'] = obj.topic
        msg['node_pub'] = obj.node_pub
        msg['node_sub'] = obj.node_sub
        msg['window_start'] = obj.window_start
        msg['window_stop'] = obj.window_stop
        msg['delivered_msgs'] = obj.delivered_msgs
        msg['dropped_msgs'] = obj.dropped_msgs
        msg['traffic'] = obj.traffic
        msg['period_mean'] = obj.period_mean
        msg['period_stddev'] = obj.period_stddev
        msg['period_max'] = obj.period_max
        msg['stamp_age_mean'] = obj.stamp_age_mean
        msg['stamp_age_stddev'] = obj.stamp_age_stddev
        msg['stamp_age_max'] = obj.stamp_age_max
        return(msg)

class Decode():
    def __init__(self):
        pass

    def clock(cls, msg, obj):
        obj.clock = msg['clock']
        return(obj)

    def log(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.level = msg['level']
        obj.name = msg['name']
        obj.msg = msg['msg']
        obj.file = msg['file']
        obj.function = msg['function']
        obj.line = msg['line']
        obj.topics = msg['topics']
        return(obj)

    def topic_statistics(cls, msg, obj):
        obj.topic = msg['topic']
        obj.node_pub = msg['node_pub']
        obj.node_sub = msg['node_sub']
        obj.window_start = msg['window_start']
        obj.window_stop = msg['window_stop']
        obj.delivered_msgs = msg['delivered_msgs']
        obj.dropped_msgs = msg['dropped_msgs']
        obj.traffic = msg['traffic']
        obj.period_mean = msg['period_mean']
        obj.period_stddev = msg['period_stddev']
        obj.period_max = msg['period_max']
        obj.stamp_age_mean = msg['stamp_age_mean']
        obj.stamp_age_stddev = msg['stamp_age_stddev']
        obj.stamp_age_max = msg['stamp_age_max']
        return(obj)

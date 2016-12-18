
"""
Privides a method to convert actionlib_msgs into serializable structures for
 msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

from rospy_msgpack import interpret
from actionlib_msgs.msg import GoalID, GoalStatus


encode = interpret.Encode()
decode = interpret.Decode()


class Encode():
    def __init__(self):
        pass

    def goal_id(self, data):
        msg = {}
        msg['secs'] = data.stamp.secs
        msg['nsecs'] = data.stamp.nsecs
        msg['id'] = data.id
        return(msg)

    def goal_status(cls, obj):
        msg {}
        t = encode.time_stamp(obj.goal_id.stamp, "")
        msg['id'] = obj.goal_id.id
        msg['status'] = obj.status
        msg['text'] = obj.text
        msg.update(t)
        return(msg)

    def goal_status_array(cls, obj):
        msg = {}
        e_time = encode.time_stamp
        h = encode.header(obj.header, "")
        msg['_length'] = len(obj.status_list)
        for i in range(msg['_length']):
            t = e_time(obj.status_list[i].goal_id.stamp, i)
            msg['%s_id' % i] = obj.status_list[i].goal_id.id
            msg['%s_status' % i] = obj.status_list[i].status
            msg['%s_text' % i] = obj.status_list[i].text
            msg.update(t)
        msg.update(h)
        return(msg)


class Decode():
    def __init__(self):
        pass

    def goal_id(self, msg, obj):
        obj.stamp.secs = msg['secs']
        obj.stamp.nsecs = msg['nsecs']
        obj.id = msg['id']
        return(obj)

    def goal_status(cls, msg, obj):
        obj.goal_id.stamp = decode.time_stamp(msg, obj.goal_id.stamp, "")
        obj.goal_id.id = msg['id']
        obj.status = msg['status']
        obj.text = msg['text']
        return(obj)

    def goal_status_array(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(msg['_length']):
            goal_status = GoalStatus()
            goal_status.goal_id.stamp = decode.time_stamp(msg,
                                                          goal_id.stamp, i)
            goal_status.goal_id.id = msg['%s_id' % i]
            goal_status.status = msg['%s_status' % i]
            goal_status.text = msg['%s_text' % i]
            obj.status_list.append(goal_status)
        return(obj)


"""
Privides a method to convert octomap_msgs into serializable structures for
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

    def octomap(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['binary'] = obj.binary
        msg['id'] = obj.id
        msg['resolution'] = obj.resolution
        msg['data'] = obj.data
        return(msg)

    def octomap_with_pose(cls, obj):
        msg = {}
        h = encode.header(obj.header, "top")
        msg.update(h)
        p = encode.position(obj.origin.position, "")
        o = encode.orientation(obj.origin.orientation, "")
        msg.update(p)
        msg.update(o)
        h2 = encode.header(obj.octomap.header, "nest")
        msg['binary'] = obj.octomap.binary
        msg['id'] = obj.octomap.id
        msg['resolution'] = obj.octomap.resolution
        msg['data'] = obj.octomap.data
        return(msg)


class Decode():
    def __init__(self):
        pass

    def octomap(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.binary = msg['binary']
        obj.id = msg['id']
        obj.resolution = msg['resolution']
        obj.data = msg['data']
        return(obj)

    def octomap_with_pose(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "top")
        obj.origin.position = decode.position(msg, obj.origin.position, "")
        obj.origin.orientation = \
            decode.orientation(msg, obj.origin.orientation, "")
        obj.octomap.header = decode.header(msg, obj.octomap.header, "nest")
        obj.octomap.binary = msg['binary']
        obj.octomap.id = msg['id']
        obj.octomap.resolution = msg['resolution']
        obj.octomap.data = msg['data']
        return(obj)

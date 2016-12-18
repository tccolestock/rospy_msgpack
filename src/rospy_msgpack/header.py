
"""
Privides a method to convert header_msgs into serializable structures for
 msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"


class Header():
    def encode(self, obj, i):
        h = {}
        h['%sseq' % i] = obj.header.seq
        h['%ssecs' % i] = obj.header.stamp.secs
        h['%snsecs' % i] = obj.header.stamp.nsecs
        h['%sframe_id' % i] = obj.header.frame_id
        return(h)

    def decode(self, msg, obj, i):
        obj.header.seq = msg['%sseq' % i]
        obj.header.stamp.secs = msg['%ssecs' % i]
        obj.header.stamp.nsecs = msg['%snsecs' % i]
        obj.header.frame_id = msg['%sframe_id' % i]
        return(obj)

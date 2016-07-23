
from rospy_msgpack import interpret
from geometry_msgs.msg import Point, PoseStamped, Pose, Quaternion
from std_msgs.msg import Header

encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def grid_cells(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['cell_width'] = obj.cell_width
        msg['cell_height'] = obj.cell_height
        msg['_length'] = len(obj.cells)
        for i in range(msg['_length']):
            c = encode.xyz(obj.cells[i], i, "cells")
            msg.update(c)
        msg.update(h)
        return(msg)

    def map_meta_data(cls, obj):
        msg = {}
        msg['map_load_time'] = obj.map_load_time
        msg['resolution'] = obj.resolution
        msg['width'] = obj.width
        msg['height'] = obj.height
        p = encode.position(obj.origin.position, "")
        o = encode.orientation(obj.origin.orientation, "")
        msg.update(p)
        msg.update(o)
        return(msg)

    def occupancy_grid(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['map_load_time'] = obj.info.map_load_time
        msg['resolution'] = obj.info.resolution
        msg['width'] = obj.info.width
        msg['height'] = obj.info.height
        p = encode.position(obj.info.origin.position, "")
        o = encode.orientation(obj.info.origin.orientation, "")
        msg['data'] = obj.data
        msg.update(h)
        msg.update(p)
        msg.update(o)
        return(msg)

    def odometry(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['child_frame_id'] = obj.child_frame_id
        p = encode.position(obj.pose.pose.position, "")
        o = encode.orientation(obj.pose.pose.orientation, "")
        pc = encode.covariance(obj.pose, "pose")
        l = encode.linear(obj.twist.twist.linear, "")
        a = encode.angular(obj.twist.twist.angular, "")
        tc = encode.covariance(obj.twist, "twist")
        msg.update(h)
        msg.update(p)
        msg.update(o)
        msg.update(pc)
        msg.update(l)
        msg.update(a)
        msg.update(tc)
        return(msg)

    def path(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['_length'] = len(obj.poses)
        for i in range(msg['_length']):
            h2 = encode.header(obj.poses[i].header, i)
            p = encode.position(obj.poses[i].pose.position, i)
            o = encode.orientation(obj.poses[i].pose.orientation, i)
            msg.update(h2)
            msg.update(p)
            msg.update(o)
        msg.update(h)
        return(msg)

#=================================================================================

class Decode():
    def __init__(self):
        pass

    def grid_cells(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.cell_width = msg['cell_width']
        obj.cell_height = msg['cell_height']
        for i in range(msg['_length']):
            cell = Point()
            cell = decode.xyz(msg, cell, i, "cells")
            obj.cells.append(cell)
        return(obj)

    def map_meta_data(cls, msg, obj):
        obj.map_load_time = msg['map_load_time']
        obj.resolution = msg['resolution']
        obj.width = msg['width']
        obj.height = msg['height']
        obj.origin.position = decode.position(msg, obj.origin.position, "")
        obj.origin.orientation = decode.orientation(msg, obj.origin.orientation, "")
        return(obj)

    def occupancy_grid(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.info.map_load_time = msg['map_load_time']
        obj.info.resolution = msg['resolution']
        obj.info.width = msg['width']
        obj.info.height = msg['height']
        obj.info.origin.position = decode.position(msg, obj.info.origin.position, "")
        obj.info.origin.orientation = decode.orientation(msg, obj.info.origin.orientation, "")
        obj.data = msg['data']
        return(obj)

    def odometry(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.child_frame_id = msg['child_frame_id']
        obj.pose.pose.position = decode.position(msg, obj.pose.pose.position, "")
        obj.pose.pose.orientation = decode.orientation(msg, obj.pose.pose.orientation, "")
        obj.pose = decode.covariance(msg, obj.pose, "pose")
        obj.twist.twist.linear = decode.linear(msg, obj.twist.twist.linear, "")
        obj.twist.twist.angular = decode.angular(msg, obj.twist.twist.angular, "")
        obj.twist = decode.covariance(msg, obj.twist, "twist")
        return(obj)

    def path(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(msg['_length']):
            ps = PoseStamped()
            ps.header = decode.header(msg, ps.header, i)
            ps.pose.position = decode.position(msg, ps.pose.position, i)
            ps.pose.orientation = decode.orientation(msg, ps.pose.orientation, i)
            obj.poses.append(ps)
        return(obj)

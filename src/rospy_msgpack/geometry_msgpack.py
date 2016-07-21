
# import rospy
from rospy_msgpack import interpret
# from roslib import geometry_msgs #import *
 # std_msgs.msg
# import roslib ; roslib.load_manifest('geometry_msgs')
import geometry_msgs.msg

encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def accel(cls, obj):
        msg = {}
        lin = encode.linear(obj.linear, "")
        ang = encode.angular(obj.angular, "")
        msg.update(lin)
        msg.update(ang)
        return(msg)

    def accel_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        lin = encode.linear(obj.accel.linear, "")
        ang = encode.angular(obj.accel.angular, "")
        msg.update(h)
        msg.update(lin)
        msg.update(ang)
        return(msg)

    def accel_with_covariance(cls, obj):
        msg = {}
        lin = encode.linear(obj.accel.linear, "")
        ang = encode.angular(obj.accel.angular, "")
        covar = encode.covariance(obj, "")
        msg.update(lin)
        msg.update(ang)
        msg.update(covar)
        return(msg)

    def accel_with_covariance_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        lin = encode.linear(obj.accel.accel.linear, "")
        ang = encode.angular(obj.accel.accel.angular, "")
        covar = encode.covariance(obj.accel, "")
        msg.update(h)
        msg.update(lin)
        msg.update(ang)
        msg.update(covar)
        return(msg)

    def inertia(cls, obj):
        msg = {}
        msg['m'] = obj.m
        c = encode.com(obj.com, "")
        i = encode.inertia(obj, "")
        msg.update(c)
        msg.update(i)
        return(msg)

    def inertia_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['m'] = obj.inertia.m
        c = encode.com(obj.inertia.com, "")
        i = encode.inertia(obj.inertia, "")
        msg.update(h)
        msg.update(c)
        msg.update(i)
        return(msg)

    def point(cls, obj):
        msg = {}
        p = encode.point(obj, "")
        msg.update(p)
        return(msg)

    def point32(cls, obj):
        msg = cls.point(obj)
        return(msg)

    def point_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        p = encode.point(obj.point, "")
        msg.update(h)
        msg.update(p)
        return(msg)

    def polygon(cls, obj):
        msg = {}
        obj_points = obj.points
        e_point = encode.point
        msg['_length'] = len(obj.points)
        for i in range(msg['_length']):
            p = e_point(obj_points[i], i)
            msg.update(p)
        return(msg)

    def polygon_stamped(cls, obj):
        msg = {}
        msg['_length'] = len(obj.polygon.points)
        obj_poly_points = obj.polygon.points
        e_point = encode.point
        h = encode.header(obj.header, "")
        for i in range(msg['_length']):
            p = e_point(obj_poly_points[i], i)
            msg.update(p)
        msg.update(h)
        return(msg)

    def pose(cls, obj):
        msg = {}
        pos = encode.position(obj.position, "")
        orient = encode.orientation(obj.orientation, "")
        msg.update(pos)
        msg.update(orient)
        return(msg)

    def pose_2d(cls, obj):
        msg = {}
        msg['x'] = obj.x
        msg['y'] = obj.y
        msg['theta'] = obj.theta
        return(msg)

    def pose_array(cls, obj):
        msg = {}
        obj_poses = obj.poses
        e_pos = encode.position
        e_orient = encode.orientation
        msg['_length'] = len(obj.poses)
        h = encode.header(obj.header, "")
        for i in range(msg['_length']):
            p = e_pos(obj_poses[i].position, i)
            o = e_orient(obj_poses[i].orientation, i)
            msg.update(p)
            msg.update(o)
        msg.update(h)
        return(msg)

    def pose_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        p = encode.position(obj.pose.position, "")
        o = encode.orientation(obj.pose.orientation, "")
        msg.update(h)
        msg.update(p)
        msg.update(o)
        return(msg)

    def pose_with_covariance(cls, obj):
        msg = {}
        p = encode.position(obj.pose.position, "")
        o = encode.orientation(obj.pose.orientation, "")
        c = encode.covariance(obj, "")
        msg.update(p)
        msg.update(o)
        msg.update(c)
        return(msg)

    def pose_with_covariance_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        p = encode.position(obj.pose.pose.position, "")
        o = encode.orientation(obj.pose.pose.orientation, "")
        c = encode.covariance(obj.pose, "")
        msg.update(h)
        msg.update(p)
        msg.update(o)
        msg.update(c)
        return(msg)

    def quaternion(cls, obj):
        msg = {}
        q = encode.quaternion(obj, "")
        msg.update(q)
        return(msg)

    def quaternion_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        q = encode.quaternion(obj.quaternion, "")
        msg.update(h)
        msg.update(q)
        return(msg)

    def transform(cls, obj):
        msg = {}
        t = encode.translation(obj.translation, "")
        r = encode.rotation(obj.rotation, "")
        msg.update(t)
        msg.update(r)
        return(msg)

    def transform_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['child_frame_id'] = obj.child_frame_id
        t = encode.translation(obj.transform.translation, "")
        r = encode.rotation(obj.transform.rotation, "")
        msg.update(h)
        msg.update(t)
        msg.update(r)
        return(msg)

    def twist(self, obj):
        msg = {}
        lin = encode.linear(obj.linear, "")
        ang = encode.angular(obj.angular, "")
        msg.update(lin)
        msg.update(ang)
        return(msg)


    def twist_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.linear(obj.twist.linear, "")
        a = encode.angular(obj.twist.angular, "")
        msg.update(h)
        msg.update(l)
        msg.update(a)
        return(msg)

    def twist_with_covariance(cls, obj):
        msg = {}
        l = encode.linear(obj.twist.linear, "")
        a = encode.angular(obj.twist.angular, "")
        c = encode.covariance(obj.twist, "")
        msg.update(l)
        msg.update(a)
        msg.update(c)
        return(msg)

    def twist_with_covariance_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.linear(obj.twist.twist.linear, "")
        a = encode.angular(obj.twist.twist.angular, "")
        c = encode.covariance(obj.twist, "")
        msg.update(h)
        msg.update(l)
        msg.update(a)
        msg.update(c)
        return(msg)

    def vector3(cls, obj):
        msg = {}
        v = encode.vector(obj, "")
        msg.update(v)
        return(msg)

    def vector3_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        v = encode.vector(obj.vector, "")
        msg.update(h)
        msg.update(v)
        return(msg)

    def wrench(cls, obj):
        msg = {}
        f = encode.force(obj.force, "")
        t = encode.torque(obj.torque, "")
        msg.update(f)
        msg.update(t)
        return(msg)

    def wrench_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        f = encode.force(obj.wrench.force, "")
        t = encode.torque(obj.wrench.torque, "")
        msg.update(h)
        msg.update(f)
        msg.update(t)
        return(msg)

#=======================================================================================

class Decode():
    def __init__(self):
        pass

    def accel(cls, msg, obj):
        obj.linear = decode.linear(msg, obj.linear, "")
        obj.angular = decode.angular(msg, obj.angular, "")
        return(obj)

    def accel_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.linear = decode.linear(msg, obj.linear, "")
        obj.angular = decode.angular(msg, obj.angular, "")
        return(obj)

    def accel_with_covariance(cls, msg, obj):
        obj.accel.linear = decode.linear(msg, obj.accel.linear, "")
        obj.accel.angular = decode.angular(msg, obj.accel.angular, "")
        obj = decode.covariance(msg, obj, "")
        return(obj)

    def accel_with_covariance_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.accel.accel.linear = decode.linear(msg, obj.accel.accel.linear, "")
        obj.accel.accel.angular = decode.angular(msg, obj.accel.accel.angular, "")
        obj.accel = decode.covariance(msg, obj.accel, "")
        return(obj)

    def inertia(cls, msg, obj):
        obj.m = msg['m']
        obj.com = decode.com(msg, obj.com, "")
        obj = decode.inertia(msg, obj, "")
        return(obj)

    def inertia_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.inertia.m = msg['m']
        obj.inertia.com = decode.com(msg, obj.inertia.com, "")
        obj.inertia = decode.inertia(msg, obj.inertia, "")
        return(obj)

    def point(cls, msg, obj):
        obj = decode.point(msg, obj, "")
        return(obj)

    def point32(cls, msg, obj):
        obj = cls.point(msg, obj)
        return(obj)

    def point_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.point = decode.point(msg, obj.point, "")
        return(obj)

    def polygon(cls, msg, obj):
        obj_points_append = obj.points.append
        decode_point = decode.point
        point32 = geometry_msgs.msg.Point32
        for i in range(msg['_length']):
            pnt = point32()
            obj_points_append(decode_point(msg, pnt, i))
        return(obj)

    def polygon_stamped(cls, msg, obj):
        obj_poly_points_app = obj.polygon.points.append
        d_point = decode.point
        point32 = geometry_msgs.msg.Point32
        obj.header = decode.header(msg, obj.header, "")
        for i in range(msg['_length']):
            pnt = point32()
            obj_poly_points_app(d_point(msg, pnt, i))
        return(obj)

    def pose(cls, msg, obj):
        obj.position = decode.position(msg, obj.position, "")
        obj.orientation = decode.orientation(msg, obj.orientation, "")
        return(obj)

    def pose_2d(cls, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.theta = msg['theta']
        return(obj)

    def pose_array(cls, msg, obj):
        obj_poses_app = obj.poses.append
        pose = geometry_msgs.msg.Pose
        pos = geometry_msgs.msg.Point
        orient = geometry_msgs.msg.Quaternion
        d_pos = decode.position
        d_orient = decode.orientation
        obj.header = decode.header(msg, obj.header, "")
        position = pos()
        orientation = orient()
        for i in range(['_length']):
            pose1 = pose()
            pose1.position = d_pos(msg, position, i)
            pose1.orientation = d_orient(msg, orientation, i)
            obj_poses_app(pose1)
        return(obj)

    def pose_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.poses.position = decode.position(msg, obj.pose.position, "")
        obj.poses.orientation = decode.orientation(msg, obj.pose.orientation, "")
        return(obj)

    def pose_with_covariance(cls, msg, obj):
        obj.pose.position = decode.position(msg, obj.pose.position, "")
        obj.pose.orientation = decode.orientation(msg, obj.pose.orientation, "")
        obj = decode.covariance(msg, obj, "")
        return(obj)

    def pose_with_covariance_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.pose.pose.position = decode.position(msg, obj.pose.pose.position, "")
        obj.pose.pose.orientation = decode.orientation(msg, obj.pose.pose.orientation, "")
        obj.pose = decode.covariance(msg, obj.pose, "")
        return(obj)

    def quaternion(cls, msg, obj):
        obj = decode.quaternion(msg, obj, "")
        return(obj)

    def quaternion_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.quaternion = decode.quaternion(msg, obj.quaternion, "")
        return(obj)

    def transform(cls, msg, obj):
        obj.translation = decode.translation(msg, obj.translation, "")
        obj.rotation = decode.rotation(msg, obj.rotation, "")
        return(obj)

    def transform_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.child_frame_id = msg['child_frame_id']
        obj.transform.translation = decode.translation(msg, obj.transform.translation, "")
        obj.transform.rotation = decode.rotation(msg, obj.transform.rotation, "")
        return(obj)

    def twist(self, msg, obj):
        obj.linear = decode.linear(msg, obj.linear, "")
        obj.angular = decode.angular(msg, obj.angular, "")
        return(obj)

    def twist_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.twist.linear = decode.linear(msg, obj.twist.linear, "")
        obj.twist.angular = decode.angular(msg, obj.twist.angular, "")
        return(obj)

    def twist_with_covariance(cls, msg, obj):
        obj.twist.linear = decode.linear(msg, obj.twist.linear, "")
        obj.twist.angular = decode.angular(msg, obj.twist.angular, "")
        obj.twist = decode.covariance(msg, obj.twist, "")
        return(obj)

    def twist_with_covariance_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.twist.twist.linear = decode.linear(msg, obj.twist.twist.linear, "")
        obj.twist.twist.angular = decode.angular(msg, obj.twist.twist.angular, "")
        obj.twist = decode.covariance(msg, obj.twist, "")
        return(obj)

    def vector3(cls, msg, obj):
        obj = decode.vector(msg, obj, "")
        return(obj)

    def vector3_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.vector = decode.vector(msg, obj.vector, "")
        return(obj)

    def wrench(cls, msg, obj):
        obj.force = decode.force(msg, obj.force, "")
        obj.torque = decode.torque(msg, obj.torque, "")
        return(obj)

    def wrench_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.wrench.force = decode.force(msg, obj.wrench.force, "")
        obj.wrench.torque = decode.torque(msg, obj.wrench.torque, "")
        return(obj)

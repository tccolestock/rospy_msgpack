
"""
Privides a method to convert trajectory_msgs into serializable structures for
 msgpack. For use with the ZeroMQ socket communication.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

from rospy_msgpack import interpret
from trajectory_msgs.msg import (JointTrajectoryPoint,
                                 MultiDOFJointTrajectoryPoint)
from geometry_msgs.msg import Transform, Twist


encode = interpret.Encode()
decode = interpret.Decode()


class Encode():
    def __init__(self):
        pass

    def joint_trajectory(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['joint_names'] = obj.joint_names
        msg['_length'] = len(obj.points)
        for i in range(msg['_length']):
            p = encode.grasp_points(obj.points[i], i)
            msg.update(p)
        msg.update(h)
        return(msg)

    def joint_trajectory_point(cls, obj):
        msg = {}
        p = encode.grasp_points(obj, "")
        msg.update(p)
        return(msg)

    def multi_dof_joint_trajectory(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['joint_names'] = obj.joint_names
        msg['_length_points'] = len(obj.points)
        for i in range(msg['_length_points']):
            msg['%s_length_trans' % i] = len(obj.points[i].transforms)
            for j in range(msg['%s_length_trans' % i]):
                tr = \
                    encode.translation(obj.points[i].transfroms[j].translation,
                                       "%s_%s" % (i, j))
                msg.update(tr)
                rot = encode.rotation(obj.points[i].transforms[j].rotation,
                                      "%s_%s" % (i, j))
                msg.update(rot)

            msg['%s_length_velo' % i] = len(obj.points[i].velocities)
            for j in range(msg['%s_length_velo' % i]):
                vl = encode.linear(obj.points[i].velocities[j].linear,
                                   "%s_%s_v" % (i, j))
                msg.update(vl)
                va = encode.angular(obj.points[i].velocities[j].angular,
                                    "%s_%s_v" % (i, j))
                msg.update(va)

            msg['%s_length_acc' % i] = len(obj.points[i].accelerations)
            for j in range(msg['%s_length_acc' % i]):
                al = encode.linear(obj.points[i].accelerations[j].linear,
                                   "%s_%s_a" % (i, j))
                msg.update(al)
                aa = encode.angular(obj.points[i].accelerations[j].angular,
                                    "%s_%s_a" % (i, j))
                msg.update(aa)

            msg['%s_time_from_start' % i] = obj.points[i].time_from_start
        return(msg)

    def multi_dof_joint_trajectory_point(cls, obj):
        msg['_length_trans'] = len(obj.transforms)
        for i in range(msg['_length_trans']):
            tr = encode.translation(obj.transfroms[i].translation, i)
            msg.update(tr)
            rot = encode.rotation(obj.transforms[i].rotation, i)
            msg.update(rot)

        msg['_length_velo'] = len(obj.velocities)
        for i in range(msg['length_velo']):
            vl = encode.linear(obj.velocities[i].linear, "%s_v" % i)
            msg.update(vl)
            va = encode.angular(obj.velocities[i].angular, "%s_v" % i)
            msg.update(va)

        msg['_length_acc'] = len(obj.accelerations)
        for i in range(msg['_length_acc']):
            al = encode.linear(obj.accelerations[i].linear, "%s_a" % i)
            msg.update(al)
            aa = encode.angular(obj.accelerations[i].angular, "%s_a" % i)
            msg.update(aa)

        msg['time_from_start'] = obj.time_from_start
    return(msg)


class Decode():
    def __init__(self):
        pass

    def joint_trajectory(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.joint_names = msg['joint_names']
        for i in range(msg['_length']):
            jtp = JointTrajectoryPoint()
            jtp = decode.grasp_points(msg, jtp, i)
            obj.points.append(jtp)
        return(obj)

    def joint_trajectory_point(cls, msg, obj):
        obj = decode.grasp_points(msg, obj, "")
        return(obj)

    def multi_dof_joint_trajectory(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.joint_names = msg['joint_names']
        for i in range(msg['_length_points']):
            mjtp = MultiDOFJointTrajectoryPoint()
            for j in range(msg['%s_length_trans' % i]):
                tr = Transform()
                tr.translation = decode.translation(msg, tr.translation,
                                                    "%s_%s" % (i, j))
                tr.rotation = \
                    decode.rotation(msg, tr.rotation, "%s_%s" % (i, j))
                mjtp.transforms.append(tr)

            for j in range(msg['%s_length_velo' % i]):
                v = Twist()
                v.linear = decode.linear(msg, v.linear, "%s_%s_v" % (i, j))
                v.angular = decode.angular(msg, v.angular, "%s_%s_v" % (i, j))
                mjtp.velocities.append(v)

            for j in range(msg['%s_length_acc' % i]):
                a = Twist()
                a.linear = decode.linear(msg, a.linear, "%s_%s_a" % (i, j))
                a.angular = decode.angular(msg, a.angular, "%s_%s_a" % (i, j))
                mjtp.accelerations.append(a)
            mjtp.time_from_start = msg['%s_time_from_start' % i]
            obj.points.append(mjtp)
        return(obj)

    def multi_dof_joint_trajectory_point(cls, msg, obj):
        for i in range(msg['_length_trans']):
            tr = Transform()
            tr.translation = decode.translation(msg, tr.translation, i)
            tr.rotation = decode.rotation(msg, tr.rotation, i)
            obj.transforms.append(tr)
        for i in range(msg['_length_velo']):
            v = Twist()
            v.linear = decode.linear(msg, v.linear, "%s_v" % i)
            v.angular = decode.angular(msg, v.angular, "%s_v" % i)
            obj.velocities.append(v)
        for i in range(msg['_length_acc']):
            a = Twist()
            a.linear = decode.linear(msg, a.linear, "%s_a" % i)
            a.angular = decode.angular(msg, a.angular, "%s_a" % i)
            obj.accelerations.append(a)
        obj.time_from_start = msg['time_from_start']
    return(obj)

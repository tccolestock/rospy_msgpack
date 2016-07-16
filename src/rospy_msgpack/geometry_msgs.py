
from rospy_msgpack import header


class Encode():
    def __init__(self):
        pass

    def accel(cls, obj):
        msg = cls.twist(obj)
        # msg = {}
        # msg['lx'] = data.linear.x
        # msg['ly'] = data.linear.y
        # msg['lz'] = data.linear.z
        # msg['ax'] = data.angular.x
        # msg['ay'] = data.angular.y
        # msg['az'] = data.angular.z
        return(msg)

    def accel_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['lx'] = obj.accel.linear.x
        msg['ly'] = obj.accel.linear.y
        msg['lz'] = obj.accel.linear.z
        msg['ax'] = obj.accel.angular.x
        msg['ay'] = obj.accel.angular.y
        msg['az'] = obj.accel.angular.z
        msg.update(h)
        return(msg)

    def accel_with_covariance(cls, obj):
        msg = {}
        msg['lx'] = obj.accel.linear.x
        msg['ly'] = obj.accel.linear.y
        msg['lz'] = obj.accel.linear.z
        msg['ax'] = obj.accel.angular.x
        msg['ay'] = obj.accel.angular.y
        msg['az'] = obj.accel.angular.z
        msg['covariance'] = obj.covariance
        return(msg)

    def accel_with_covariance_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['lx'] = obj.accel.accel.linear.x
        msg['ly'] = obj.accel.accel.linear.y
        msg['lz'] = obj.accel.accel.linear.z
        msg['ax'] = obj.accel.accel.angular.x
        msg['ay'] = obj.accel.accel.angular.y
        msg['az'] = obj.accel.accel.angular.z
        msg['covariance'] = obj.accel.covariance
        msg.update(h)
        return(msg)

    def inertia(cls, obj):
        msg = {}
        msg['m'] = obj.m
        msg['x'] = obj.com.x
        msg['y'] = obj.com.y
        msg['z'] = obj.com.z
        msg['ixx'] = obj.ixx
        msg['ixy'] = obj.ixy
        msg['ixz'] = obj.ixz
        msg['iyy'] = obj.iyy
        msg['iyz'] = obj.iyz
        msg['izz'] = obj.izz
        return(msg)

    def inertia_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['m'] = obj.inertia.m
        msg['x'] = obj.inertia.com.x
        msg['y'] = obj.inertia.com.y
        msg['z'] = obj.inertia.com.z
        msg['ixx'] = obj.inertia.ixx
        msg['ixy'] = obj.inertia.ixy
        msg['ixz'] = obj.inertia.ixz
        msg['iyy'] = obj.inertia.iyy
        msg['iyz'] = obj.inertia.iyz
        msg['izz'] = obj.inertia.izz
        msg.update(h)
        return(msg)

    def point(cls, obj):
        msg = {}
        msg['x'] = obj.x
        msg['y'] = obj.y
        msg['z'] = obj.z
        return(msg)

    def point32(cls, obj):
        msg = cls.point(obj)
        return(msg)

    def point_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['x'] = obj.point.x
        msg['y'] = obj.point.y
        msg['z'] = obj.point.z
        msg.update(h)
        return(msg)

    def polygon(cls, obj):
        msg = {}
        msg['x'] = obj.points.x
        msg['y'] = obj.points.y
        msg['z'] = obj.points.z
        return(msg)

    def polygon_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['x'] = obj.polygon.points.x
        msg['y'] = obj.polygon.points.y
        msg['z'] = obj.polygon.points.z
        msg.update(h)
        return(msg)

    def pose(cls, obj):
        msg = {}
        msg['px'] = obj.position.x
        msg['py'] = obj.position.y
        msg['pz'] = obj.position.z
        msg['ox'] = obj.orientation.x
        msg['oy'] = obj.orientation.y
        msg['oz'] = obj.orientation.z
        msg['ow'] = obj.orientation.w
        return(msg)

    def pose_2d(cls, obj):
        msg = {}
        msg['x'] = obj.x
        msg['y'] = obj.y
        msg['theta'] = obj.theta
        return(msg)

    def pose_array(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['px'] = obj.poses.position.x
        msg['py'] = obj.poses.position.y
        msg['pz'] = obj.poses.position.z
        msg['ox'] = obj.poses.orientation.x
        msg['oy'] = obj.poses.orientation.y
        msg['oz'] = obj.poses.orientation.z
        msg['ow'] = obj.poses.orientation.w
        msg.update(h)
        return(msg)

    def pose_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['px'] = obj.pose.position.x
        msg['py'] = obj.pose.position.y
        msg['pz'] = obj.pose.position.z
        msg['ox'] = obj.pose.orientation.x
        msg['oy'] = obj.pose.orientation.y
        msg['oz'] = obj.pose.orientation.z
        msg['ow'] = obj.pose.orientation.w
        msg.update(h)
        return(msg)

    def pose_with_covariance(cls, obj):
        msg = {}
        msg['px'] = obj.pose.position.x
        msg['py'] = obj.pose.position.y
        msg['pz'] = obj.pose.position.z
        msg['ox'] = obj.pose.orientation.x
        msg['oy'] = obj.pose.orientation.y
        msg['oz'] = obj.pose.orientation.z
        msg['ow'] = obj.pose.orientation.w
        msg['covariance'] = obj.covariance
        return(msg)

    def pose_with_covariance_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['px'] = obj.pose.pose.position.x
        msg['py'] = obj.pose.pose.position.y
        msg['pz'] = obj.pose.pose.position.z
        msg['ox'] = obj.pose.pose.orientation.x
        msg['oy'] = obj.pose.pose.orientation.y
        msg['oz'] = obj.pose.pose.orientation.z
        msg['ow'] = obj.pose.pose.orientation.w
        msg['covariance'] = obj.pose.covariance
        msg.update(h)
        return(msg)

    def quaternion(cls, obj):
        msg = {}
        msg['x'] = obj.x
        msg['y'] = obj.y
        msg['z'] = obj.z
        msg['w'] = obj.w
        return(msg)

    def quaternion_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['x'] = obj.quaternion.x
        msg['y'] = obj.quaternion.y
        msg['z'] = obj.quaternion.z
        msg['w'] = obj.quaternion.w
        msg.update(h)
        return(msg)

    def transform(cls, obj):
        msg = {}
        msg['tx'] = obj.translation.x
        msg['ty'] = obj.translation.y
        msg['tz'] = obj.translation.z
        msg['rx'] = obj.rotation.x
        msg['ry'] = obj.rotation.y
        msg['rz'] = obj.rotation.z
        msg['rw'] = obj.rotation.w
        return(msg)

    def transform_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['child_frame_id'] = obj.child_frame_id
        msg['tx'] = obj.transform.translation.x
        msg['ty'] = obj.transform.translation.y
        msg['tz'] = obj.transform.translation.z
        msg['rx'] = obj.transform.rotation.x
        msg['ry'] = obj.transform.rotation.y
        msg['rz'] = obj.transform.rotation.z
        msg['rw'] = obj.transform.rotation.w
        msg.update(h)
        return(msg)

    def twist(self, obj):
        msg = {}
        msg['lx'] = obj.linear.x
        msg['ly'] = obj.linear.y
        msg['lz'] = obj.linear.z
        msg['ax'] = obj.angular.x
        msg['ay'] = obj.angular.y
        msg['az'] = obj.angular.z
        return(msg)


    def twist_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['lx'] = obj.twist.linear.x
        msg['ly'] = obj.twist.linear.y
        msg['lz'] = obj.twist.linear.z
        msg['ax'] = obj.twist.angular.x
        msg['ay'] = obj.twist.angular.y
        msg['az'] = obj.twist.angular.z
        msg.update(h)
        return(msg)

    def twist_with_covariance(cls, obj):
        msg = {}
        msg['lx'] = obj.twist.linear.x
        msg['ly'] = obj.twist.linear.y
        msg['lz'] = obj.twist.linear.z
        msg['ax'] = obj.twist.angular.x
        msg['ay'] = obj.twist.angular.y
        msg['az'] = obj.twist.angular.z
        msg['covariance'] = obj.covariance
        return(msg)

    def twist_with_covariance_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['lx'] = obj.twist.twist.linear.x
        msg['ly'] = obj.twist.twist.linear.y
        msg['lz'] = obj.twist.twist.linear.z
        msg['ax'] = obj.twist.twist.angular.x
        msg['ay'] = obj.twist.twist.angular.y
        msg['az'] = obj.twist.twist.angular.z
        msg['covariance'] = obj.twist.covariance
        msg.update(h)
        return(msg)

    def vector3(cls, obj):
        msg = {}
        msg['x'] = obj.x
        msg['y'] = obj.y
        msg['z'] = obj.z
        return(msg)

    def vector3_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['x'] = obj.vector.x
        msg['y'] = obj.vector.y
        msg['z'] = obj.vector.z
        msg.update(h)
        return(msg)

    def wrench(cls, obj):
        msg = {}
        msg['fx'] = obj.force.x
        msg['fy'] = obj.force.y
        msg['fz'] = obj.force.z
        msg['tx'] = obj.torque.x
        msg['ty'] = obj.torque.y
        msg['tz'] = obj.torque.z
        return(msg)

    def wrench_stamped(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['fx'] = obj.wrench.force.x
        msg['fy'] = obj.wrench.force.y
        msg['fz'] = obj.wrench.force.z
        msg['tx'] = obj.wrench.torque.x
        msg['ty'] = obj.wrench.torque.y
        msg['tz'] = obj.wrench.torque.z
        msg.update(h)
        return(msg)

#=======================================================================================


class Decode():
    def __init__(self):
        pass

    def twist(self, msg, obj):
         obj.linear.x = msg['lx']
         obj.linear.y = msg['ly']
         obj.linear.z = msg['lz']
         obj.angular.x = msg['ax']
         obj.angular.y = msg['ay']
         obj.angular.z = msg['az']
         return(obj)

    def accel(cls, msg, obj):
        obj = cls.twist(msg, obj)
        # obj.linear.x = msg['lx']
        # obj.linear.y = msg['ly']
        # obj.linear.z = msg['lz']
        # obj.angular.x = msg['ax']
        # obj.angular.y = msg['ay']
        # obj.angular.z = msg['az']
        return(obj)

    def accel_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.accel.linear.x = msg['lx']
        obj.accel.linear.y = msg['ly']
        obj.accel.linear.z = msg['lz']
        obj.accel.angular.x = msg['ax']
        obj.accel.angular.y = msg['ay']
        obj.accel.angular.z = msg['az']
        return(obj)

    def accel_with_covariance(cls, msg, obj):
        obj.accel.linear.x = msg['lx']
        obj.accel.linear.y = msg['ly']
        obj.accel.linear.z = msg['lz']
        obj.accel.angular.x = msg['ax']
        obj.accel.angular.y = msg['ay']
        obj.accel.angular.z = msg['az']
        obj.covariance = msg['covariance']
        return(obj)

    def accel_with_covariance_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.accel.accel.linear.x = msg['lx']
        obj.accel.accel.linear.y = msg['ly']
        obj.accel.accel.linear.z = msg['lz']
        obj.accel.accel.angular.x = msg['ax']
        obj.accel.accel.angular.y = msg['ay']
        obj.accel.accel.angular.z = msg['az']
        obj.accel.covariance = msg['covariance']
        return(obj)

    def inertia(cls, msg, obj):
        obj.m = msg['m']
        obj.com.x = msg['x']
        obj.com.y = msg['y']
        obj.com.z = msg['z']
        obj.ixx = msg['ixx']
        obj.ixy = msg['ixy']
        obj.ixz = msg['ixz']
        obj.iyy = msg['iyy']
        obj.iyz = msg['iyz']
        obj.izz = msg['izz']
        return(obj)

    def inertia_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.inertia.m = msg['m']
        obj.inertia.com.x = msg['x']
        obj.inertia.com.y = msg['y']
        obj.inertia.com.z = msg['z']
        obj.inertia.ixx = msg['ixx']
        obj.inertia.ixy = msg['ixy']
        obj.inertia.ixz = msg['ixz']
        obj.inertia.iyy = msg['iyy']
        obj.inertia.iyz = msg['iyz']
        obj.inertia.izz = msg['izz']
        return(obj)

    def point(cls, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.z = msg['z']
        return(obj)

    def point32(cls, msg, obj):
        obj = cls.point(msg, obj)
        return(obj)

    def point_stamped(cls, msg, obj):
        msg = {}
        obj = header.Header().decode(msg, obj)
        obj.point.x = msg['x']
        obj.point.y = msg['y']
        obj.point.z = msg['z']
        return(obj)

    def polygon(cls, msg, obj):
        obj.points.x = msg['x']
        obj.points.y = msg['y']
        obj.points.z = msg['z']
        return(obj)

    def polygon_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.polygon.points.x = msg['x']
        obj.polygon.points.y = msg['y']
        obj.polygon.points.z = msg['z']
        return(obj)

    def pose(cls, msg, obj):
        obj.position.x = msg['px']
        obj.position.y = msg['py']
        obj.position.z = msg['pz']
        obj.orientation.x = msg['ox']
        obj.orientation.y = msg['oy']
        obj.orientation.z = msg['oz']
        obj.orientation.w = msg['ow']
        return(obj)

    def pose_2d(cls, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.theta = msg['theta']
        return(obj)

    def pose_array(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.poses.position.x = msg['px']
        obj.poses.position.y = msg['py']
        obj.poses.position.z = msg['pz']
        obj.poses.orientation.x = msg['ox']
        obj.poses.orientation.y = msg['oy']
        obj.poses.orientation.z = msg['oz']
        obj.poses.orientation.w = msg['ow']
        return(obj)

    def pose_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.pose.position.x = msg['px']
        obj.pose.position.y = msg['py']
        obj.pose.position.z = msg['pz']
        obj.pose.orientation.x = msg['ox']
        obj.pose.orientation.y = msg['oy']
        obj.pose.orientation.z = msg['oz']
        obj.pose.orientation.w = msg['ow']
        return(obj)

    def pose_with_covariance(cls, msg, obj):
        obj.pose.position.x = msg['px']
        obj.pose.position.y = msg['py']
        obj.pose.position.z = msg['pz']
        obj.pose.orientation.x = msg['ox']
        obj.pose.orientation.y = msg['oy']
        obj.pose.orientation.z = msg['oz']
        obj.pose.orientation.w = msg['ow']
        obj.covariance = msg['covariance']
        return(obj)

    def pose_with_covariance_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.pose.pose.position.x = msg['px']
        obj.pose.pose.position.y = msg['py']
        obj.pose.pose.position.z = msg['pz']
        obj.pose.pose.orientation.x = msg['ox']
        obj.pose.pose.orientation.y = msg['oy']
        obj.pose.pose.orientation.z = msg['oz']
        obj.pose.pose.orientation.w = msg['ow']
        obj.pose.covariance = msg['covariance']
        return(obj)

    def quaternion(cls, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.z = msg['z']
        obj.w = msg['w']
        return(obj)

    def quaternion_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.quaternion.x = msg['x']
        obj.quaternion.y = msg['y']
        obj.quaternion.z = msg['z']
        obj.quaternion.w = msg['w']
        return(obj)

    def transform(cls, msg, obj):
        obj.translation.x = msg['tx']
        obj.translation.y = msg['ty']
        obj.translation.z = msg['tz']
        obj.rotation.x = msg['rx']
        obj.rotation.y = msg['ry']
        obj.rotation.z = msg['rz']
        obj.rotation.w = msg['rw']
        return(obj)

    def transform_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.child_frame_id = msg['child_frame_id']
        obj.transform.translation.x = msg['tx']
        obj.transform.translation.y = msg['ty']
        obj.transform.translation.z = msg['tz']
        obj.transform.rotation.x = msg['rx']
        obj.transform.rotation.y = msg['ry']
        obj.transform.rotation.z = msg['rz']
        obj.transform.rotation.w = msg['rw']
        return(obj)

    def twist_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.twist.linear.x = msg['lx']
        obj.twist.linear.y = msg['ly']
        obj.twist.linear.z = msg['lz']
        obj.twist.angular.x = msg['ax']
        obj.twist.angular.y = msg['ay']
        obj.twist.angular.z = msg['az']
        return(obj)

    def twist_with_covariance(cls, msg, obj):
        obj.twist.linear.x = msg['lx']
        obj.twist.linear.y = msg['ly']
        obj.twist.linear.z = msg['lz']
        obj.twist.angular.x = msg['ax']
        obj.twist.angular.y = msg['ay']
        obj.twist.angular.z = msg['az']
        obj.covariance = msg['covariance']
        return(obj)

    def twist_with_covariance_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.twist.twist.linear.x = msg['lx']
        obj.twist.twist.linear.y = msg['ly']
        obj.twist.twist.linear.z = msg['lz']
        obj.twist.twist.angular.x = msg['ax']
        obj.twist.twist.angular.y = msg['ay']
        obj.twist.twist.angular.z = msg['az']
        obj.twist.covariance = msg['covariance']
        return(obj)

    def vector3(cls, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.z = msg['z']
        return(obj)

    def vector3_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.vector.x = msg['x']
        obj.vector.y = msg['y']
        obj.vector.z = msg['z']
        return(obj)

    def wrench(cls, msg, obj):
        obj.force.x = msg['fx']
        obj.force.y = msg['fy']
        obj.force.z = msg['fz']
        obj.torque.x = msg['tx']
        obj.torque.y = msg['ty']
        obj.torque.z = msg['tz']
        return(obj)

    def wrench_stamped(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.wrench.force.x = msg['fx']
        obj.wrench.force.y = msg['fy']
        obj.wrench.force.z = msg['fz']
        obj.wrench.torque.x = msg['tx']
        obj.wrench.torque.y = msg['ty']
        obj.wrench.torque.z = msg['tz']
        return(obj)

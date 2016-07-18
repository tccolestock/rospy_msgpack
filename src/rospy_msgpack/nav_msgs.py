
from rospy_msgpack import header

class Encode():
    def __init__(self):
        pass

    def grid_cells(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['cell_width'] = obj.cell_width
        msg['cell_height'] = obj.cell_height
        msg['x'] = obj.cells.x
        msg['y'] = obj.cells.y
        msg['z'] = obj.cells.z
        msg.update(h)
        return(msg)

    def map_meta_data(cls, obj):
        msg = {}
        msg['map_load_time'] = obj.map_load_time
        msg['resolution'] = obj.resolution
        msg['width'] = obj.width
        msg['height'] = obj.height
        msg['px'] = obj.origin.position.x
        msg['py'] = obj.origin.position.y
        msg['pz'] = obj.origin.position.z
        msg['ox'] = obj.origin.orientation.x
        msg['oy'] = obj.origin.orientation.y
        msg['oz'] = obj.origin.orientation.z
        msg['ow'] = obj.origin.orientation.w
        return(msg)

    def occupancy_grid(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['map_load_time'] = obj.info.map_load_time
        msg['resolution'] = obj.info.resolution
        msg['width'] = obj.info.width
        msg['height'] = obj.info.height
        msg['px'] = obj.info.origin.position.x
        msg['py'] = obj.info.origin.position.y
        msg['pz'] = obj.info.origin.position.z
        msg['ox'] = obj.info.origin.orientation.x
        msg['oy'] = obj.info.origin.orientation.y
        msg['oz'] = obj.info.origin.orientation.z
        msg['ow'] = obj.info.origin.orientation.w
        msg['data'] = obj.data
        msg.update(h)
        return(msg)

    def odometry(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['child_frame_id'] = obj.child_frame_id
        msg['px'] = obj.pose.pose.position.x
        msg['py'] = obj.pose.pose.position.y
        msg['pz'] = obj.pose.pose.position.z
        msg['ox'] = obj.pose.pose.orientation.x
        msg['oy'] = obj.pose.pose.orientation.y
        msg['oz'] = obj.pose.pose.orientation.z
        msg['ow'] = obj.pose.pose.orientation.w
        msg['pose_covariance'] = obj.pose.covariance
        msg['lx'] = obj.twist.twist.linear.x
        msg['ly'] = obj.twist.twist.linear.y
        msg['lz'] = obj.twist.twist.linear.z
        msg['ax'] = obj.twist.twist.angular.x
        msg['ay'] = obj.twist.twist.angular.y
        msg['az'] = obj.twist.twist.angular.z
        msg['twist_covariance'] = obj.twist.covariance
        msg.update(h)
        return(msg)

    def path(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['pose_seq'] = obj.poses.header.seq
        msg['pose_secs'] = obj.poses.header.stamp.secs
        msg['pose_nsecs'] = obj.poses.header.stamp.nsecs
        msg['pose_frame_id'] = obj.poses.header.frame_id
        msg['px'] = obj.poses.pose.position.x
        msg['py'] = obj.poses.pose.position.y
        msg['pz'] = obj.poses.pose.position.z
        msg['ox'] = obj.poses.pose.orientation.x
        msg['oy'] = obj.poses.pose.orientation.y
        msg['oz'] = obj.poses.pose.orientation.z
        msg['ow'] = obj.poses.pose.orientation.w
        msg.update(h)
        return(msg)

#=================================================================================

class Decode():
    def __init__(self):
        pass

    def grid_cells(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.cell_width = msg['cell_width']
        obj.cell_height = msg['cell_height']
        obj.cells.x = msg['x']
        obj.cells.y = msg['y']
        obj.cells.z = msg['z']
        return(obj)

    def map_meta_data(cls, msg, obj):
        obj.map_load_time = msg['map_load_time']
        obj.resolution = msg['resolution']
        obj.width = msg['width']
        obj.height = msg['height']
        obj.origin.position.x = msg['px']
        obj.origin.position.y = msg['py']
        obj.origin.position.z = msg['pz']
        obj.origin.orientation.x = msg['ox']
        obj.origin.orientation.y = msg['oy']
        obj.origin.orientation.z = msg['oz']
        obj.origin.orientation.w = msg['ow']
        return(obj)

    def occupancy_grid(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.info.map_load_time = msg['map_load_time']
        obj.info.resolution = msg['resolution']
        obj.info.width = msg['width']
        obj.info.height = msg['height']
        obj.info.origin.position.x = msg['px']
        obj.info.origin.position.y = msg['py']
        obj.info.origin.position.z = msg['pz']
        obj.info.origin.orientation.x = msg['ox']
        obj.info.origin.orientation.y = msg['oy']
        obj.info.origin.orientation.z = msg['oz']
        obj.info.origin.orientation.w = msg['ow']
        obj.data = msg['data']
        return(obj)

    def odometry(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.child_frame_id = msg['child_frame_id']
        obj.pose.pose.position.x = msg['px']
        obj.pose.pose.position.y = msg['py']
        obj.pose.pose.position.z = msg['pz']
        obj.pose.pose.orientation.x = msg['ox']
        obj.pose.pose.orientation.y = msg['oy']
        obj.pose.pose.orientation.z = msg['oz']
        obj.pose.pose.orientation.w = msg['ow']
        obj.pose.covariance = msg['pose_covariance']
        obj.twist.twist.linear.x = msg['lx']
        obj.twist.twist.linear.y = msg['ly']
        obj.twist.twist.linear.z = msg['lz']
        obj.twist.twist.angular.x = msg['ax']
        obj.twist.twist.angular.y = msg['ay']
        obj.twist.twist.angular.z = msg['az']
        obj.twist.covariance = msg['twist_covariance']
        return(obj)

    def path(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.poses.header.seq = msg['pose_seq']
        obj.poses.header.stamp.secs = msg['pose_secs']
        obj.poses.header.stamp.nsecs = msg['pose_nsecs']
        obj.poses.header.frame_id = msg['pose_frame_id']
        obj.poses.pose.position.x = msg['px']
        obj.poses.pose.position.y = msg['py']
        obj.poses.pose.position.z = msg['pz']
        obj.poses.pose.orientation.x = msg['ox']
        obj.poses.pose.orientation.y = msg['oy']
        obj.poses.pose.orientation.z = msg['oz']
        obj.poses.pose.orientation.w = msg['ow']
        return(obj)
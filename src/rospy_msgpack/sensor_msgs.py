# from sensor_msgs.msg import JointState


class Encode():
    def __init__(self):
        pass

    def joint_state(self, data):
        msg = {}
        msg['seq'] = data.header.seq
        msg['secs'] = data.header.stamp.secs
        msg['nsecs'] = data.header.stamp.nsecs
        msg['frame_id'] = data.header.frame_id
        msg['name'] = data.name
        msg['position'] = data.position
        msg['velocity'] = data.velocity
        msg['effort'] = data.effort
        return(msg)


class Decode():
    def __init__(self):
        pass

    def joint_state(self, msg, obj):
        # js = JointState()
        obj.header.seq = msg['seq']
        obj.header.stamp.secs = msg['secs']
        obj.header.stamp.nsecs = msg['nsecs']
        obj.header.frame_id = msg['frame_id']
        obj.name = msg['name']
        obj.position = msg['position']
        obj.velocity = msg['velocity']
        obj.effort = msg['effort']
        return(obj)

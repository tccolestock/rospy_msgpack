# from sensor_msgs.msg import JointState


class Encode():
    def __init__(self):
        pass

    def JointState(self, data):
        ser = {}
        ser['seq'] = data.header.seq
        ser['secs'] = data.header.stamp.secs
        ser['nsecs'] = data.header.stamp.nsecs
        ser['frame_id'] = data.header.frame_id
        ser['name'] = data.name
        ser['position'] = data.position
        ser['velocity'] = data.velocity
        ser['effort'] = data.effort
        return(ser)


class Decode():
    def __init__(self):
        pass

    def JointState(self, ser, js):
        # js = JointState()
        js.header.seq = ser['seq']
        js.header.stamp.secs = ser['secs']
        js.header.stamp.nsecs = ser['nsecs']
        js.header.frame_id = ser['frame_id']
        js.name = ser['name']
        js.position = ser['position']
        js.velocity = ser['velocity']
        js.effort = ser['effort']
        return(js)

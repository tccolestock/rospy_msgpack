

class Encode():
    def __init__(self):
        pass

    def goal_id(self, data):
        msg = {}
        msg['secs'] = data.stamp.secs
        msg['nsecs'] = data.stamp.nsecs
        msg['id'] = data.id
        return(msg)

    # todo: figure out GoalStatus message

    def goal_status_array(self, data):
        msg = {}
        msg['seq'] = data.header.seq
        msg['secs'] = data.header.stamp.secs
        msg['nsecs'] = data.header.stamp.nsecs
        msg['frame_id'] = data.header.frame_id
        msg['status_list'] = data.status_list
        return(msg)


class Decode():
    def __init__(self):
        pass

    def goal_id(self, msg, obj):
        obj.stamp.secs = msg['secs']
        obj.stamp.nsecs = msg['nsecs']
        obj.id = msg['id']
        return(obj)

    # todo: figure out GoalStatus message

    def goal_status_array(self, msg, obj):
        obj.header.seq = msg['seq']
        obj.header.stamp.secs = msg['secs']
        obj.header.stamp.nsecs = msg['nsecs']
        obj.header.frame_id = msg['frame_id']
        obj.status_list = msg['status_list']
        return(obj)

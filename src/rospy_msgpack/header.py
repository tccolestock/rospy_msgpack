

class Header():
    def encode(self, data):
        h = {}
        h['seq'] = data.header.seq
        h['secs'] = data.header.stamp.secs
        h['nsecs'] = data.header.stamp.nsecs
        h['frame_id'] = data.header.frame_id
        return(h)

    def decode(self, msg, obj):
        obj.header.seq = msg['seq']
        obj.header.stamp.secs = msg['secs']
        obj.header.stamp.nsecs = msg['nsecs']
        obj.header.frame_id = msg['frame_id']
        return(obj)

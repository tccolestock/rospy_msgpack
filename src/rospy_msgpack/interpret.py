

class Encode():
    def __init__(self):
        pass

    def header(cls, obj, i):
        h = {}
        h['%sseq' %i] = obj.seq
        h['%ssecs' %i] = obj.stamp.secs
        h['%snsecs' %i] = obj.stamp.nsecs
        h['%sframe_id' %i] = obj.frame_id
        return(h)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, obj, i):
        msg = {}
        msg['%saccel_x' %i] = obj.x
        msg['%saccel_y' %i] = obj.y
        msg['%saccel_z' %i] = obj.z
        return(msg)

    def linear(cls, obj, i):
        msg = {}
        msg['%slin_x' %i] = obj.x
        msg['%slin_y' %i] = obj.y
        msg['%slin_z' %i] = obj.z
        return(msg)

    def position(cls, obj, i):
        msg = {}
        msg['%spos_x' %i] = obj.x
        msg['%spos_y' %i] = obj.y
        msg['%spos_z' %i] = obj.z
        return(msg)

    def orientation(cls, obj, i):
        msg = {}
        msg['%sorient_x' %i] = obj.x
        msg['%sorient_y' %i] = obj.y
        msg['%sorient_z' %i] = obj.z
        msg['%sorient_w' %i] = obj.w
        return(msg)

    def covariance(cls, obj, i):
        msg = {}
        msg['%scovariance' %i] = obj.covariance
        return(msg)

    # def twist(cls, obj, i):
    #     msg = {}



class Decode():
    def __init__(self):
        pass

    def header(cls, msg, obj, i):
        obj.header.seq = msg['%sseq' %i]
        obj.header.stamp.secs = msg['%ssecs' %i]
        obj.header.stamp.nsecs = msg['%snsecs' %i]
        obj.header.frame_id = msg['%sframe_id' %i]
        return(obj)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, msg, obj, i):
        obj.x = msg['%saccel_x' %i]
        obj.y = msg['%saccel_y' %i]
        obj.z = msg['%saccel_z' %i]
        return(obj)

    def linear(cls, msg, obj, i):
        obj.x = msg['%slin_x' %i]
        obj.y = msg['%slin_y' %i]
        obj.z = msg['%slin_z' %i]
        return(obj)

    def position(cls, msg, obj, i):
        obj.x = msg['%spos_x' %i]
        obj.y = msg['%spos_y' %i]
        obj.z = msg['%spos_z' %i]
        return(obj)

    def orientation(cls, msg, obj, i):
        obj.x = msg['%sorient_x' %i]
        obj.y = msg['%sorient_y' %i]
        obj.z = msg['%sorient_z' %i]
        obj.w = msg['%sorient_w' %i]
        return(obj)

    def covariance(cls, msg, obj, i):
        obj.covariance = msg['%scovariance' %i]
        return(obj)

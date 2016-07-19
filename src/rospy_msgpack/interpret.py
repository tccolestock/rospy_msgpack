

class Encode():
    def __init__(self):
        pass

# ------------------ Universal Basic Functions -----------------------------
    def xyz(cls, obj, uniq, desc):
        # receives the object, a unique identifier if needed, and the descriptive term
        msg = {}
        msg['%s%s_x' %(uniq, desc)] = obj.x
        msg['%s%s_y' %(uniq, desc)] = obj.y
        msg['%s%s_z' %(uniq, desc)] = obj.z
        return(msg)

# ------------------ Header Messages -----------------------------
    def header(cls, obj, i):
        h = {}
        h['%sseq' %i] = obj.seq
        h['%ssecs' %i] = obj.stamp.secs
        h['%snsecs' %i] = obj.stamp.nsecs
        h['%sframe_id' %i] = obj.frame_id
        return(h)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, obj, i):
        msg = cls.xyz(obj, i, "ang")
        # msg = {}
        # msg['%sang_x' %i] = obj.x
        # msg['%sang_y' %i] = obj.y
        # msg['%sang_z' %i] = obj.z
        return(msg)

    def linear(cls, obj, i):
        msg = cls.xyz(obj, i, "lin")
        # msg = {}
        # msg['%slin_x' %i] = obj.x
        # msg['%slin_y' %i] = obj.y
        # msg['%slin_z' %i] = obj.z
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

    def com(cls, obj, i):
        msg = {}
        msg['%scom_x' %i] = obj.x
        msg['%scom_y' %i] = obj.y
        msg['%scom_z' %i] = obj.z
        return(msg)

    def inertia(cls, obj, i):
        msg = {}
        msg['%sixx' %i] = obj.ixx
        msg['%sixy' %i] = obj.ixy
        msg['%sixz' %i] = obj.ixz
        msg['%siyy' %i] = obj.iyy
        msg['%siyz' %i] = obj.iyz
        msg['%sizz' %i] = obj.izz
        return(msg)

    def point(cls, obj, i):
        msg = {}
        msg['%sx' %i] = obj.x
        msg['%sy' %i] = obj.y
        msg['%sz' %i] = obj.z
        return(msg)

    def quaternion(cls, obj, i):
        msg = {}
        msg['%squat_x' %i] = obj.x
        msg['%squat_y' %i] = obj.y
        msg['%squat_z' %i] = obj.z
        msg['%squat_w' %i] = obj.w
        return(msg)

    def translation(cls, obj, i):
        msg = {}
        msg['%strans_x' %i] = obj.x
        msg['%strans_y' %i] = obj.y
        msg['%strans_z' %i] = obj.z
        return(msg)

    def rotation(cls, obj, i):
        msg = {}
        msg['%srot_x' %i] = obj.x
        msg['%srot_y' %i] = obj.y
        msg['%srot_z' %i] = obj.z
        msg['%srot_w' %i] = obj.w
        return(msg)

    def vector(cls, obj, i):
        msg = {}
        msg['%svect_x' %i] = obj.x
        msg['%svect_y' %i] = obj.y
        msg['%svect_z' %i] = obj.z
        return(msg)

    def force(cls, obj, i):
        msg = {}
        msg['%sforce_x' %i] = obj.x
        msg['%sforce_y' %i] = obj.y
        msg['%sforce_z' %i] = obj.z
        return(msg)

    def torque(cls, obj, i):
        msg = {}
        msg['%storq_x' %i] = obj.x
        msg['%storq_y' %i] = obj.y
        msg['%storq_z' %i] = obj.z
        return(msg)

class Decode():
    def __init__(self):
        pass

# ------------------ Universal Basic Functions -----------------------------
    def xyz(cls, msg, obj, uniq, desc):
        obj.x = msg["%s%s_x" %(uniq, desc)]
        obj.y = msg["%s%s_y" %(uniq, desc)]
        obj.z = msg["%s%s_z" %(uniq, desc)]
        return(obj)

# ------------------ Header Messages -----------------------------
    def header(cls, msg, obj, i):
        obj.seq = msg['%sseq' %i]
        obj.stamp.secs = msg['%ssecs' %i]
        obj.stamp.nsecs = msg['%snsecs' %i]
        obj.frame_id = msg['%sframe_id' %i]
        return(obj)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "ang")
        # obj.x = msg['%sang_x' %i]
        # obj.y = msg['%sang_y' %i]
        # obj.z = msg['%sang_z' %i]
        return(obj)

    def linear(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "lin")
        # obj.x = msg['%slin_x' %i]
        # obj.y = msg['%slin_y' %i]
        # obj.z = msg['%slin_z' %i]
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

    def com(cls, msg, obj, i):
        obj.x = msg['%scom_x' %i]
        obj.y = msg['%scom_y' %i]
        obj.z = msg['%scom_z' %i]
        return(obj)

    def inertia(cls, msg, obj, i):
        obj.ixx = msg['%sixx' %i]
        obj.ixy = msg['%sixy' %i]
        obj.ixz = msg['%sixz' %i]
        obj.iyy = msg['%siyy' %i]
        obj.iyz = msg['%siyz' %i]
        obj.izz = msg['%sizz' %i]
        return(obj)

    def point(cls, msg, obj, i):
        obj.x = msg['%sx' %i]
        obj.y = msg['%sy' %i]
        obj.z = msg['%sz' %i]
        return(obj)

    def quaternion(cls, msg, obj, i):
        obj.x = msg['%squat_x' %i]
        obj.y = msg['%squat_y' %i]
        obj.z = msg['%squat_z' %i]
        obj.w = msg['%squat_w' %i]
        return(obj)

    def translation(cls, msg, obj, i):
        obj.x = msg['%strans_x' %i]
        obj.y = msg['%strans_y' %i]
        obj.z = msg['%strans_z' %i]
        return(obj)

    def rotation(cls, msg, obj, i):
        obj.x = msg['%srot_x' %i]
        obj.y = msg['%srot_y' %i]
        obj.z = msg['%srot_z' %i]
        obj.w = msg['%srot_w' %i]
        return(obj)

    def vector(cls, msg, obj, i):
        obj.x = msg['%svect_x' %i]
        obj.y = msg['%svect_y' %i]
        obj.z = msg['%svect_z' %i]
        return(obj)

    def force(cls, msg, obj, i):
        obj.x = msg['%sforce_x' %i]
        obj.y = msg['%sforce_y' %i]
        obj.z = msg['%sforce_z' %i]
        return(obj)
    def torque(cls, msg, obj, i):
        obj.x = msg['%storq_x' %i]
        obj.y = msg['%storq_y' %i]
        obj.z = msg['%storq_z' %i]
        return(obj)

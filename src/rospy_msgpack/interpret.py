

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

    def xyzw(cls, obj, uniq, desc):
        # receives the object, a unique identifier if needed, and the descriptive term
        msg = {}
        msg['%s%s_x' %(uniq, desc)] = obj.x
        msg['%s%s_y' %(uniq, desc)] = obj.y
        msg['%s%s_z' %(uniq, desc)] = obj.z
        msg['%s%s_w' %(uniq, desc)] = obj.w
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
        return(msg)

    def com(cls, obj, i):
        msg = cls.xyz(obj, i, "com")
        return(msg)

    def covariance(cls, obj, i):
        msg = {}
        msg['%scovariance' %i] = obj.covariance
        return(msg)

    def force(cls, obj, i):
        msg = cls.xyz(obj, i, "force")
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

    def linear(cls, obj, i):
        msg = cls.xyz(obj, i, "lin")
        return(msg)

    def orientation(cls, obj, i):
        msg = cls.xyzw(obj, i, "orient")
        return(msg)

    def point(cls, obj, i):
        msg = cls.xyz(obj, i, "pnt")
        return(msg)

    def position(cls, obj, i):
        msg = cls.xyz(obj, i, "pos")
        return(msg)

    def quaternion(cls, obj, i):
        msg = xyzw(obj, i, "quat")
        return(msg)

    def rotation(cls, obj, i):
        msg = cls.xyzw(obj, i, "rot")
        return(msg)

    def torque(cls, obj, i):
        msg = cls.xyz(obj, i, "torq")
        return(msg)

    def translation(cls, obj, i):
        msg = cls.xyz(obj, i, "trans")
        return(msg)

    def vector(cls, obj, i):
        msg = cls.xyz(obj, i, "vect")
        return(msg)

# ------------------ Sensor Messages -----------------------------
    def roi(cls, obj, i): # region_of_interest
        msg = {}
        msg["%sx_offset" %i] = obj.x_offset
        msg["%sy_offset" %i] = obj.y_offset
        msg["%sheight" %i] = obj.height
        msg["%swidth" %i] = obj.width
        msg["%sdo_rectify" %i] = obj.do_rectify
        return(msg)

    def laser(cls, obj, i):
        msg = {}
        msg["%sangle_min" %i] = obj.angle_min
        msg["%sangle_max" %i] = obj.angle_max
        msg["%sangle_increment" %i] = obj.angle_increment
        msg["%stime_increment" %i] = obj.time_increment
        msg["%sscan_time" %i] = obj.scan_time
        msg["%srange_min" %i] = obj.range_min
        msg["%srange_max" %i] = obj.range_max
        return(msg)


# =========================== Decode Functions ==============================================

class Decode():
    def __init__(self):
        pass

# ------------------ Universal Basic Functions -----------------------------
    def xyz(cls, msg, obj, uniq, desc):
        obj.x = msg["%s%s_x" %(uniq, desc)]
        obj.y = msg["%s%s_y" %(uniq, desc)]
        obj.z = msg["%s%s_z" %(uniq, desc)]
        return(obj)

    def xyzw(cls, msg, obj, uniq, desc):
        obj.x = msg["%s%s_x" %(uniq, desc)]
        obj.y = msg["%s%s_y" %(uniq, desc)]
        obj.z = msg["%s%s_z" %(uniq, desc)]
        obj.w = msg["%s%s_w" %(uniq, desc)]
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
        return(obj)

    def com(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "com")
        return(obj)

    def covariance(cls, msg, obj, i):
        obj.covariance = msg['%scovariance' %i]
        return(obj)

    def force(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "force")
        return(obj)

    def inertia(cls, msg, obj, i):
        obj.ixx = msg['%sixx' %i]
        obj.ixy = msg['%sixy' %i]
        obj.ixz = msg['%sixz' %i]
        obj.iyy = msg['%siyy' %i]
        obj.iyz = msg['%siyz' %i]
        obj.izz = msg['%sizz' %i]
        return(obj)

    def linear(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "lin")
        return(obj)

    def orientation(cls, msg, obj, i):
        obj = cls.xyzw(msg, obj, i, "orient")
        return(obj)

    def point(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "pnt")
        return(obj)

    def position(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "pos")
        return(obj)

    def quaternion(cls, msg, obj, i):
        obj = cls.xyzw(msg, obj, i, "quat")
        return(obj)

    def rotation(cls, msg, obj, i):
        obj = cls.xyzw(msg, obj, i, "rot")
        return(obj)

    def torque(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "torq")
        return(obj)

    def translation(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "trans")
        return(obj)

    def vector(cls, msg, obj, i):
        obj = cls.xyz(msg, obj, i, "vect")
        return(obj)

# ------------------ Sensor Messages -----------------------------

    def roi(cls, msg, obj, i): # region_of_interest
        obj.x_offset = msg["%sx_offset" %i]
        obj.y_offset = msg["%sy_offset" %i]
        obj.height = msg["%sheight" %i]
        obj.width = msg["%swidth" %i]
        obj.do_rectify = msg["%sdo_rectify" %i]
        return(obj)

    def laser(cls, msg, obj, i):
        obj.angle_min = msg["%sangle_min" %i]
        obj.angle_max = msg["%sangle_max" %i]
        obj.angle_increment = msg["%sangle_increment" %i]
        obj.time_increment = msg["%stime_increment" %i]
        obj.scan_time = msg["%sscan_time" %i]
        obj.range_min = msg["%srange_min" %i]
        obj.range_max = msg["%srange_max" %i]
        return(obj)

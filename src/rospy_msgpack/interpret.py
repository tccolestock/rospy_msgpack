

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
    def header(cls, obj, uniq):
        h = {}
        h['%sseq' %uniq] = obj.seq
        h['%ssecs' %uniq] = obj.stamp.secs
        h['%snsecs' %uniq] = obj.stamp.nsecs
        h['%sframe_id' %uniq] = obj.frame_id
        return(h)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, obj, uniq):
        msg = {}
        msg['%s_ang_x' %uniq] = obj.x
        msg['%s_ang_y' %uniq] = obj.y
        msg['%s_ang_z' %uniq] = obj.z
        return(msg)

    def com(cls, obj, uniq):
        msg = {}
        msg['%s_com_x' %uniq] = obj.x
        msg['%s_com_y' %uniq] = obj.y
        msg['%s_com_z' %uniq] = obj.z
        return(msg)

    def covariance(cls, obj, uniq):
        msg = {}
        msg['%s_covariance' %uniq] = obj.covariance
        return(msg)

    def force(cls, obj, uniq):
        # msg = cls.xyz(obj, i, "force")
        msg = {}
        msg['%s_force_x' %uniq] = obj.x
        msg['%s_force_y' %uniq] = obj.y
        msg['%s_force_z' %uniq] = obj.z
        return(msg)

    def inertia(cls, obj, uniq):
        msg = {}
        msg['%s_ixx' %uniq] = obj.ixx
        msg['%s_ixy' %uniq] = obj.ixy
        msg['%s_ixz' %uniq] = obj.ixz
        msg['%s_iyy' %uniq] = obj.iyy
        msg['%s_iyz' %uniq] = obj.iyz
        msg['%s_izz' %uniq] = obj.izz
        return(msg)

    def linear(cls, obj, uniq):
        msg = {}
        msg['%s_lin_x' %uniq] = obj.x
        msg['%s_lin_y' %uniq] = obj.y
        msg['%s_lin_z' %uniq] = obj.z
        return(msg)

    def orientation(cls, obj, uniq):
        msg = {}
        msg['%s_orient_x' %uniq] = obj.x
        msg['%s_orient_y' %uniq] = obj.y
        msg['%s_orient_z' %uniq] = obj.z
        msg['%s_orient_w' %uniq] = obj.w
        return(msg)

    def point(cls, obj, uniq):
        msg = {}
        msg['%s_pnt_x' %uniq] = obj.x
        msg['%s_pnt_y' %uniq] = obj.y
        msg['%s_pnt_z' %uniq] = obj.z
        return(msg)

    def position(cls, obj, uniq):
        msg = {}
        msg['%s_pos_x' %uniq] = obj.x
        msg['%s_pos_y' %uniq] = obj.y
        msg['%s_pos_z' %uniq] = obj.z
        return(msg)

    def quaternion(cls, obj, uniq):
        msg = {}
        msg['%s_quat_x' %uniq] = obj.x
        msg['%s_quat_y' %uniq] = obj.y
        msg['%s_quat_z' %uniq] = obj.z
        msg['%s_quat_w' %uniq] = obj.w
        return(msg)

    def rotation(cls, obj, uniq):
        msg = {}
        msg['%s_rot_x' %uniq] = obj.x
        msg['%s_rot_y' %uniq] = obj.y
        msg['%s_rot_z' %uniq] = obj.z
        msg['%s_rot_w' %uniq] = obj.w
        return(msg)

    def torque(cls, obj, uniq):
        msg = {}
        msg['%s_torq_x' %uniq] = obj.x
        msg['%s_torq_y' %uniq] = obj.y
        msg['%s_torq_z' %uniq] = obj.z
        return(msg)

    def translation(cls, obj, uniq):
        msg = {}
        msg['%s_trans_x' %uniq] = obj.x
        msg['%s_trans_y' %uniq] = obj.y
        msg['%s_trans_z' %uniq] = obj.z
        return(msg)

    def vector(cls, obj, uniq):
        msg = {}
        msg['%s_vect_x' %uniq] = obj.x
        msg['%s_vect_y' %uniq] = obj.y
        msg['%s_vect_z' %uniq] = obj.z
        return(msg)

# ------------------ Sensor Messages -----------------------------
    def roi(cls, obj, uniq): # region_of_interest
        msg = {}
        msg["%sx_offset" %uniq] = obj.x_offset
        msg["%sy_offset" %uniq] = obj.y_offset
        msg["%sheight" %uniq] = obj.height
        msg["%swidth" %uniq] = obj.width
        msg["%sdo_rectify" %uniq] = obj.do_rectify
        return(msg)

    def laser(cls, obj, uniq):
        msg = {}
        msg["%sangle_min" %uniq] = obj.angle_min
        msg["%sangle_max" %uniq] = obj.angle_max
        msg["%sangle_increment" %uniq] = obj.angle_increment
        msg["%stime_increment" %uniq] = obj.time_increment
        msg["%sscan_time" %uniq] = obj.scan_time
        msg["%srange_min" %uniq] = obj.range_min
        msg["%srange_max" %uniq] = obj.range_max
        return(msg)

# ------------------ SR_Robot Messages -----------------------------
    def biotacs(cls, obj, uniq):
        msg = {}
        msg["%s_pac0" %uniq] = obj.pac0
        msg["%s_pac1" %uniq] = obj.pac1
        msg["%s_pdc" %uniq] = obj.pdc
        msg["%s_tac" %uniq] = obj.tac
        msg["%s_tdc" %uniq] = obj.tdc
        msg["%s_electrodes" %uniq] = obj.electrodes
        return(msg)

    def grasp_points(cls, obj, uniq):
        msg = {}
        msg["%s_positions" %uniq] = obj.positions
        msg["%s_velocities" %uniq] = obj.velocities
        msg["%s_accelerations" %uniq] = obj.accelerations
        msg["%s_effort" %uniq] = obj.effort
        msg["%s_time_from_start" %uniq] = obj.time_from_start
        return(msg)

    def tip(cls, obj, uniq):
        msg = {}
        msg["%s_tip_name" %uniq] = obj.tip_name
        msg["%s_tip_pos_x" %uniq] = obj.tip_pos_x
        msg["%s_tip_pos_y" %uniq] = obj.tip_pos_y
        msg["%s_tip_pos_z" %uniq] = obj.tip_pos_z
        msg["%s_tip_orientation_rho" %uniq] = obj.tip_orientation_rho
        msg["%s_tip_orientation_theta" %uniq] = obj.tip_orientation_theta
        msg["%s_tip_orientation_sigma" %uniq] = obj.tip_orientation_sigma
        return(msg)

    def joint(cls, obj, uniq):
        msg = {}
        msg["%s_joint_name" %uniq] = obj.joint_name
        msg["%s_joint_position" %uniq] = obj.joint_position
        msg["%s_joint_target" %uniq] = obj.joint_target
        msg["%s_joint_torque" %uniq] = obj.joint_torque
        msg["%s_joint_temperature" %uniq] = obj.joint_temperature
        msg["%s_joint_current" %uniq] = obj.joint_current
        msg["%s_error_flag" %uniq] = obj.error_flag
        return(msg)

# =========================== Decode Functions ===========================================

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
    def header(cls, msg, obj, uniq):
        obj.seq = msg['%sseq' %uniq]
        obj.stamp.secs = msg['%ssecs' %uniq]
        obj.stamp.nsecs = msg['%snsecs' %uniq]
        obj.frame_id = msg['%sframe_id' %uniq]
        return(obj)

# ------------------ Geometry Messages -----------------------------
    def angular(cls, msg, obj, uniq):
        obj.x = msg['%s_ang_x' %uniq]
        obj.y = msg['%s_ang_y' %uniq]
        obj.z = msg['%s_ang_z' %uniq]
        return(obj)

    def com(cls, msg, obj, uniq):
        obj.x = msg['%s_com_x' %uniq]
        obj.y = msg['%s_com_y' %uniq]
        obj.z = msg['%s_com_z' %uniq]
        return(obj)

    def covariance(cls, msg, obj, uniq):
        obj.covariance = msg['%s_covariance' %uniq]
        return(obj)

    def force(cls, msg, obj, uniq):
        obj.x = msg['%s_force_x' %uniq]
        obj.y = msg['%s_force_y' %uniq]
        obj.z = msg['%s_force_z' %uniq]
        return(obj)

    def inertia(cls, msg, obj, uniq):
        obj.ixx = msg['%s_ixx' %uniq]
        obj.ixy = msg['%s_ixy' %uniq]
        obj.ixz = msg['%s_ixz' %uniq]
        obj.iyy = msg['%s_iyy' %uniq]
        obj.iyz = msg['%s_iyz' %uniq]
        obj.izz = msg['%s_izz' %uniq]
        return(obj)

    def linear(cls, msg, obj, uniq):
        obj.x = msg['%s_lin_x' %uniq]
        obj.y = msg['%s_lin_y' %uniq]
        obj.z = msg['%s_lin_z' %uniq]
        return(obj)

    def orientation(cls, msg, obj, uniq):
        obj.x = msg['%s_orient_x' %uniq]
        obj.y = msg['%s_orient_y' %uniq]
        obj.z = msg['%s_orient_z' %uniq]
        obj.w = msg['%s_orient_w' %uniq]
        return(obj)

    def point(cls, msg, obj, uniq):
        obj.x = msg['%s_pnt_x' %uniq]
        obj.y = msg['%s_pnt_y' %uniq]
        obj.z = msg['%s_pnt_z' %uniq]
        return(obj)

    def position(cls, msg, obj, uniq):
        obj.x = msg['%s_pos_x' %uniq]
        obj.y = msg['%s_pos_y' %uniq]
        obj.z = msg['%s_pos_z' %uniq]
        return(obj)

    def quaternion(cls, msg, obj, uniq):
        obj.x = msg['%s_quat_x' %uniq]
        obj.y = msg['%s_quat_y' %uniq]
        obj.z = msg['%s_quat_z' %uniq]
        obj.w = msg['%s_quat_w' %uniq]
        return(obj)

    def rotation(cls, msg, obj, uniq):
        obj.x = msg['%s_rot_x' %uniq]
        obj.y = msg['%s_rot_y' %uniq]
        obj.z = msg['%s_rot_z' %uniq]
        obj.w = msg['%s_rot_w' %uniq]
        return(obj)

    def torque(cls, msg, obj, uniq):
        obj.x = msg['%s_torq_x' %uniq]
        obj.y = msg['%s_torq_y' %uniq]
        obj.z = msg['%s_torq_z' %uniq]
        return(obj)

    def translation(cls, msg, obj, uniq):
        obj.x = msg['%s_trans_x' %uniq]
        obj.y = msg['%s_trans_y' %uniq]
        obj.z = msg['%s_trans_z' %uniq]
        return(obj)

    def vector(cls, msg, obj, uniq):
        obj.x = msg['%s_vect_x' %uniq]
        obj.y = msg['%s_vect_y' %uniq]
        obj.z = msg['%s_vect_z' %uniq]
        return(obj)

# ------------------ Sensor Messages -----------------------------

    def roi(cls, msg, obj, uniq): # region_of_interest
        obj.x_offset = msg["%sx_offset" %uniq]
        obj.y_offset = msg["%sy_offset" %uniq]
        obj.height = msg["%sheight" %uniq]
        obj.width = msg["%swidth" %uniq]
        obj.do_rectify = msg["%sdo_rectify" %uniq]
        return(obj)

    def laser(cls, msg, obj, uniq):
        obj.angle_min = msg["%sangle_min" %uniq]
        obj.angle_max = msg["%sangle_max" %uniq]
        obj.angle_increment = msg["%sangle_increment" %uniq]
        obj.time_increment = msg["%stime_increment" %uniq]
        obj.scan_time = msg["%sscan_time" %uniq]
        obj.range_min = msg["%srange_min" %uniq]
        obj.range_max = msg["%srange_max" %uniq]
        return(obj)

# ------------------ SR_Robot Messages -----------------------------
    def biotacs(cls, msg, obj, uniq):
        obj.pac0 = msg["%s_pac0" %uniq]
        obj.pac1 = msg["%s_pac1" %uniq]
        obj.pdc = msg["%s_pdc" %uniq]
        obj.tac = msg["%s_tac" %uniq]
        obj.tdc = msg["%s_tdc" %uniq]
        obj.electrodes = msg["%s_electrodes" %uniq]
        return(obj)

    def grasp_points(cls, msg, obj, uniq):
        obj.positions = msg["%s_positions" %uniq]
        obj.velocities = msg["%s_velocities" %uniq]
        obj.accelerations = msg["%s_accelerations" %uniq]
        obj.effort = msg["%s_effort" %uniq]
        obj.time_from_start = msg["%s_time_from_start" %uniq]
        return(obj)

    def tip(cls, msg, obj, uniq):
        obj.tip_name = msg["%s_tip_name" %uniq]
        obj.tip_pos_x = msg["%s_tip_pos_x" %uniq]
        obj.tip_pos_y = msg["%s_tip_pos_y" %uniq]
        obj.tip_pos_z = msg["%s_tip_pos_z" %uniq]
        obj.tip_orientation_rho = msg["%s_tip_orientation_rho" %uniq]
        obj.tip_orientation_theta = msg["%s_tip_orientation_theta" %uniq]
        obj.tip_orientation_sigma = msg["%s_tip_orientation_sigma" %uniq]
        return(obj)

    def joint(cls, msg, obj, uniq):
        obj.joint_name = msg["%s_joint_name" %uniq]
        obj.joint_position = msg["%s_joint_position" %uniq]
        obj.joint_target = msg["%s_joint_target" %uniq]
        obj.joint_torque = msg["%s_joint_torque" %uniq]
        obj.joint_temperature = msg["%s_joint_temperature" %uniq]
        obj.joint_current = msg["%s_joint_current" %uniq]
        obj.error_flag = msg["%s_error_flag" %uniq]
        return(obj)


from rospy_msgpack import interpret

encode = interpret.Encode()
decode = interpret.Decode()

# msg["key"] = obj.path.attribute
class Encode():
    def __init__(self):
        pass

    def camera_info(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['height'] = obj.height
        msg['width'] = obj.width
        msg['distortion_model'] = obj.distortion_model
        msg['D'] = obj.D
        msg["K"] = obj.K
        msg["R"] = obj.R
        msg["P"] = obj.P
        msg["binning_x"] = obj.binning_x
        msg["binning_y"] = obj.binning_y
        r = encode.roi(obj.roi, "")
        msg.update(h)
        msg.update(r)
        return(msg)

    def channel_float32(cls, obj):
        msg = {}
        msg["name"] = obj.name
        msg["values"] = obj.values
        return(msg)

    def compressed_image(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["format"] = obj.format
        msg["data"] = obj.data
        msg.update(h)
        return(msg)

    def fluid_pressure(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["fluid_pressure"] = obj.fluid_pressure
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def illuminance(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["illuminance"] = obj.illuminance
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def image(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["height"] = obj.height
        msg["width"] = obj.width
        msg["encoding"] = obj.encoding
        msg["is_bigedian"] = obj.is_bigedian
        msg["step"] = obj.step
        msg["data"] = obj.data
        msg.update(h)
        return(msg)

    def imu(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        o = encode.orientation(obj.orientation, "")
        msg["orientation_covariance"] = obj.orientation_covariance
        av = encode.xyz(obj.angular_velocity, "ang_", "velo")
        # msg["ax"] = obj.angular_velocity.x
        # msg["ay"] = obj.angular_velocity.y
        # msg["az"] = obj.angular_velocity.z
        msg["angular_velocity_covariance"] = obj.angular_velocity_covariance
        la = encode.xyz(obj.linear_acceleration, "lin_", "accel")
        # msg["lx"] = obj.linear_acceleration.x
        # msg["ly"] = obj.linear_acceleration.y
        # msg["lz"] = obj.linear_acceleration.z
        msg["linear_acceleration_covariance"] = obj.linear_acceleration_covariance
        msg.update(h)
        msg.update(o)
        msg.update(av)
        msg.update(la)
        return(msg)

    def joint_state(self, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['name'] = obj.name
        msg['position'] = obj.position
        msg['velocity'] = obj.velocity
        msg['effort'] = obj.effort
        msg.update(h)
        return(msg)

    def joy(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["axes"] = obj.axes
        msg["buttons"] = obj.buttons
        msg.update(h)
        return(msg)

    # def joy_feedback(cls, obj):
    #     msg = {}

    # def joy_feedback_array(cls, obj):
    #     msg = {}
    #

    def laser_echo(cls, obj):
        msg = {}
        msg["echoes"] = obj.echoes
        return(msg)

    def laser_scan(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.laser(obj, "")
        # msg["angle_min"] = obj.angle_min
        # msg["angle_max"] = obj.angle_max
        # msg["angle_increment"] = obj.angle_increment
        # msg["time_increment"] = obj.time_increment
        # msg["scan_time"] = obj.scan_time
        # msg["range_min"] = obj.range_min
        # msg["range_max"] = obj.range_max
        msg["ranges"] = obj.ranges
        msg["intensities"] = obj.intensities
        msg.update(h)
        msg.update(l)
        return(msg)

    def magnetic_field(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        mf = encode.xyz(obj.magnetic_field, "", "mag")
        # msg["x"] = obj.magnetic_field.x
        # msg["y"] = obj.magnetic_field.y
        # msg["z"] = obj.magnetic_field.z
        msg["magnetic_field_covariance"] = obj.magnetic_field_covariance
        msg.update(h)
        msg.update(mf)
        return(msg)

    def multi_dof_joint_state(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["joint_names"] = obj.joint_names
        for i in msg['joint_names']:
            tr = encode.translation(obj.transforms[i].translation, i)
            r = encode.rotation(obj.transforms[i].rotation, i)
            l = encode.linear(obj.twist[i].linear, i)
            a = encode.angular(obj.twist[i].angular, i)
            f = encode.force(obj.wrench[i].force, i)
            tq = encode.torque(obj.wrench[i].torque, i)
            msg.update(tr)
            msg.update(r)
            msg.update(l)
            msg.update(a)
            msg.update(f)
            msg.update(tq)
        msg.update(h)
        return(msg)

    def multi_echo_laser_scan(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.laser(obj, "")
        # msg["angle_min"] = obj.angle_min
        # msg["angle_max"] = obj.angle_max
        # msg["angle_increment"] = obj.angle_increment
        # msg["time_increment"] = obj.time_increment
        # msg["scan_time"] = obj.scan_time
        # msg["range_min"] = obj.range_min
        # msg["range_max"] = obj.range_max
        msg["rechoes"] = obj.ranges.echoes
        msg["iechoes"] = obj.intensities.echoes
        msg.update(h)
        msg.update(l)
        return(msg)

    # def nav_sat_fix(cls, obj):
    #     msg = {}
    #

    # def nav_sat_status(cls, obj):
    #     msg = {}
    #

    def point_cloud(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        p = encode.point(obj.points, "")
        # msg["x"] = obj.points.x
        # msg["y"] = obj.points.y
        # msg["z"] = obj.points.z
        msg["name"] = obj.channels.name
        msg["values"] = obj.channels.values
        msg. update(h)
        msg.update(p)
        return(msg)

    # def point_cloud_2(cls, obj):
    #     msg = {}
    #     h = encode.header(obj.header, "")
    #     msg["height"] = obj.height
    #     msg["width"] = obj.width

    # def point_field(cls, obj):
    #     msg = {}
    #

    # def range(cls, obj):
    #     msg = {}
    #

    def region_of_interest(cls, obj):
        msg = {}
        r = encode.roi(obj, "")
        msg.update(r)
        return(msg)

    def relative_humidity(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["relative_humidity"] = obj.relative_humidity
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def temperature(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["temperature"] = obj.temperature
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def time_reference(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["time_ref"] = obj.time_ref
        msg["source"] = obj.source
        msg.update(h)
        return(msg)


# ==========================================================================================


class Decode():
    def __init__(self):
        pass


    def camera_info(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.height = msg['height']
        obj.width = msg['width']
        obj.distortion_model = msg['distortion_model']
        obj.D = msg['D']
        obj.K = msg["K"]
        obj.R = msg["R"]
        obj.P = msg["P"]
        obj.binning_x = msg["binning_x"]
        obj.binning_y = msg["binning_y"]
        obj.roi = decode.roi(msg, obj.roi, "")
        return(obj)

    def channel_float32(cls, msg, obj):
        obj.name = msg["name"]
        obj.values = msg["values"]
        return(obj)

    def compressed_image(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.format = msg["format"]
        obj.data = msg["data"]
        return(obj)

    def fluid_pressure(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.fluid_pressure = msg["fluid_pressure"]
        obj.variance = msg["variance"]
        return(obj)

    def illuminance(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.illuminance = msg["illuminance"]
        obj.variance = msg["variance"]
        return(obj)

    def image(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.height = msg["height"]
        obj.width = msg["width"]
        obj.encoding = msg["encoding"]
        obj.is_bigedian = msg["is_bigedian"]
        obj.step = msg["step"]
        obj.data = msg["data"]
        return(obj)

    def imu(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.orientation = decode.orientation(msg, obj.orientation, "")
        obj.orientation_covariance = msg["orientation_covariance"]
        obj.angular_velocity = decode.xyz(msg, obj.angular_velocity, "ang_", "velo")
        # obj.angular_velocity.x = msg["ax"]
        # obj.angular_velocity.y = msg["ay"]
        # obj.angular_velocity.z = msg["az"]
        obj.angular_velocity_covariance = msg["angular_velocity_covariance"]
        obj.linear_acceleration = decode.xyz(msg, obj.linear_acceleration, "lin_", "accel")
        # obj.linear_acceleration.x = msg["lx"]
        # obj.linear_acceleration.y = msg["ly"]
        # obj.linear_acceleration.z = msg["lz"]
        obj.linear_acceleration_covariance = msg["linear_acceleration_covariance"]
        return(obj)

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

    def joy(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.axes = msg["axes"]
        obj.buttons = msg["buttons"]
        return(obj)

    def laser_echo(cls, obj):
        obj.echoes = msg["echoes"]
        return(obj)

    def laser_scan(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj = decode.laser(msg, obj, "")
        # obj.angle_min = msg["angle_min"]
        # obj.angle_max = msg["angle_max"]
        # obj.angle_increment = msg["angle_increment"]
        # obj.time_increment = msg["time_increment"]
        # obj.scan_time = msg["scan_time"]
        # obj.range_min = msg["range_min"]
        # obj.range_max = msg["range_max"]
        obj.ranges = msg["ranges"]
        obj.intensities = msg["intensities"]
        return(obj)

    def magnetic_field(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.magnetic_field = decode.xyz(msg, obj.magnetic_field, "", "mag")
        # obj.magnetic_field.x = msg["x"]
        # obj.magnetic_field.y = msg["y"]
        # obj.magnetic_field.z = msg["z"]
        obj.magnetic_field_covariance = msg["magnetic_field_covariance"]
        return(obj)

    def multi_dof_joint_state(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.joint_names = msg["joint_names"]
        for i in msg['joint_names']:
            obj.transforms[i].translation = decode.translation(msg, obj.transforms[i].translation, i)
            obj.transforms[i].rotation = decode.rotation(msg, obj.transforms[i].rotation, i)
            obj.twist[i].linear = decode.linear(msg, obj.twist[i].linear, i)
            obj.twist[i].angular = decode.angular(msg, obj.twist[i].angular, i)
            obj.wrench[i].force = decode.force(msg, obj.wrench[i].force, i)
            obj.wrench[i].torque = decode.torque(msg, obj.wrench[i].torque, i)
        return(obj)

    def multi_echo_laser_scan(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj = decode.laser(msg, obj, "")
        # obj.angle_min = msg["angle_min"]
        # obj.angle_max = msg["angle_max"]
        # obj.angle_increment = msg["angle_increment"]
        # obj.time_increment = msg["time_increment"]
        # obj.scan_time = msg["scan_time"]
        # obj.range_min = msg["range_min"]
        # obj.range_max = msg["range_max"]
        obj.ranges.echoes = msg["rechoes"]
        obj.intensities.echoes = msg["iechoes"]
        return(obj)

    def point_cloud(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.points = decode.point(msg, obj.points, "")
        # obj.points.x = msg["x"]
        # obj.points.y = msg["y"]
        # obj.points.z = msg["z"]
        obj.channels.name = msg["name"]
        obj.channels.values = msg["values"]
        return(obj)

    def region_of_interest(cls, msg, obj):
        obj = decode.roi(msg, obj, "")
        return(obj)

    def relative_humidity(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.relative_humidity = msg["relative_humidity"]
        obj.variance = msg["variance"]
        return(obj)

    def temperature(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.temperature = msg["temperature"]
        obj.variance = msg["variance"]
        return(obj)

    def time_reference(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.time_ref = msg["time_ref"]
        obj.source = msg["source"]
        return(obj)

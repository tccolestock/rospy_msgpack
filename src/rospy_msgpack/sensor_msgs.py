
from rospy_msgpack import header

# msg["key"] = obj.path.attribute
class Encode():
    def __init__(self):
        pass

    def camera_info(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg['height'] = obj.height
        msg['width'] = obj.width
        msg['distortion_model'] = obj.distortion_model
        msg['D'] = obj.D
        msg["K"] = obj.K
        msg["R"] = obj.R
        msg["P"] = obj.P
        msg["binning_x"] = obj.binning_x
        msg["binning_y"] = obj.binning_y
        msg["x_offset"] = obj.roi.x_offset
        msg["y_offset"] = obj.roi.y_offset
        msg["rheight"] = obj.roi.height
        msg["rwidth"] = obj.roi.width
        msg["do_rectify"] = obj.roi.do_rectify
        msg.update(h)
        return(msg)

    def channel_float32(cls, obj):
        msg = {}
        msg["name"] = obj.name
        msg["values"] = obj.values
        return(msg)

    def compressed_image(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg["format"] = obj.format
        msg["data"] = obj.data
        msg.update(h)
        return(msg)

    def fluid_pressure(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg["fluid_pressure"] = obj.fluid_pressure
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def illuminance(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
        msg["illuminance"] = obj.illuminance
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def image(cls, obj):
        msg = {}
        h = header.Header().encode(obj)
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
        h = header.Header().endcode(obj)
        msg["ox"] = obj.orientation.x
        msg["oy"] = obj.orientation.y
        msg["oz"] = obj.orientation.z
        msg["ow"] = obj.orientation.w
        msg["orientation_covariance"] = obj.orientation_covariance
        msg["ax"] = obj.angular_velocity.x
        msg["ay"] = obj.angular_velocity.y
        msg["az"] = obj.angular_velocity.z
        msg["angular_velocity_covariance"] = obj.angular_velocity_covariance
        msg["lx"] = obj.linear_acceleration.x
        msg["ly"] = obj.linear_acceleration.y
        msg["lz"] = obj.linear_acceleration.z
        msg["linear_acceleration_covariance"] = obj.linear_acceleration_covariance
        msg.update(h)
        return(msg)

    def joint_state(self, obj):
        msg = {}
        msg['seq'] = obj.header.seq
        msg['secs'] = obj.header.stamp.secs
        msg['nsecs'] = obj.header.stamp.nsecs
        msg['frame_id'] = obj.header.frame_id
        msg['name'] = obj.name
        msg['position'] = obj.position
        msg['velocity'] = obj.velocity
        msg['effort'] = obj.effort
        return(msg)

    def joy(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
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
        h = header.Header().endcode(obj)
        msg["angle_min"] = obj.angle_min
        msg["angle_max"] = obj.angle_max
        msg["angle_increment"] = obj.angle_increment
        msg["time_increment"] = obj.time_increment
        msg["scan_time"] = obj.scan_time
        msg["range_min"] = obj.range_min
        msg["range_max"] = obj.range_max
        msg["ranges"] = obj.ranges
        msg["intensities"] = obj.intensities
        msg.update(h)
        return(msg)

    def magnetic_field(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["x"] = obj.magnetic_field.x
        msg["y"] = obj.magnetic_field.y
        msg["z"] = obj.magnetic_field.z
        msg["magnetic_field_covariance"] = obj.magnetic_field_covariance
        msg.update(h)
        return(msg)

    def multi_dof_joint_state(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["joint_names"] = obj.joint_names
        msg["tx"] = obj.transforms.translation.x
        msg["ty"] = obj.transforms.translation.y
        msg["tz"] = obj.transforms.translation.z
        msg["rx"] = obj.transforms.rotation.x
        msg["ry"] = obj.transforms.rotation.y
        msg["rz"] = obj.transforms.rotation.z
        msg["rw"] = obj.transforms.rotation.w

        msg["lx"] = obj.twist.linear.x
        msg["ly"] = obj.twist.linear.y
        msg["lz"] = obj.twist.linear.z
        msg["ax"] = obj.twist.angular.x
        msg["ay"] = obj.twist.angular.y
        msg["az"] = obj.twist.angular.z

        msg["fx"] = obj.wrench.force.x
        msg["fy"] = obj.wrench.force.y
        msg["fz"] = obj.wrench.force.z
        msg["qx"] = obj.wrench.torque.x
        msg["qy"] = obj.wrench.torque.y
        msg["qz"] = obj.wrench.torque.z
        msg.update(h)
        return(msg)

    def multi_echo_laser_scan(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["angle_min"] = obj.angle_min
        msg["angle_max"] = obj.angle_max
        msg["angle_increment"] = obj.angle_increment
        msg["time_increment"] = obj.time_increment
        msg["scan_time"] = obj.scan_time
        msg["range_min"] = obj.range_min
        msg["range_max"] = obj.range_max
        msg["rechoes"] = obj.ranges.echoes
        msg["iechoes"] = obj.intensities.echoes
        msg.update(h)
        return(msg)

    # def nav_sat_fix(cls, obj):
    #     msg = {}
    #

    # def nav_sat_status(cls, obj):
    #     msg = {}
    #

    def point_cloud(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["x"] = obj.points.x
        msg["y"] = obj.points.y
        msg["z"] = obj.points.z
        msg["name"] = obj.channels.name
        msg["values"] = obj.channels.values
        msg. update(h)
        return(msg)

    # def point_cloud_2(cls, obj):
    #     msg = {}
    #     h = header.Header().endcode(obj)
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
        msg["x_offset"] = obj.x_offset
        msg["y_offset"] = obj.y_offset
        msg["height"] = obj.height
        msg["width"] = obj.width
        msg["do_rectify"] = obj.do_rectify
        return(msg)

    def relative_humidity(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["relative_humidity"] = obj.relative_humidity
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def temperature(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["temperature"] = obj.temperature
        msg["variance"] = obj.variance
        msg.update(h)
        return(msg)

    def time_reference(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["time_ref"] = obj.time_ref
        msg["source"] = obj.source
        msg.update(h)
        return(msg)


# ==========================================================================================


class Decode():
    def __init__(self):
        pass


    def camera_info(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.height = msg['height']
        obj.width = msg['width']
        obj.distortion_model = msg['distortion_model']
        obj.D = msg['D']
        obj.K = msg["K"]
        obj.R = msg["R"]
        obj.P = msg["P"]
        obj.binning_x = msg["binning_x"]
        obj.binning_y = msg["binning_y"]
        obj.roi.x_offset = msg["x_offset"]
        obj.roi.y_offset = msg["y_offset"]
        obj.roi.height = msg["rheight"]
        obj.roi.width = msg["rwidth"]
        obj.roi.do_rectify = msg["do_rectify"]
        return(obj)

    def channel_float32(cls, msg, obj):
        obj.name = msg["name"]
        obj.values = msg["values"]
        return(obj)

    def compressed_image(cls, msg, obj):
        obj = header.Header().encode(msg, obj)
        obj.format = msg["format"]
        obj.data = msg["data"]
        return(obj)

    def fluid_pressure(cls, msg, obj):
        obj = header.Header().encode(msg, obj)
        obj.fluid_pressure = msg["fluid_pressure"]
        obj.variance = msg["variance"]
        return(obj)

    def illuminance(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.illuminance = msg["illuminance"]
        obj.variance = msg["variance"]
        return(obj)

    def image(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.height = msg["height"]
        obj.width = msg["width"]
        obj.encoding = msg["encoding"]
        obj.is_bigedian = msg["is_bigedian"]
        obj.step = msg["step"]
        obj.data = msg["data"]
        return(obj)

    def imu(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.orientation.x = msg["ox"]
        obj.orientation.y = msg["oy"]
        obj.orientation.z = msg["oz"]
        obj.orientation.w = msg["ow"]
        obj.orientation_covariance = msg["orientation_covariance"]
        obj.angular_velocity.x = msg["ax"]
        obj.angular_velocity.y = msg["ay"]
        obj.angular_velocity.z = msg["az"]
        obj.angular_velocity_covariance = msg["angular_velocity_covariance"]
        obj.linear_acceleration.x = msg["lx"]
        obj.linear_acceleration.y = msg["ly"]
        obj.linear_acceleration.z = msg["lz"]
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
        obj = header.Header().decode(msg, obj)
        obj.axes = msg["axes"]
        obj.buttons = msg["buttons"]
        return(obj)

    def laser_echo(cls, obj):
        obj.echoes = msg["echoes"]
        return(obj)

    def laser_scan(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.angle_min = msg["angle_min"]
        obj.angle_max = msg["angle_max"]
        obj.angle_increment = msg["angle_increment"]
        obj.time_increment = msg["time_increment"]
        obj.scan_time = msg["scan_time"]
        obj.range_min = msg["range_min"]
        obj.range_max = msg["range_max"]
        obj.ranges = msg["ranges"]
        obj.intensities = msg["intensities"]
        return(obj)

    def magnetic_field(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.magnetic_field.x = msg["x"]
        obj.magnetic_field.y = msg["y"]
        obj.magnetic_field.z = msg["z"]
        obj.magnetic_field_covariance = msg["magnetic_field_covariance"]
        return(obj)

    def multi_dof_joint_state(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.joint_names = msg["joint_names"]
        obj.transforms.translation.x = msg["tx"]
        obj.transforms.translation.y = msg["ty"]
        obj.transforms.translation.z = msg["tz"]
        obj.transforms.rotation.x = msg["rx"]
        obj.transforms.rotation.y = msg["ry"]
        obj.transforms.rotation.z = msg["rz"]
        obj.transforms.rotation.w = msg["rw"]
        obj.twist.linear.x = msg["lx"]
        obj.twist.linear.y = msg["ly"]
        obj.twist.linear.z = msg["lz"]
        obj.twist.angular.x = msg["ax"]
        obj.twist.angular.y = msg["ay"]
        obj.twist.angular.z = msg["az"]
        obj.wrench.force.x = msg["fx"]
        obj.wrench.force.y = msg["fy"]
        obj.wrench.force.z = msg["fz"]
        obj.wrench.torque.x = msg["qx"]
        obj.wrench.torque.y = msg["qy"]
        obj.wrench.torque.z = msg["qz"]
        return(obj)

    def multi_echo_laser_scan(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.angle_min = msg["angle_min"]
        obj.angle_max = msg["angle_max"]
        obj.angle_increment = msg["angle_increment"]
        obj.time_increment = msg["time_increment"]
        obj.scan_time = msg["scan_time"]
        obj.range_min = msg["range_min"]
        obj.range_max = msg["range_max"]
        obj.ranges.echoes = msg["rechoes"]
        obj.intensities.echoes = msg["iechoes"]
        return(obj)

    def point_cloud(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.points.x = msg["x"]
        obj.points.y = msg["y"]
        obj.points.z = msg["z"]
        obj.channels.name = msg["name"]
        obj.channels.values = msg["values"]
        return(obj)

    def region_of_interest(cls, msg, obj):
        obj.x_offset = msg["x_offset"]
        obj.y_offset = msg["y_offset"]
        obj.height = msg["height"]
        obj.width = msg["width"]
        obj.do_rectify = msg["do_rectify"]
        return(obj)

    def relative_humidity(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.relative_humidity = msg["relative_humidity"]
        obj.variance = msg["variance"]
        return(obj)

    def temperature(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.temperature = msg["temperature"]
        obj.variance = msg["variance"]
        return(obj)

    def time_reference(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.time_ref = msg["time_ref"]
        obj.source = msg["source"]
        return(obj)

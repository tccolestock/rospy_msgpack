
from rospy_msgpack import interpret
from sensor_msgs.msg import JoyFeedback, LaserEcho, ChannelFloat32, PointField
from geometry_msgs.msg import Transform, Twist, Wrench, Point32

encode = interpret.Encode()
decode = interpret.Decode()

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
        msg["angular_velocity_covariance"] = obj.angular_velocity_covariance
        la = encode.xyz(obj.linear_acceleration, "lin_", "accel")
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

    def joy_feedback(cls, obj):
        msg = {}
        msg['type'] = obj.type
        msg['id'] = obj.id
        msg['intensity'] = intensity
        return(msg)

    def joy_feedback_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.array)
        for i in range(msg['_length']):
            msg['%s_type' %i] = obj.array[i].type
            msg['%s_id' %i] = obj.array[i].id
            msg['%s_intensity' %i] = obj.array[i].intensity
        return(msg)

    def laser_echo(cls, obj):
        msg = {}
        msg["echoes"] = obj.echoes
        return(msg)

    def laser_scan(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.laser(obj, "")
        msg["ranges"] = obj.ranges
        msg["intensities"] = obj.intensities
        msg.update(h)
        msg.update(l)
        return(msg)

    def magnetic_field(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        mf = encode.xyz(obj.magnetic_field, "", "mag")
        msg["magnetic_field_covariance"] = obj.magnetic_field_covariance
        msg.update(h)
        msg.update(mf)
        return(msg)

    def multi_dof_joint_state(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg["joint_names"] = obj.joint_names
        msg['_length_trans'] = len(obj.transforms)
        msg['_length_twist'] = len(obj.twist)
        msg['_length_wrench'] = len(obj.wrench)
        for i in msg['_length_trans']:
            tr = encode.translation(obj.transforms[i].translation, i)
            r = encode.rotation(obj.transforms[i].rotation, i)
            msg.update(tr)
            msg.update(r)
        for i in msg['_length_twist']:
            l = encode.linear(obj.twist[i].linear, i)
            a = encode.angular(obj.twist[i].angular, i)
            msg.update(l)
            msg.update(a)
        for i in msg['_length_wrench']:
            f = encode.force(obj.wrench[i].force, i)
            tq = encode.torque(obj.wrench[i].torque, i)
            msg.update(f)
            msg.update(tq)
        return(msg)

    def multi_echo_laser_scan(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        l = encode.laser(obj, "")
        msg['_length_ranges'] = len(obj.ranges)
        msg['_length_intensities'] = len(obj.intensities)
        for i in range(msg['_length_ranges']):
            msg["%s_rechoes" %i] = obj.ranges[i].echoes
        for i in range(msg['_length_intensities']):
            msg["%s_iechoes" %i] = obj.intensities[i].echoes
        msg.update(h)
        msg.update(l)
        return(msg)

    def nav_sat_fix(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['status'] = obj.status.status
        msg['service'] = obj.status.service
        msg['lat'] = obj.latitude
        msg['long'] = obj.longitude
        msg['alt'] = obj.altitude
        msg['pos_covar'] = obj.position_covariance
        msg['pos_cavar_type'] = obj.position_covariance_type
        msg.update(h)
        return(msg)

    def nav_sat_status(cls, obj):
        msg = {}
        msg['status'] = obj.status
        msg['service'] = obj.service
        return(msg)


    def point_cloud(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg['_length_points'] = len(obj.points)
        msg['_length_channels'] = len(obj.channels)
        for i in range(msg['_length_points']):
            p = encode.point(obj.points[i], i)
            msg.update(p)
        for i in range(msg['_length_channels']):
            msg["%s_name" %i] = obj.channels[i].name
            msg["%s_values" %i] = obj.channels[i].values
        msg. update(h)
        return(msg)

    def point_cloud_2(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg["height"] = obj.height
        msg["width"] = obj.width
        msg['_length'] = len(obj.fields)
        for i in range(msg['_length']):
            msg['%s_name' %i] = obj.fields[i].name
            msg['%s_offset' %i] = obj.fields[i].offset
            msg['%s_datatype' %i] = obj.fields[i].datatype
            msg['%s_count' %i] = obj.fields[i].count
        msg['is_bigedian'] = obj.is_bigedian
        msg['point_step'] = obj.point_step
        msg['row_step'] = obj.row_step
        msg['data'] = obj.data
        msg['is_dense'] = obj.is_dense
        return(msg)

    def point_field(cls, obj):
        msg = {}
        msg['name'] = obj.name
        msg['offset'] = obj.offset
        msg['datatype'] = obj.datatype
        msg['count'] = obj.count
        return(msg)

    def range(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        msg['radiation_type'] = obj.radiation_type
        msg['field_of_view'] = obj.field_of_view
        msg['min_range'] = obj.min_range
        msg['max_range'] = obj.max_range
        msg['range'] = obj.range
        return(msg)


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
        obj.angular_velocity_covariance = msg["angular_velocity_covariance"]
        obj.linear_acceleration = decode.xyz(msg, obj.linear_acceleration, "lin_", "accel")
        obj.linear_acceleration_covariance = msg["linear_acceleration_covariance"]
        return(obj)

    def joint_state(self, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
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

    def joy_feedback(cls, msg, obj):
        obj.type = msg['type']
        obj.id = msg['id']
        intensity = msg['intensity']
        return(obj)

    def joy_feedback_array(cls, msg, obj):
        for i in range(msg['_length']):
            jf = JoyFeedback()
            jf.type = msg['%s_type' %i]
            jf.id = msg['%s_id' %i]
            jf.intensity = msg['%s_intensity' %i]
            obj.array.append(jf)
        return(obj)

    def laser_echo(cls, obj):
        obj.echoes = msg["echoes"]
        return(obj)

    def laser_scan(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj = decode.laser(msg, obj, "")
        obj.ranges = msg["ranges"]
        obj.intensities = msg["intensities"]
        return(obj)

    def magnetic_field(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.magnetic_field = decode.xyz(msg, obj.magnetic_field, "", "mag")
        obj.magnetic_field_covariance = msg["magnetic_field_covariance"]
        return(obj)

    def multi_dof_joint_state(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.joint_names = msg["joint_names"]
        for i in msg['_length_trans']:
            trans = Transform()
            trans.translation = decode.translation(msg, trans.translation, i)
            trans.rotation = decode.rotation(msg, trans.rotation, i)
            obj.transforms.append(trans)
        for i in msg['_length_twist']:
            tw = Twist()
            tw.linear = decode.linear(msg, tw.linear, i)
            tw.angular = decode.angular(msg, tw.angular, i)
            obj.twist.append(twist)
        for i in msg['_length_twist']:
            wr = Wrench()
            wr.force = decode.force(msg, wr.force, i)
            wr.torque = decode.torque(msg, wr.torque, i)
            obj.wrench.append(wr)
        return(obj)

    def multi_echo_laser_scan(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj = decode.laser(msg, obj, "")
        for i in range(msg['_length_ranges']):
            ler = LaserEcho() # laser echo ranges
            ler.echoes = msg["%s_rechoes" %i]
            obj.ranges.append(ler)
        for i in range(msg['_length_intensities']):
            lei = LaserEcho() # laser echo intensities
            lei.echoes = msg["%s_iechoes" %i]
            obj.intensities.append(lei)
        return(obj)

    def nav_sat_fix(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.status.status = msg['status']
        obj.status.service = msg['service']
        obj.latitude = msg['lat']
        obj.longitude = msg['long']
        obj.altitude = msg['alt']
        obj.position_covariance = msg['pos_covar']
        obj.position_covariance_type = msg['pos_cavar_type']
        return(obj)

    def nav_sat_status(cls, msg, obj):
        obj.status = msg['status']
        obj.service = msg['service']
        return(obj)

    def point_cloud(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(msg['_length_points']):
            pnt = Point32()
            pnt = decode.point(msg, pnt, i)
            obj.points.append(png)
        for i in range(msg['_length_channels']):
            ch = ChannelFloat32()
            ch.name = msg["%s_name" %i]
            ch.values = msg["%s_values" %i]
            obj.channels.append(ch)
        return(obj)

    def point_cloud_2(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.height = msg["height"]
        obj.width = msg["width"]
        for i in range(msg['_length']):
            pf = PointField()
            pf.name = msg['%s_name' %i]
            pf.offset = msg['%s_offset' %i]
            pf.datatype = msg['%s_datatype' %i]
            pf.count = msg['%s_count' %i]
            obj.fields.append(pf)
        obj.is_bigedian = msg['is_bigedian']
        obj.point_step = msg['point_step']
        obj.row_step = msg['row_step']
        obj.data = msg['data']
        obj.is_dense = msg['is_dense']
        return(obj)

    def point_field(cls, msg, obj):
        obj.name = msg['name']
        obj.offset = msg['offset']
        obj.datatype = msg['datatype']
        obj.count = msg['count']
        return(obj)

    def range(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.radiation_type = msg['radiation_type']
        obj.field_of_view = msg['field_of_view']
        obj.min_range = msg['min_range']
        obj.max_range = msg['max_range']
        obj.range = msg['range']
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


from rospy_msgpack import interpret

encode = interpret.Encode()
decode = interpret.Decode()


class Encode():
    def __init__(self):
        pass

    def aux_spi_data(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["sensors"] = obj.sensors
        msg.update(h)
        return(msg)

    def biotac(cls, obj):
        msg = {}
        bio = encode.biotacs(obj, "")
        msg.update(bio)
        return(msg)

    def biotac_all(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg.update(h)
        for i in range(5):
            bio = encode.biotacs(obj.tactiles[i], i)
            msg.update(bio)
        return(msg)

    # def control_type(cls, obj):
    #     msg = {}

    def ethercat_debug(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["sensors"] = obj.sensors
        msg["data"] = obj.motor_data_type.data
        msg["which_motors"] = obj.which_motors
        msg["which_motors_data_arrived"] = obj.which_motors_data_arrived
        msg["which_motors_data_had_errors"] = obj.which_motors_data_had_errors
        msg["motor_data_packet_torque"] = obj.motor_data_packet_torque
        msg["motor_data_packet_misc"] = obj.motor_data_packet_misc
        msg["tactile_data_type"] = obj.tactile_data_type
        msg["tactile_data_valid"] = obj.tactile_data_valid
        msg["tactile"] = obj.tactile
        msg["idle_time_us"] = obj.idle_time_us
        msg.update(h)
        return(msg)

    def from_motor_data_type(cls, obj):
        msg = {}
        msg["data"] = obj.data
        return(msg)

    def grasp_array(cls, obj):
        msg = {}
        # grasps
        msg["id"] = obj.grasps.id
        msg["grasp_quality"] = obj.grasps.grasp_quality
        msg["max_contact_force"] = obj.grasps.max_contact_force
        msg["allowed_touch_objects"] = obj.grasps.allowed_touch_objects
        # pre_grasp_posture
        preh = encode.header(obj.grasps.pre_grasp_posture.header, "pre")
        msg["prejoint_names"] = obj.grasps.pre_grasp_posture.joint_names
        pre_grasp = encode.grasp_points(obj.grasps.pre_grasp_posture.points, "pre")
        # grasp_posture
        postureh = encode.header(obj.grasps.grasp_posture.header, "posture")
        msg["joint_names"] = obj.grasps.grasp_posture.joint_names
        posture_grasp = encode.grasp_points(obj.grasps.grasp_posture.points, "posture")
        # grasp_pose
        poseh = encode.header(obj.grasps.grasp_pose.header, "pose")
        posep = encode.position(obj.grasps.grasp_pose.pose.position, "pose")
        poseo = encode.orientation(obj.grasps.grasp_pose.pose.orientation, "pose")
        # pre_grasp_approach
        apph = encode.header(obj.grasps.pre_grasp_approach.direction.header, "app")
        appv = encode.vector(obj.grasps.pre_grasp_approach.direction.vector, "app")
        msg["appdesired_distance"] = obj.grasps.pre_grasp_approach.desired_distance
        msg["appmin_distance"] = obj.grasps.pre_grasp_approach.min_distance
        # post_grasp_retreat
        reth = encode.header(obj.grasps.post_grasp_retreat.direction.header, "ret")
        retv = encode.vector(obj.grasps.post_grasp_retreat.direction.vector, "ret")
        msg["retdesired_distance"] = obj.grasps.post_grasp_retreat.desired_distance
        msg["retmin_distance"] = obj.grasps.post_grasp_retreat.min_distance
        # post_place_retreat
        plh = encode.header(obj.grasps.post_place_retreat.direction.header, "place")
        plv = encode.vector(obj.grasps.post_place_retreat.direction.vector, "place")
        msg["pldesired_distance"] = obj.grasps.post_place_retreat.desired_distance
        msg["plmin_distance"] = obj.grasps.post_place_retreat.min_distance
        # update
        msg.update(preh)
        msg.update(pre_grasp)
        msg.update(postureh)
        msg.update(posture_grasp)
        msg.update(poseh)
        msg.update(posep)
        msg.update(poseo)
        msg.update(apph)
        msg.update(appv)
        msg.update(reth)
        msg.update(retv)
        msg.update(plh)
        msg.update(plv)
        return(msg)

    def joint_controller_state(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["set_point"] = obj.set_point
        msg["process_value"] = obj.process_value
        msg["process_value_dot"] = obj.process_value_dot
        msg["commanded_velocity"] = obj.commanded_velocity
        msg["error"] = obj.error
        msg["time_step"] = obj.time_step
        msg["command"] = obj.command
        msg["measured_effort"] = obj.measured_effort
        msg["friction_compensation"] = obj.friction_compensation
        msg["position_p"] = obj.position_p
        msg["position_i"] = obj.position_i
        msg["position_d"] = obj.position_d
        msg["position_i_clamp"] = obj.position_i_clamp
        msg["velocity_p"] = obj.velocity_p
        msg["velocity_i"] = obj.velocity_i
        msg["velocity_d"] = obj.velocity_d
        msg["velocity_i_clamp"] = obj.velocity_i_clamp
        msg.update(h)
        return(msg)

    def joint_muscle_position_controller_state(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["set_point"] = obj.set_point
        msg["process_value"] = obj.process_value
        msg["process_value_dot"] = obj.process_value_dot
        msg["error"] = obj.error
        msg["time_step"] = obj.time_step
        msg["pseudo_command"] = obj.pseudo_command
        msg["valve_muscle_0"] = obj.valve_muscle_0
        msg["valve_muscle_1"] = obj.valve_muscle_1
        msg["packed_valve"] = obj.packed_valve
        msg["muscle_pressure_0"] = obj.muscle_pressure_0
        msg["muscle_pressure_1"] = obj.muscle_pressure_1
        msg["p"] = obj.p
        msg["i"] = obj.i
        msg["d"] = obj.d
        msg["i_clamp"] = obj.i_clamp
        msg.update(h)
        return(msg)

    def joint_muscle_valve_controller_command(cls, obj):
        msg = {}
        msg["cmd_valve_muscle"] = obj.cmd_valve_muscle
        msg["cmd_duration_ms"] = obj.cmd_duration_ms
        return(msg)

    def joint_muscle_valve_controller_state(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["set_valve_muscle_0"] = obj.set_valve_muscle_0
        msg["set_valve_muscle_1"] = obj.set_valve_muscle_1
        msg["set_duration_muscle_0"] = obj.set_duration_muscle_0
        msg["set_duration_muscle_1"] = obj.set_duration_muscle_1
        msg["current_valve_muscle_0"] = obj.current_valve_muscle_0
        msg["current_valve_muscle_1"] = obj.current_valve_muscle_1
        msg["current_duration_muscle_0"] = obj.current_duration_muscle_0
        msg["current_duration_muscle_1"] = obj.current_duration_muscle_1
        msg["packed_valve"] = obj.packed_valve
        msg["muscle_pressure_0"] = obj.muscle_pressure_0
        msg["muscle_pressure_1"] = obj.muscle_pressure_1
        msg["time_step"] = obj.time_step
        msg.update(h)
        return(msg)

    def mid_prox_data(cls, obj):
        msg = {}
        msg["middle"] = obj.middle
        msg["proximal"] = obj.proximal
        return(msg)

    def mid_prox_data_all(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        for i in range(5):
            msg["%s_middle" %i] = obj.sensors[i].middle
            msg["%s_proximal" %i] = obj.sensors[i].proximal
        msg.update(h)
        return(msg)

    def motor_system_controls(cls, obj):
        msg = {}
        msg["motor_id"] = obj.motor_id
        msg["enable_backlash_compensation"] = obj.enable_backlash_compensation
        msg["increase_sgl_tracking"] = obj.increase_sgl_tracking
        msg["decrease_sgl_tracking"] = obj.decrease_sgl_tracking
        msg["increase_sgr_tracking"] = obj.increase_sgr_tracking
        msg["decrease_sgr_tracking"] = obj.decrease_sgr_tracking
        msg["initiate_jiggling"] = obj.initiate_jiggling
        msg["write_config_to_eeprom"] = obj.write_config_to_eeprom
        return(msg)

    def shadow_contact_state_stamped(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        f = encode.force(obj.tangential_force, "tan")
        cp = encode.position(obj.contact_position, "cont")
        cn = encode.xyz(obj.contact_normal, "cont", "norm")
        msg["Fnormal"] = obj.Fnormal
        msg["Ltorque"] = obj.Ltorque
        msg.update(h)
        msg.update(f)
        msg.update(cp)
        msg.update(cn)
        return(msg)

    def shadow_pst(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["pressure"] = obj.pressure
        msg["temperature"] = obj.temperature
        msg.update(h)
        return(msg)

    def tactile(cls, obj):
        msg = {}
        msg["data"] = obj.data.data
        return(msg)

    def tactile_array(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        msg["data"] = obj.data.data.data
        msg.update(h)
        return(msg)

    def ubi0(cls, obj):
        msg = {}
        msg["distal"] = obj.distal
        return(msg)

    def ubi0_all(cls, obj):
        msg = {}
        h = encode.header(obj.header, "")
        for i in range(5):
            msg["%s_distal" %i] = obj.tactiles[i].distal
        msg.update(h)
        return(msg)

    def cartesian_data(cls, obj):
        msg = {}
        msg["cartesian_positions_length"] = obj.cartesian_positions_length
        for i in range(msg['cartesian_positions_length']):
            t = encode.tip(obj.cartesian_positions[i], i)
            msg.update(t)
        return(msg)

    def cartesian_position(cls, obj):
        msg = {}
        t = encode.tip(obj, "")
        return(msg)

    def command(cls, obj):
        msg = {}
        msg["command_type"] = obj.command_type
        msg["sendupdate_length"] = obj.sendupdate_command.sendupdate_length
        for i in range(msg['sendupdate_length']):
            j = encode.joint(obj.sendupdate_command.sendupdate_list[i], i)
            msg.update(j)
        msg["contrlr_name"] = obj.contrlr_command.contrlr_name
        msg["list_of_parameters"] = obj.contrlr_command.list_of_parameters
        msg["length_of_list"] = obj.contrlr_command.length_of_list
        return(msg)

    def config(cls, obj):
        msg = {}
        msg["node_name"] = obj.node_name
        msg["list_of_parameters"] = obj.list_of_parameters
        msg["length_of_list"] = obj.length_of_list
        return(msg)

    def contrlr(cls, obj):
        msg = {}
        msg["contrlr_name"] = obj.contrlr_name
        msg["list_of_parameters"] = obj.list_of_parameters
        msg["length_of_list"] = obj.length_of_list
        return(msg)

    def joint(cls, obj):
        msg = {}
        j = encode.joint(obj, "")
        msg.update(j)
        return(msg)

    def joints_data(cls, obj):
        msg = {}
        msg["joints_list_length"] = obj.joints_list_length
        for i in range(msg['joints_list_length']):
            j = encode.joint(obj.joints_list[i], i)
            msg.update(j)
        return(msg)

    def reverse_kinematics(cls, obj):
        msg = {}
        msg["finger_name"] = obj.finger_name
        return(msg)

    def send_update(cls, obj):
        msg = {}
        msg["sendupdate_length"] = obj.sendupdate_length
        for i in range(msg['sendupdate_length']):
            j = encode.joint(obj.sendupdate_list[i], i)
            msg.update(j)
        return(msg)

# ======================================================================================

class Decode():
    def __init__(self):
        pass

    def aux_spi_data(cls, msg,obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.sensors = msg["sensors"]
        return(obj)

    def biotac(cls, msg, obj):
        obj = decode.biotacs(msg, obj, "")
        return(obj)

    def biotac_all(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(5):
            obj.tactiles[i] = decode.biotacs(msg, obj.tactiles[i], i)
        return(obj)

    def ethercat_debug(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.sensors = msg["sensors"]
        obj.motor_data_type.data = msg["data"]
        obj.which_motors = msg["which_motors"]
        obj.which_motors_data_arrived = msg["which_motors_data_arrived"]
        obj.which_motors_data_had_errors = msg["which_motors_data_had_errors"]
        obj.motor_data_packet_torque = msg["motor_data_packet_torque"]
        obj.motor_data_packet_misc = msg["motor_data_packet_misc"]
        obj.tactile_data_type = msg["tactile_data_type"]
        obj.tactile_data_valid = msg["tactile_data_valid"]
        obj.tactile = msg["tactile"]
        obj.idle_time_us = msg["idle_time_us"]
        return(obj)

    def from_motor_data_type(cls, msg, obj):
        obj.data = msg["data"]
        return(obj)

    def grasp_array(cls, msg, obj):
        # grasps
        obj.grasps.id = msg["id"]
        obj.grasps.grasp_quality = msg["grasp_quality"]
        obj.grasps.max_contact_force = msg["max_contact_force"]
        obj.grasps.allowed_touch_objects = msg["allowed_touch_objects"]
        # pre_grasp_posture
        obj.grasps.pre_grasp_posture.header = decode.header(msg, obj.grasps.pre_grasp_posture.header, "pre")
        obj.grasps.pre_grasp_posture.joint_names = msg["prejoint_names"]
        obj.grasps.pre_grasp_posture.points = decode.grasp_points(msg, obj.grasps.pre_grasp_posture.points, "pre")
        # grasp_posture
        obj.grasps.grasp_posture.header = decode.header(msg, obj.grasps.grasp_posture.header, "posture")
        obj.grasps.grasp_posture.joint_names = msg["joint_names"]
        obj.grasps.grasp_posture.points = decode.grasp_points(msg, obj.grasps.grasp_posture.points, "posture")
        # grasp_pose
        obj.grasps.grasp_pose.header = decode.header(msg, obj.grasps.grasp_pose.header, "pose")
        obj.grasps.grasp_pose.pose.position = decode.position(msg, obj.grasps.grasp_pose.pose.position, "pose")
        obj.grasps.grasp_pose.pose.orientation = decode.orientation(msg, obj.grasps.grasp_pose.pose.orientation, "pose")
        # pre_grasp_approach
        obj.grasps.pre_grasp_approach.direction.header = decode.header(msg, obj.grasps.pre_grasp_approach.direction.header, "app")
        obj.grasps.pre_grasp_approach.direction.vector = decode.vector(msg, obj.grasps.pre_grasp_approach.direction.vector, "app")
        obj.grasps.pre_grasp_approach.desired_distance = msg["appdesired_distance"]
        obj.grasps.pre_grasp_approach.min_distance = msg["appmin_distance"]
        # post_grasp_retreat
        obj.grasps.post_grasp_retreat.direction.header = decode.header(msg, obj.grasps.post_grasp_retreat.direction.header, "ret")
        obj.grasps.post_grasp_retreat.direction.vector = decode.vector(msg, obj.grasps.post_grasp_retreat.direction.vector, "ret")
        obj.grasps.post_grasp_retreat.desired_distance = msg["retdesired_distance"]
        obj.grasps.post_grasp_retreat.min_distance = msg["retmin_distance"]
        # post_place_retreat
        obj.grasps.post_place_retreat.direction.header = decode.header(msg, obj.grasps.post_place_retreat.direction.header, "place")
        obj.grasps.post_place_retreat.direction.vector = decode.vector(msg, obj.grasps.post_place_retreat.direction.vector, "place")
        obj.grasps.post_place_retreat.desired_distance = msg["pldesired_distance"]
        obj.grasps.post_place_retreat.min_distance = msg["plmin_distance"]
        # return
        return(obj)

    def joint_controller_state(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.set_point = msg["set_point"]
        obj.process_value = msg["process_value"]
        obj.process_value_dot = msg["process_value_dot"]
        obj.commanded_velocity = msg["commanded_velocity"]
        obj.error = msg["error"]
        obj.time_step = msg["time_step"]
        obj.command = msg["command"]
        obj.measured_effort = msg["measured_effort"]
        obj.friction_compensation = msg["friction_compensation"]
        obj.position_p = msg["position_p"]
        obj.position_i = msg["position_i"]
        obj.position_d = msg["position_d"]
        obj.position_i_clamp = msg["position_i_clamp"]
        obj.velocity_p = msg["velocity_p"]
        obj.velocity_i = msg["velocity_i"]
        obj.velocity_d = msg["velocity_d"]
        obj.velocity_i_clamp = msg["velocity_i_clamp"]
        return(obj)

    def joint_muscle_position_controller_state(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.set_point = msg["set_point"]
        obj.process_value = msg["process_value"]
        obj.process_value_dot = msg["process_value_dot"]
        obj.error = msg["error"]
        obj.time_step = msg["time_step"]
        obj.pseudo_command = msg["pseudo_command"]
        obj.valve_muscle_0 = msg["valve_muscle_0"]
        obj.valve_muscle_1 = msg["valve_muscle_1"]
        obj.packed_valve = msg["packed_valve"]
        obj.muscle_pressure_0 = msg["muscle_pressure_0"]
        obj.muscle_pressure_1 = msg["muscle_pressure_1"]
        obj.p = msg["p"]
        obj.i = msg["i"]
        obj.d = msg["d"]
        obj.i_clamp = msg["i_clamp"]
        return(obj)

    def joint_muscle_valve_controller_command(cls, msg, obj):
        obj.cmd_valve_muscle = msg["cmd_valve_muscle"]
        obj.cmd_duration_ms = msg["cmd_duration_ms"]
        return(obj)

    def joint_muscle_valve_controller_state(cls, msg, obj):
        obj = header.Header().decode(msg,obj)
        obj.set_valve_muscle_0 = msg["set_valve_muscle_0"]
        obj.set_valve_muscle_1 = msg["set_valve_muscle_1"]
        obj.set_duration_muscle_0 = msg["set_duration_muscle_0"]
        obj.set_duration_muscle_1 = msg["set_duration_muscle_1"]
        obj.current_valve_muscle_0 = msg["current_valve_muscle_0"]
        obj.current_valve_muscle_1 = msg["current_valve_muscle_1"]
        obj.current_duration_muscle_0 = msg["current_duration_muscle_0"]
        obj.current_duration_muscle_1 = msg["current_duration_muscle_1"]
        obj.packed_valve = msg["packed_valve"]
        obj.muscle_pressure_0 = msg["muscle_pressure_0"]
        obj.muscle_pressure_1 = msg["muscle_pressure_1"]
        obj.time_step = msg["time_step"]
        return(obj)

    def mid_prox_data(cls, msg, obj):
        obj.middle = msg["middle"]
        obj.proximal = msg["proximal"]
        return(obj)

    def mid_prox_data_all(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(5):
            obj.sensors[i].middle = msg["%s_middle" %i]
            obj.sensors[i].proximal = msg["%s_proximal" %i]
        return(obj)

    def motor_system_controls(cls, msg, obj):
        obj.motor_id = msg["motor_id"]
        obj.enable_backlash_compensation = msg["enable_backlash_compensation"]
        obj.increase_sgl_tracking = msg["increase_sgl_tracking"]
        obj.decrease_sgl_tracking = msg["decrease_sgl_tracking"]
        obj.increase_sgr_tracking = msg["increase_sgr_tracking"]
        obj.decrease_sgr_tracking = msg["decrease_sgr_tracking"]
        obj.initiate_jiggling = msg["initiate_jiggling"]
        obj.write_config_to_eeprom = msg["write_config_to_eeprom"]
        return(obj)

    def shadow_contact_state_stamped(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.tangential_force = decode.force(msg, obj.tangential_force, "tan")
        obj.contact_position = decode.position(msg, obj.contact_position, "cont")
        obj.contact_normal = decode.xyz(msg, obj.contact_normal, "cont", "norm")
        obj.Fnormal = msg["Fnormal"]
        obj.Ltorque = msg["Ltorque"]
        return(obj)

    def shadow_pst(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.pressure = msg["pressure"]
        obj.temperature = msg["temperature"]
        return(obj)

    def tactile(cls, msg, obj):
        obj.data.data = msg["data"]
        return(obj)

    def tactile_array(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        obj.data.data.data = msg["data"]
        return(obj)

    def ubi0(cls, msg, obj):
        obj.distal = msg["distal"]
        return(obj)

    def ubi0_all(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "")
        for i in range(5):
            obj.tactiles[i].distal = msg["%s_distal" %i]
        return(obj)

    def cartesian_data(cls, msg, obj):
        obj.cartesian_positions_length = msg["cartesian_positions_length"]
        for i in range(5):
            obj.cartesian_positions[i] = decode.tip(msg, obj.cartesian_positions[i], i)
        return(obj)


    def cartesian_position(cls, msg, obj):
        obj = decode.tip(msg, obj, "")
        return(obj)

    def command(cls, msg, obj):
        obj.command_type = msg["command_type"]
        obj.sendupdate_command.sendupdate_length = msg["sendupdate_length"]
        for i in range(msg['sendupdate_length']):
            obj.sendupdate_command.sendupdate_list[i] = decode.joint(msg, obj.sendupdate_command.sendupdate_list[i], i)
        obj.contrlr_command.contrlr_name = msg["contrlr_name"]
        obj.contrlr_command.list_of_parameters = msg["list_of_parameters"]
        obj.contrlr_command.length_of_list = msg["length_of_list"]
        return(obj)

    def config(cls, msg, obj):
        obj.node_name = msg["node_name"]
        obj.list_of_parameters = msg["list_of_parameters"]
        obj.length_of_list = msg["length_of_list"]
        return(obj)

    def contrlr(cls, msg, obj):
        obj.contrlr_name = msg["contrlr_name"]
        obj.list_of_parameters = msg["list_of_parameters"]
        obj.length_of_list = msg["length_of_list"]
        return(obj)

    def joint(cls, msg, obj):
        obj = decode.joint(msg, obj, "")
        return(obj)

    def joints_data(cls, msg, obj):
        obj.joints_list_length = msg["joints_list_length"]
        for i in range(msg['joints_list_length']):
            obj.joints_list[i] = decode.joint(obj.joints_list[i], i)
        return(obj)

    def reverse_kinematics(cls, msg, obj):
        obj.finger_name = msg["finger_name"]
        return(obj)

    def send_update(cls, msg, obj):
        obj.sendupdate_length = msg["sendupdate_length"]
        for i in range(msg['sendupdate_length']):
            obj.sendupdate_list[i] = decode.joint(msg, obj.sendupdate_list[i], i)
        return(obj)

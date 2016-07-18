
from rospy_msgpack import header


class Encode():
    def __init__(self):
        pass

    def aux_spi_data(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["sensors"] = obj.sensors
        msg.update(h)
        return(msg)

    def biotac(cls, obj):
        msg = {}
        msg["pac0"] = obj.pac0
        msg["pac1"] = obj.pac1
        msg["pdc"] = obj.pdc
        msg["tac"] = obj.tac
        msg["tdc"] = obj.tdc
        msg["electrodes"] = obj.electrodes
        return(msg)

    def biotac_all(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["pac0"] = obj.tactiles.pac0
        msg["pac1"] = obj.tactiles.pac1
        msg["pdc"] = obj.tactiles.pdc
        msg["tac"] = obj.tactiles.tac
        msg["tdc"] = obj.tactiles.tdc
        msg["electrodes"] = obj.tactiles.electrodes
        msg.update(h)
        return(msg)

    # def control_type(cls, obj):
    #     msg = {}

    def ethercat_debug(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
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
        msg["preseq"] = obj.grasps.pre_grasp_posture.header.seq
        msg["presecs"] = obj.grasps.pre_grasp_posture.header.stamp.secs
        msg["prensecs"] = obj.grasps.pre_grasp_posture.header.stamp.nsecs
        msg["preframe_id"] = obj.grasps.pre_grasp_posture.header.frame_id
        msg["prejoint_names"] = obj.grasps.pre_grasp_posture.joint_names
        msg["prepositions"] = obj.grasps.pre_grasp_posture.points.positions
        msg["prevelocities"] = obj.grasps.pre_grasp_posture.points.velocities
        msg["preaccelerations"] = obj.grasps.pre_grasp_posture.points.accelerations
        msg["preeffort"] = obj.grasps.pre_grasp_posture.points.effort
        msg["pretime_from_start"] = obj.grasps.pre_grasp_posture.points.time_from_start
        # grasp_posture
        msg["seq"] = obj.grasps.grasp_posture.header.seq
        msg["secs"] = obj.grasps.grasp_posture.header.stamp.secs
        msg["nsecs"] = obj.grasps.grasp_posture.header.stamp.nsecs
        msg["frame_id"] = obj.grasps.grasp_posture.header.frame_id
        msg["joint_names"] = obj.grasps.grasp_posture.joint_names
        msg["positions"] = obj.grasps.grasp_posture.points.positions
        msg["velocities"] = obj.grasps.grasp_posture.points.velocities
        msg["accelerations"] = obj.grasps.grasp_posture.points.accelerations
        msg["effort"] = obj.grasps.grasp_posture.points.effort
        msg["time_from_start"] = obj.grasps.grasp_posture.points.time_from_start
        # grasp_pose
        msg["poseseq"] = obj.grasps.grasp_pose.header.seq
        msg["posesecs"] = obj.grasps.grasp_pose.header.stamp.secs
        msg["posensecs"] = obj.grasps.grasp_pose.header.stamp.nsecs
        msg["poseframe_id"] = obj.grasps.grasp_pose.header.frame_id
        msg["px"] = obj.grasps.grasp_pose.pose.position.x
        msg["py"] = obj.grasps.grasp_pose.pose.position.y
        msg["pz"] = obj.grasps.grasp_pose.pose.position.z
        msg["ox"] = obj.grasps.grasp_pose.pose.orientation.x
        msg["oy"] = obj.grasps.grasp_pose.pose.orientation.y
        msg["oz"] = obj.grasps.grasp_pose.pose.orientation.z
        msg["ow"] = obj.grasps.grasp_pose.pose.orientation.w
        # pre_grasp_approach
        msg["appseq"] = obj.grasps.pre_grasp_approach.direction.header.seq
        msg["appsecs"] = obj.grasps.pre_grasp_approach.direction.header.stamp.secs
        msg["appnsecs"] = obj.grasps.pre_grasp_approach.direction.header.stamp.nsecs
        msg["appframe_id"] = obj.grasps.pre_grasp_approach.direction.header.frame_id
        msg["appx"] = obj.grasps.pre_grasp_approach.direction.vector.x
        msg["appy"] = obj.grasps.pre_grasp_approach.direction.vector.y
        msg["appz"] = obj.grasps.pre_grasp_approach.direction.vector.z
        msg["appdesired_distance"] = obj.grasps.pre_grasp_approach.desired_distance
        msg["appmin_distance"] = obj.grasps.pre_grasp_approach.min_distance
        # post_grasp_retreat
        msg["retseq"] = obj.grasps.post_grasp_retreat.direction.header.seq
        msg["retsecs"] = obj.grasps.post_grasp_retreat.direction.header.stamp.secs
        msg["retnsecs"] = obj.grasps.post_grasp_retreat.direction.header.stamp.nsecs
        msg["retframe_id"] = obj.grasps.post_grasp_retreat.direction.header.frame_id
        msg["retx"] = obj.grasps.post_grasp_retreat.direction.vector.x
        msg["rety"] = obj.grasps.post_grasp_retreat.direction.vector.y
        msg["retz"] = obj.grasps.post_grasp_retreat.direction.vector.z
        msg["retdesired_distance"] = obj.grasps.post_grasp_retreat.desired_distance
        msg["retmin_distance"] = obj.grasps.post_grasp_retreat.min_distance
        # post_place_retreat
        msg["plseq"] = obj.grasps.post_place_retreat.direction.header.seq
        msg["plsecs"] = obj.grasps.post_place_retreat.direction.header.stamp.secs
        msg["plnsecs"] = obj.grasps.post_place_retreat.direction.header.stamp.nsecs
        msg["plframe_id"] = obj.grasps.post_place_retreat.direction.header.frame_id
        msg["plx"] = obj.grasps.post_place_retreat.direction.vector.x
        msg["ply"] = obj.grasps.post_place_retreat.direction.vector.y
        msg["plz"] = obj.grasps.post_place_retreat.direction.vector.z
        msg["pldesired_distance"] = obj.grasps.post_place_retreat.desired_distance
        msg["plmin_distance"] = obj.grasps.post_place_retreat.min_distance
        # return
        return(msg)

    def joint_controller_state(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
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
        h = header.Header().endcode(obj)
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
        h = header.Header().endcode(obj)
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
        h = header.Header().endcode(obj)
        msg["middle"] = obj.sensors.middle
        msg["proximal"] = obj.sensors.proximal
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
        h = header.Header().endcode(obj)
        msg["tanx"] = obj.tangential_force.x
        msg["tany"] = obj.tangential_force.y
        msg["tanz"] = obj.tangential_force.z
        msg["posx"] = obj.contact_position.x
        msg["posy"] = obj.contact_position.y
        msg["posz"] = obj.contact_position.z
        msg["normx"] = obj.contact_normal.x
        msg["normy"] = obj.contact_normal.y
        msg["normz"] = obj.contact_normal.z
        msg["Fnormal"] = obj.Fnormal
        msg["Ltorque"] = obj.Ltorque
        msg.update(h)
        return(msg)

    def shadow_pst(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
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
        h = header.Header().endcode(obj)
        msg["data"] = obj.data.data.data
        msg.update(h)
        return(msg)

    def ubi0(cls, obj):
        msg = {}
        msg["distal"] = obj.distal
        return(msg)

    def ubi0_all(cls, obj):
        msg = {}
        h = header.Header().endcode(obj)
        msg["distal"] = obj.tactiles.distal
        msg.update(h)
        return(msg)

    def cartesian_data(cls, obj):
        msg = {}
        msg["cartesian_positions_length"] = obj.cartesian_positions_length
        msg["tip_name"] = obj.cartesian_positions.tip_name
        msg["tip_pos_x"] = obj.cartesian_positions.tip_pos_x
        msg["tip_pos_y"] = obj.cartesian_positions.tip_pos_y
        msg["tip_pos_z"] = obj.cartesian_positions.tip_pos_z
        msg["tip_orientation_rho"] = obj.cartesian_positions.tip_orientation_rho
        msg["tip_orientation_theta"] = obj.cartesian_positions.tip_orientation_theta
        msg["tip_orientation_sigma"] = obj.cartesian_positions.tip_orientation_sigma
        return(msg)

    def cartesian_position(cls, obj):
        msg = {}
        msg["tip_name"] = obj.tip_name
        msg["tip_pos_x"] = obj.tip_pos_x
        msg["tip_pos_y"] = obj.tip_pos_y
        msg["tip_pos_z"] = obj.tip_pos_z
        msg["tip_orientation_rho"] = obj.tip_orientation_rho
        msg["tip_orientation_theta"] = obj.tip_orientation_theta
        msg["tip_orientation_sigma"] = obj.tip_orientation_sigma
        return(msg)

    def command(cls, obj):
        msg = {}
        msg["command_type"] = obj.command_type
        msg["sendupdate_length"] = obj.sendupdate_command.sendupdate_length
        msg["joint_name"] = obj.sendupdate_command.sendupdate_list.joint_name
        msg["joint_position"] = obj.sendupdate_command.sendupdate_list.joint_position
        msg["joint_target"] = obj.sendupdate_command.sendupdate_list.joint_target
        msg["joint_torque"] = obj.sendupdate_command.sendupdate_list.joint_torque
        msg["joint_temperature"] = obj.sendupdate_command.sendupdate_list.joint_temperature
        msg["joint_current"] = obj.sendupdate_command.sendupdate_list.joint_current
        msg["error_flag"] = obj.sendupdate_command.sendupdate_list.error_flag
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
        msg["joint_name"] = obj.joint_name
        msg["joint_position"] = obj.joint_position
        msg["joint_target"] = obj.joint_target
        msg["joint_torque"] = obj.joint_torque
        msg["joint_temperature"] = obj.joint_temperature
        msg["joint_current"] = obj.joint_current
        msg["error_flag"] = obj.error_flag
        return(msg)

    def joints_data(cls, obj):
        msg = {}
        msg["joints_list_length"] = obj.joints_list_length
        msg["joint_name"] = obj.joints_list.joint_name
        msg["joint_position"] = obj.joints_list.joint_position
        msg["joint_target"] = obj.joints_list.joint_target
        msg["joint_torque"] = obj.joints_list.joint_torque
        msg["joint_temperature"] = obj.joints_list.joint_temperature
        msg["joint_current"] = obj.joints_list.joint_current
        msg["error_flag"] = obj.joints_list.error_flag
        return(msg)

    def reverse_kinematics(cls, obj):
        msg = {}
        msg["finger_name"] = obj.finger_name
        return(msg)

    def send_update(cls, obj):
        msg = {}
        msg["joints_list_length"] = obj.joints_list_length
        msg["joint_name"] = obj.sendupdate_list.joint_name
        msg["joint_position"] = obj.sendupdate_list.joint_position
        msg["joint_target"] = obj.sendupdate_list.joint_target
        msg["joint_torque"] = obj.sendupdate_list.joint_torque
        msg["joint_temperature"] = obj.sendupdate_list.joint_temperature
        msg["joint_current"] = obj.sendupdate_list.joint_current
        msg["error_flag"] = obj.sendupdate_list.error_flag
        return(msg)

# ===========================================================================================

class Decode():
    def __init__(self):
        pass

    def aux_spi_data(cls, msg,obj):
        obj = header.Header().decode(msg, obj)
        obj.sensors = msg["sensors"]
        return(obj)

    def biotac(cls, msg, obj):
        obj.pac0 = msg["pac0"]
        obj.pac1 = msg["pac1"]
        obj.pdc = msg["pdc"]
        obj.tac = msg["tac"]
        obj.tdc = msg["tdc"]
        obj.electrodes = msg["electrodes"]
        return(obj)

    def biotac_all(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.tactiles.pac0 = msg["pac0"]
        obj.tactiles.pac1 = msg["pac1"]
        obj.tactiles.pdc = msg["pdc"]
        obj.tactiles.tac = msg["tac"]
        obj.tactiles.tdc = msg["tdc"]
        obj.tactiles.electrodes = msg["electrodes"]
        return(obj)

    def ethercat_debug(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
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
        obj.grasps.pre_grasp_posture.header.seq = msg["preseq"]
        obj.grasps.pre_grasp_posture.header.stamp.secs = msg["presecs"]
        obj.grasps.pre_grasp_posture.header.stamp.nsecs = msg["prensecs"]
        obj.grasps.pre_grasp_posture.header.frame_id = msg["preframe_id"]
        obj.grasps.pre_grasp_posture.joint_names = msg["prejoint_names"]
        obj.grasps.pre_grasp_posture.points.positions = msg["prepositions"]
        obj.grasps.pre_grasp_posture.points.velocities = msg["prevelocities"]
        obj.grasps.pre_grasp_posture.points.accelerations = msg["preaccelerations"]
        obj.grasps.pre_grasp_posture.points.effort = msg["preeffort"]
        obj.grasps.pre_grasp_posture.points.time_from_start = msg["pretime_from_start"]
        # grasp_posture
        obj.grasps.grasp_posture.header.seq = msg["seq"]
        obj.grasps.grasp_posture.header.stamp.secs = msg["secs"]
        obj.grasps.grasp_posture.header.stamp.nsecs = msg["nsecs"]
        obj.grasps.grasp_posture.header.frame_id = msg["frame_id"]
        obj.grasps.grasp_posture.joint_names = msg["joint_names"]
        obj.grasps.grasp_posture.points.positions = msg["positions"]
        obj.grasps.grasp_posture.points.velocities = msg["velocities"]
        obj.grasps.grasp_posture.points.accelerations = msg["accelerations"]
        obj.grasps.grasp_posture.points.effort = msg["effort"]
        obj.grasps.grasp_posture.points.time_from_start = msg["time_from_start"]
        # grasp_pose
        obj.grasps.grasp_pose.header.seq = msg["poseseq"]
        obj.grasps.grasp_pose.header.stamp.secs = msg["posesecs"]
        obj.grasps.grasp_pose.header.stamp.nsecs = msg["posensecs"]
        obj.grasps.grasp_pose.header.frame_id = msg["poseframe_id"]
        obj.grasps.grasp_pose.pose.position.x = msg["px"]
        obj.grasps.grasp_pose.pose.position.y = msg["py"]
        obj.grasps.grasp_pose.pose.position.z = msg["pz"]
        obj.grasps.grasp_pose.pose.orientation.x = msg["ox"]
        obj.grasps.grasp_pose.pose.orientation.y = msg["oy"]
        obj.grasps.grasp_pose.pose.orientation.z = msg["oz"]
        obj.grasps.grasp_pose.pose.orientation.w = msg["ow"]
        # pre_grasp_approach
        obj.grasps.pre_grasp_approach.direction.header.seq = msg["appseq"]
        obj.grasps.pre_grasp_approach.direction.header.stamp.secs = msg["appsecs"]
        obj.grasps.pre_grasp_approach.direction.header.stamp.nsecs = msg["appnsecs"]
        obj.grasps.pre_grasp_approach.direction.header.frame_id = msg["appframe_id"]
        obj.grasps.pre_grasp_approach.direction.vector.x = msg["appx"]
        obj.grasps.pre_grasp_approach.direction.vector.y = msg["appy"]
        obj.grasps.pre_grasp_approach.direction.vector.z = msg["appz"]
        obj.grasps.pre_grasp_approach.desired_distance = msg["appdesired_distance"]
        obj.grasps.pre_grasp_approach.min_distance = msg["appmin_distance"]
        # post_grasp_retreat
        obj.grasps.post_grasp_retreat.direction.header.seq = msg["retseq"]
        obj.grasps.post_grasp_retreat.direction.header.stamp.secs = msg["retsecs"]
        obj.grasps.post_grasp_retreat.direction.header.stamp.nsecs = msg["retnsecs"]
        obj.grasps.post_grasp_retreat.direction.header.frame_id = msg["retframe_id"]
        obj.grasps.post_grasp_retreat.direction.vector.x = msg["retx"]
        obj.grasps.post_grasp_retreat.direction.vector.y = msg["rety"]
        obj.grasps.post_grasp_retreat.direction.vector.z = msg["retz"]
        obj.grasps.post_grasp_retreat.desired_distance = msg["retdesired_distance"]
        obj.grasps.post_grasp_retreat.min_distance = msg["retmin_distance"]
        # post_place_retreat
        obj.grasps.post_place_retreat.direction.header.seq = msg["plseq"]
        obj.grasps.post_place_retreat.direction.header.stamp.secs = msg["plsecs"]
        obj.grasps.post_place_retreat.direction.header.stamp.nsecs = msg["plnsecs"]
        obj.grasps.post_place_retreat.direction.header.frame_id = msg["plframe_id"]
        obj.grasps.post_place_retreat.direction.vector.x = msg["plx"]
        obj.grasps.post_place_retreat.direction.vector.y = msg["ply"]
        obj.grasps.post_place_retreat.direction.vector.z = msg["plz"]
        obj.grasps.post_place_retreat.desired_distance = msg["pldesired_distance"]
        obj.grasps.post_place_retreat.min_distance = msg["plmin_distance"]
        # return
        return(obj)

    def joint_controller_state(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
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
        obj = header.Header().decode(msg, obj)
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
        obj = header.Header().decode(msg, obj)
        obj.sensors.middle = msg["middle"]
        obj.sensors.proximal = msg["proximal"]
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
        obj = header.Header().decode(msg, obj)
        obj.tangential_force.x = msg["tanx"]
        obj.tangential_force.y = msg["tany"]
        obj.tangential_force.z = msg["tanz"]
        obj.contact_position.x = msg["posx"]
        obj.contact_position.y = msg["posy"]
        obj.contact_position.z = msg["posz"]
        obj.contact_normal.x = msg["normx"]
        obj.contact_normal.y = msg["normy"]
        obj.contact_normal.z = msg["normz"]
        obj.Fnormal = msg["Fnormal"]
        obj.Ltorque = msg["Ltorque"]
        return(obj)

    def shadow_pst(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.pressure = msg["pressure"]
        obj.temperature = msg["temperature"]
        return(obj)

    def tactile(cls, msg, obj):
        obj.data.data = msg["data"]
        return(obj)

    def tactile_array(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.data.data.data = msg["data"]
        return(obj)

    def ubi0(cls, msg, obj):
        obj.distal = msg["distal"]
        return(obj)

    def ubi0_all(cls, msg, obj):
        obj = header.Header().decode(msg, obj)
        obj.tactiles.distal = msg["distal"]
        return(obj)

    def cartesian_data(cls, msg, obj):
        obj.cartesian_positions_length = msg["cartesian_positions_length"]
        obj.cartesian_positions.tip_name = msg["tip_name"]
        obj.cartesian_positions.tip_pos_x = msg["tip_pos_x"]
        obj.cartesian_positions.tip_pos_y = msg["tip_pos_y"]
        obj.cartesian_positions.tip_pos_z = msg["tip_pos_z"]
        obj.cartesian_positions.tip_orientation_rho = msg["tip_orientation_rho"]
        obj.cartesian_positions.tip_orientation_theta = msg["tip_orientation_theta"]
        obj.cartesian_positions.tip_orientation_sigma = msg["tip_orientation_sigma"]
        return(obj)


    def cartesian_position(cls, msg, obj):
        obj.tip_name = msg["tip_name"]
        obj.tip_pos_x = msg["tip_pos_x"]
        obj.tip_pos_y = msg["tip_pos_y"]
        obj.tip_pos_z = msg["tip_pos_z"]
        obj.tip_orientation_rho = msg["tip_orientation_rho"]
        obj.tip_orientation_theta = msg["tip_orientation_theta"]
        obj.tip_orientation_sigma = msg["tip_orientation_sigma"]
        return(obj)

    def command(cls, msg, obj):
        obj.command_type = msg["command_type"]
        obj.sendupdate_command.sendupdate_length = msg["sendupdate_length"]
        obj.sendupdate_command.sendupdate_list.joint_name = msg["joint_name"]
        obj.sendupdate_command.sendupdate_list.joint_position = msg["joint_position"]
        obj.sendupdate_command.sendupdate_list.joint_target = msg["joint_target"]
        obj.sendupdate_command.sendupdate_list.joint_torque = msg["joint_torque"]
        obj.sendupdate_command.sendupdate_list.joint_temperature = msg["joint_temperature"]
        obj.sendupdate_command.sendupdate_list.joint_current = msg["joint_current"]
        obj.sendupdate_command.sendupdate_list.error_flag = msg["error_flag"]
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
        obj.joint_name = msg["joint_name"]
        obj.joint_position = msg["joint_position"]
        obj.joint_target = msg["joint_target"]
        obj.joint_torque = msg["joint_torque"]
        obj.joint_temperature = msg["joint_temperature"]
        obj.joint_current = msg["joint_current"]
        obj.error_flag = msg["error_flag"]
        return(obj)

    def joints_data(cls, msg, obj):
        obj.joints_list_length = msg["joints_list_length"]
        obj.joints_list.joint_name = msg["joint_name"]
        obj.joints_list.joint_position = msg["joint_position"]
        obj.joints_list.joint_target = msg["joint_target"]
        obj.joints_list.joint_torque = msg["joint_torque"]
        obj.joints_list.joint_temperature = msg["joint_temperature"]
        obj.joints_list.joint_current = msg["joint_current"]
        obj.joints_list.error_flag = msg["error_flag"]
        return(obj)

    def reverse_kinematics(cls, msg, obj):
        obj.finger_name = msg["finger_name"]
        return(obj)

    def send_update(cls, msg, obj):
        obj.joints_list_length = msg["joints_list_length"]
        obj.sendupdate_list.joint_name = msg["joint_name"]
        obj.sendupdate_list.joint_position = msg["joint_position"]
        obj.sendupdate_list.joint_target = msg["joint_target"]
        obj.sendupdate_list.joint_torque = msg["joint_torque"]
        obj.sendupdate_list.joint_temperature = msg["joint_temperature"]
        obj.sendupdate_list.joint_current = msg["joint_current"]
        obj.sendupdate_list.error_flag = msg["error_flag"]
        return(obj)

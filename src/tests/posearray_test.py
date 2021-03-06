#!/usr/bin/env python

"""
Test script to check the rospy_msgpack package. Creates a geometry_msgs
 PoseArray and publishes it so another topic can subscribe to the topic.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"

import time

import rospy

from geometry_msgs.msg import (Polygon, Point32, Pose, Point, Quaternion,
                               PoseArray)


posearray = PoseArray()
position1 = Point(1, 2, 3)
orientation1 = Quaternion(4, 5, 6, 7)
pose1 = Pose(position1, orientation1)
posearray.poses.append(pose1)

position2 = Point(10, 20, 30)
orientation2 = Quaternion(40, 50, 60, 70)
pose2 = Pose(position2, orientation2)
posearray.poses.append(pose2)


def talker():
    rospy.init_node("tester", anonymous=True)
    pub_handle = rospy.Publisher("test_posearray", PoseArray, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub_handle.publish(posearray)
        print("publishing...")


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

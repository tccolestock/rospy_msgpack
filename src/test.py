#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Polygon, Point32
import StringIO
import time


poly = Polygon()
pnt1 = Point32()
pnt2 = Point32()
pnt3 = Point32()
pnt1.x = 1
pnt1.y = 2
pnt1.z = 3
pnt2.x = 40
pnt2.y = 50
pnt2.z = 60
pnt3.x = 700
pnt3.y = 800
pnt3.z = 900

print("hello")
print(poly)
poly = Polygon([pnt1, pnt2, pnt3])
# poly = Polygon([pnt1])
print(dir(poly))
# print(len(poly.__getstate__()[0]))
print(len(poly.points)) #could work
print(poly.points)
# print(poly.__format__())
print(poly.points[1])
fo = poly.points[1]
print(fo.x)

for i in poly.points:
    print("testing...")
    print(i.y)

# stobj = StringIO.StringIO()
#
# st = poly.serialize(stobj)
# print(stobj.getvalue())
# print(poly)
# new = Polygon()
# print(new)
# new.deserialize(stobj.getvalue())
# print(new)
# rospy.

# print(pnt)

def talker():
    rospy.init_node("tester", anonymous=True)
    pub_handle = rospy.Publisher("test_poly", Polygon, queue_size=10)
    time.sleep(1)
    rate_handle = rospy.Rate(10) #hz
    while not rospy.is_shutdown():
        pub_handle.publish(poly)
        print("publishing...")


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Polygon, Point32
import StringIO


rospy.init_node("tester", anonymous=True)

poly = Polygon()
pnt1 = Point32()
pnt2 = Point32()
pnt3 = Point32()
pnt1.x = 1
pnt1.y = 2
pnt1.z = 3
pnt2.x = 10
pnt2.y = 20
pnt2.z = 30
pnt3.x = 100
pnt3.y = 200
pnt3.z = 300

print("hello")
print(poly)
poly = Polygon([pnt1, pnt2, pnt3])
print(poly)

stobj = StringIO.StringIO()

st = poly.serialize(stobj)
print(stobj.getvalue())
print(poly)
new = Polygon()
print(new)
new.deserialize(stobj.getvalue())
print(new)
# rospy.

# print(pnt)

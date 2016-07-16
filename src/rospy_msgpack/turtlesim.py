
# import rospy
# from turtlesim.msg import Color

class Encode():
    def __init__(self):
        pass

    def color(self, data):
        msg = {}
        msg['r'] = data.r
        msg['g'] = data.g
        msg['b'] = data.b
        return(msg)

    def pose(self, data):
        msg = {}
        msg['x'] = data.x
        msg['y'] = data.y
        msg['theta'] = data.theta
        msg['lvelo'] = data.linear_velocity
        msg['avelo'] = data.angular_velocity
        return(msg)



class Decode():
    def __init__(self):
        pass

    def color(self, msg, obj):
        # color = Color()
        obj.r = msg['r']
        obj.g = msg['g']
        obj.b = msg['b']
        return(obj)

    def pose(self, msg, obj):
        obj.x = msg['x']
        obj.y = msg['y']
        obj.theta = msg['theta']
        obj.linear_velocity = msg['lvelo']
        obj.angular_velocity = msg['avelo']
        return(obj)

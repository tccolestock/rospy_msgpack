
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



class Decode():
    def __init__(self):
        pass

    def color(self, msg, obj):
        # color = Color()
        obj.r = msg['r']
        obj.g = msg['g']
        obj.b = msg['b']
        return(obj)

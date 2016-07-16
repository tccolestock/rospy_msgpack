
# import rospy
# from turtlesim.msg import Color

class Encode():
    def __init__(self):
        pass

    def Color(self, data):
        ser = {}
        ser['r'] = data.r
        ser['g'] = data.g
        ser['b'] = data.b
        return(ser)



class Decode():
    def __init__(self):
        pass

    def Color(self, ser, color):
        # color = Color()
        color.r = ser['r']
        color.g = ser['g']
        color.b = ser['b']
        return(color)

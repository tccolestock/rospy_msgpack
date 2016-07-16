
class Encode():
    def __init__(self):
        pass

    def twist(self, data):
        msg = {}
        msg['lx'] = data.linear.x
        msg['ly'] = data.linear.y
        msg['lz'] = data.linear.z
        msg['ax'] = data.angular.x
        msg['ay'] = data.angular.y
        msg['az'] = data.angular.z
        return(msg)


class Decode():
    def __init__(self):
        pass

    def twist(self, msg, obj):
         obj.linear.x = msg['lx']
         obj.linear.y = msg['ly']
         obj.linear.z = msg['lz']
         obj.angular.x = msg['ax']
         obj.angular.y = msg['ay']
         obj.angular.z = msg['az']
         return(obj)

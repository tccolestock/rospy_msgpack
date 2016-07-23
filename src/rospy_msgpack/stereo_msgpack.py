
from rospy_msgpack import interpret

encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def disparity_image(cls, obj):
        msg = {}
        h = encode.header(obj.header, "top")
        msg.update(h)
        h2 = encode.header(obj.image.header, "nest")
        msg.update(h2)
        msg['height'] = obj.image.height
        msg['width'] = obj.image.width
        msg['encoding'] = obj.image.encoding
        msg['is_bigendian'] = obj.image.is_bigendian
        msg['step'] = obj.image.step
        msg['data'] = obj.image.data
        msg['f'] = obj.f
        msg['T'] = obj.T
        r = encode.roi(obj.valid_window, "roi")
        msg.update(r)
        msg['min_disparity'] = obj.min_disparity
        msg['max_disparity'] = obj.max_disparity
        msg['delta_d'] = obj.delta_d
        return(msg)

class Decode():
    def __init__(self):
        pass

    def disparity_image(cls, msg, obj):
        obj.header = decode.header(msg, obj.header, "top")
        obj.image.header = decode.header(msg, obj.image.header, "nest")
        obj.image.height = msg['height']
        obj.image.width = msg['width']
        obj.image.encoding = msg['encoding']
        obj.image.is_bigendian = msg['is_bigendian']
        obj.image.step = msg['step']
        obj.image.data = msg['data']
        obj.f = msg['f']
        obj.T = msg['T']
        obj.valid_window = decode.roi(msg, obj.valid_window, "roi")
        obj.min_disparity = msg['min_disparity']
        obj.max_disparity = msg['max_disparity']
        obj.delta_d = msg['delta_d']
        return(obj)

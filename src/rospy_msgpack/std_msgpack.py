
from rospy_msgpack import interpret
from std_msgs.msg import MultiArrayDimension


encode = interpret.Encode()
decode = interpret.Decode()

class Encode():
    def __init__(self):
        pass

    def bool(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def byte(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def byte_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            dim = decode.multi_array_dimension(obj.layout.dim[i], i)
            msg.update(dim)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def char(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def color_rgba(cls, obj):
        msg = {}
        msg['r'] = obj.r
        msg['g'] = obj.g
        msg['b'] = obj.b
        msg['a'] = obj.a
        return(msg)

    def duration(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def empty(cls, obj):
        msg = {}
        return(msg)

    def float_32(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def float_32_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def float_64(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def float_64_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def header(cls, obj):
        msg = {}
        h = encode.header(obj, "")
        msg.update(h)
        return(msg)

    def int_16(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def int_16_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def int_32(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def int_32_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def int_64(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def int_64_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def int_8(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def int_8_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def multi_array_dimension(cls, obj):
        msg = {}
        m = encode.multi_array_dimension(obj, "")
        msg.update(m)
        return(m)

    def multi_array_layout(cls, obj):
        msg = {}
        msg['_length'] = len(obj.dim)
        for i in range(msg['_length']):
            m = encode.multi_array_dimension(obj.dim, i)
            msg.update(m)
        msg['data_offset'] = obj.data_offset
        return(msg)

    def string(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def time(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def uint_16(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def uint_16_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def uint_32(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def uint_32_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def uint_64(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def uint_64_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)

    def uint_8(cls, obj):
        msg = {}
        msg['data'] = obj.data
        return(msg)

    def uint_8_multi_array(cls, obj):
        msg = {}
        msg['_length'] = len(obj.layout.dim)
        for i in range(msg['_length']):
            f = encode.multi_array_dimension(obj.layout.dim, i)
            msg.update(f)
        msg['data_offset'] = obj.layout.data_offset
        msg['data'] = obj.data
        return(msg)


class Decode():
    def __init__(self):
        pass

    def bool(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def byte(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def byte_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def char(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def color_rgba(cls, msg, obj):
        obj.r = msg['r']
        obj.g = msg['g']
        obj.b = msg['b']
        obj.a = msg['a']
        return(obj)

    def duration(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def empty(cls, msg, obj):
        return(obj)

    def float_32(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def float_32_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def float_64(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def float_64_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def header(cls, msg, obj):
        obj = decode.header(msg, obj, "")
        return(obj)

    def int_16(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def int_16_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def int_32(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def int_32_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def int_64(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def int_64_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def int_8(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def int_8_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def multi_array_dimension(cls, msg, obj):
        obj = decode.multi_array_dimension(msg, obj, "")
        return(obj)

    def multi_array_layout(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.dim.append(mad)
        obj.data_offset = msg['data_offset']
        return(obj)

    def string(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def time(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def uint_16(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def uint_16_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def uint_32(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def uint_32_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def uint_64(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def uint_64_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

    def uint_8(cls, msg, obj):
        obj.data = msg['data']
        return(obj)

    def uint_8_multi_array(cls, msg, obj):
        for i in range(msg['_length']):
            mad = MultiArrayDimension()
            mad = decode.multi_array_dimension(msg, mad, i)
            obj.layout.dim.append(mad)
        obj.layout.data_offset = msg['data_offset']
        obj.data = msg['data']
        return(obj)

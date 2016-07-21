

class Encode():
    def __init__(self):
        pass

    # figure out DiagnositcArray

    # figure out DiagnosticStatus

    def key_value(self, data):
        msg = {}
        msg['key'] = data.key
        msg['value'] = data.value
        return(msg)



class Decode():
    def __init__(self):
        pass

    # figure out DiagnositcArray

    # figure out DiagnosticStatus

    def key_value(self, msg, obj):
        obj.key = msg['key']
        obj.value = msg['value']
        return(obj)

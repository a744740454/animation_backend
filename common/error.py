class ParamValidErr(Exception):
    def __init__(self, msg):
        self.msg = msg


class ProtocolParamError(Exception):
    def __init__(self, msg):
        self.msg = msg


class IsNotCallableObj(Exception):
    def __init__(self, msg):
        self.msg = msg


class APIError(Exception):
    def __init__(self, res_code):
        self.res_code = res_code

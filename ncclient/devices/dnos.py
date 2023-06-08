from .default import DefaultDeviceHandler

def passthrough(xml):
    return xml

class DnosDeviceHandler(DefaultDeviceHandler):
    """
    Drivenets OS handler for device specific information.
    """

    def __init__(self, device_params):
        super(DnosDeviceHandler, self).__init__(device_params)

    def transform_reply(self):
        return passthrough


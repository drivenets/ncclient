from .default import DefaultDeviceHandler
from ncclient.xml_ import BASE_NS_1_0


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
    
    def get_xml_base_namespace_dict(self):
        return {None: BASE_NS_1_0}

    def get_xml_extra_prefix_kwargs(self):
        d = {}
        d.update(self.get_xml_base_namespace_dict())
        return {"nsmap": d}

    def perform_qualify_check(self):
        return False

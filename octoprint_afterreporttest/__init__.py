# coding=utf-8
from __future__ import absolute_import
import json

import octoprint.plugin

class AfterReportTestPlugin(octoprint.plugin.types.OctoPrintPlugin):

    # ~~ EventHandlerPlugin hook
    def firmware_after_report_hook(self, comm_instance, firmware_capabilities, *args, **kwargs):
        self._logger.info("Capability Report Done: %s" % (json.dumps(firmware_capabilities)))

__plugin_name__ = "AfterReportTest Plugin"

__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = AfterReportTestPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.firmware.after_report": __plugin_implementation__.firmware_after_report_hook
    }

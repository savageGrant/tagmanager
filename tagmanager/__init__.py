from platform import system

from .tagmanager import *

OPERATING_SYSTEM = system()

manager = OSManager()
manager.register_manager('Darwin', MacOSTagManager())

tag_manager = manager.create(OPERATING_SYSTEM)


def _os_check():
    if OPERATING_SYSTEM != 'Darwin':
        raise RuntimeError("tagmanager does not currently "
                           "support OS: {}".format(OPERATING_SYSTEM))


_os_check()

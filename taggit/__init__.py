from platform import system

from .taggit import *


OPERATING_SYSTEM = system()


def _os_check():
    if OPERATING_SYSTEM != 'Darwin':
        raise RuntimeError("Taggit does not currently "
                           "support OS: {}".format(OPERATING_SYSTEM))


_os_check()

import os
import sys
import platform
import subprocess

from exceptions import *

if platform.system() == "Windows":
    raise PlatformNotSupportedError("Windows cannot possibly have coreutils installed and is not a supported configuration. Even if it does, it is under Cygwin and has way too much overhead to be accurate. Please install Linux or another UNIX-like system on your computer to continue.")

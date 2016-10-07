
"""
Usage::

    import install_cmake
    install_cmake.install()

"""

import os
import sys

from subprocess import check_call

DEFAULT_CMAKE_VERSION = "3.5.0"


def _log(*args):
    script_name = os.path.basename(__file__)
    print("[circle:%s] " % script_name + " ".join(args))
    sys.stdout.flush()


def install(cmake_version=DEFAULT_CMAKE_VERSION):
    """Download and install CMake into ``/usr/local``."""

    name = "cmake-{}-Linux-x86_64".format(cmake_version)

    cmake_package = "{}.tar.gz".format(name)

    _log("Downloading ", cmake_package)

    cmake_version_major = cmake_version.split(".")[0]
    cmake_version_minor = cmake_version.split(".")[1]

    check_call([
        "wget", "--no-check-certificate", "--progress=dot",
        "https://cmake.org/files/v{}.{}/{}".format(
            cmake_version_major, cmake_version_minor, cmake_package)
    ])

    _log("Extracting", cmake_package)
    check_call(["tar", "xzf", name + ".tar.gz"])

    _log("Installing", name)
    check_call([
        "sudo", "rsync", "-avz", name + "/", "/usr/local"
    ])


if __name__ == '__main__':
    install(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CMAKE_VERSION)

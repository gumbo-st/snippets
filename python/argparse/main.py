#!/usr/local/env python

import sys
import traceback
import argparse
import pathlib

import common
import argparse_utils


# arparse needs python >= v3.2
# pathlib needs python >= v3.4
try:
    assert sys.version_info >= (3, 4 )
except AssertionError:
    print("ERROR: Argparse needs at least Python v3.2. Exiting applicatoin...")
    exit(1)


# Need global variables
gbls = common.CommonUtils()
# parse CLI flags
cliargs = argparse_utils.ArgparseUtils(gbls)
if gbls.prog_exit == True:
    sys.exit(-1)


if __name__ == "__main__":
    """
    Typical python runtime main() function
    """
    if (gbls.verbose == True):
        print("Verbose Mode Enabled")
    if (gbls.debug == True):
        print("Debug Mode Enabled")

        print("glbs.var1=" + str(gbls.var1))
        print("glbs.var2=" + str(gbls.var2))
        print("glbs.var3=" + str(gbls.var3))
    else:
        print("Enable debug to see output")






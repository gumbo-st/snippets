#!/usr/local/env python

import sys
import traceback
import argparse

import common
import argparse_utils

# arparse needs python >= v3.2
try:
    assert sys.version_info >= (3, 2)
except AssertionError:
    print("ERROR: Argparse needs at least Python v3.2. Exiting applicatoin...")
    exit(1)


# Need global variables
gbls = common.CommonUtils()
# parse CLI flags
cliargs = argparse_utils.ArgparseUtils(gbls)


if __name__ == "__main__":
    print("glbs.var1=" + str(gbls.var1))
    print("glbs.var2=" + str(gbls.var2))
    print("glbs.var3=" + str(gbls.var3))






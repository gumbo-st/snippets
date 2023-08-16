#!/usr/local/env python
import sys
import pathlib

PY_CMD="python"
#PY_CMD="python3"

# pathlib needs python >= v3.4
try:
    assert sys.version_info >= (3, 4)
except AssertionError:
    print("ERROR: pathlib needs at least Python v3.4. Exiting applicatoin...")
    exit(1)

# clean python dir of bytecode
for p in pathlib.Path('.').rglob('*.py[co]'): p.unlink()
for p in pathlib.Path('.').rglob('__pycache__'): p.rmdir()



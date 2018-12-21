#!/usr/bin/python
#
# Call the command line interface for Epydoc.
#

import os.path
# We have to do some path magic to prevent Python from getting
# confused about the difference between this epydoc module, and the
# real epydoc package.  So remove sys.path[0], which contains the
# directory of the script.
import sys

from epydoc.cli import cli

script_path = os.path.abspath(sys.path[0])
sys.path = [p for p in sys.path if
            os.path.abspath(p) != script_path]

cli()

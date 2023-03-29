#!/usr/bin/env python3
#
#
# (c) 2022 Robert Bosch GmbH
#
# All files and artifacts in this repository are licensed under the
# provisions of the license provided by the LICENSE file in this repository.
#
#
# Convert vspec2csv wrapper for vspec2x
#

# Deliberate trailing spaces below
       
import sys
import vspec2x

if __name__ == "__main__":
    vspec2x.main(["--format", "csv"]+sys.argv[1:])

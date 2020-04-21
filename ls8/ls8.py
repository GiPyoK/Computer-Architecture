#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

program = []
file_name = sys.argv[-1]
with open(file_name) as f:
    for line in f:
        line = line.split('#')
        line = line[0].strip()
        if line == '':
            continue
        program.append(int(line, 2))
print(program)
cpu = CPU()
cpu.load(program)
cpu.run()
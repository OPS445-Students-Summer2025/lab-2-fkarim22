#!/usr/bin/env python3

# Author: Faisal Karim
# Author ID: 147424238
# Date Created: 2025/05/21

import sys

# This code is to determine if a command-line argument was provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3  # Default value if not any of the argument is given

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

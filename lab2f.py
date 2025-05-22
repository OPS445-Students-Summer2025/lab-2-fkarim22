#!/usr/bin/env python3

# Author: Faisal Karim
# Author ID: 147424238
# Date Created: 2025/05/21

import sys

# This code is to assign first command-line argument as an integer to timer
timer = int(sys.argv[1])

# For countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
#!/usr/bin/env python3

import sys

# This will check if exactly 2 arguments are provided
if len(sys.argv) != 3: # we did three because the script name is itself counted as and argument{0}
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# This code will then assign command-line arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])  # This will Convert age from string to integer

# Finally this will Print the hi message along with name and age
print(f"Hi {name}, you are {age} years old.")

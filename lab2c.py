#!/usr/bin/env python3

import sys

# This will Assign command-line arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])  # This will Convert age from string to integer

# This will Print the greeting message
print(f"Hi {name}, you are {age} years old.")


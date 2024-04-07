#!/usr/bin/env python3

import sys

# Reducer to return overall top 10 NBA players by efficiency (EFF)
# Data passed from mapper should be in the format produced by your modified mapper script, which includes the EFF as part of the record

# Initialize a list to store the top N records as a collection of tuples (EFF, record)
myList = []
n = 10  # Number of top N records

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split data values into list
    # Assuming the mapper output is comma-separated as modified in the mapper script
    data = line.split(",")

    # Skip rows that don't contain the expected number of columns
    if len(data) < 29:
        continue

    try:
        # The EFF column is expected to be the 28th column based on the provided structure
        eff = float(data[27])  # Convert efficiency (currently a string) to float
    except ValueError:
        # Ignore/discard this line if conversion fails
        continue
    
    # Add (EFF, record) tuple to list
    myList.append((eff, line))
    # Sort list in reverse order by EFF
    myList.sort(reverse=True, key=lambda x: x[0])
    
    # Keep only the first N records
    if len(myList) > n:
        myList = myList[:n]

# Print top N records
for (_, v) in myList:
    print(v)


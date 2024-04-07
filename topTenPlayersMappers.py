#!/usr/bin/env python3

import sys

# Mapper to return local top 10 NBA players by efficiency (EFF)
# Data is expected to be in the structure as provided in the uploaded CSV
# Expected Data header: Year, Season_type, PLAYER_ID, RANK, PLAYER, TEAM_ID, TEAM, GP, MIN, FGM, ..., PTS, EFF, AST_TOV, STL_TOV
# Note: Data columns are indexed starting from 0

# Initialize a list to store the top N records as a collection of tuples (EFF, record)
myList = []
n = 10  # Number of top N records

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split data values into list
    data = line.split(",")

    # Skip rows that don't contain the expected number of columns
    if len(data) < 29:
        continue

    year = data[0]
    # Check if year is within the specified range
    if year >= "2012-13" and year <= "2021-22":
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

#!/usr/bin/env python

'''
preprocess_age.py
  Author(s): Amir Kayumov (1386890)

  Module: Question 2 Analyzer
  Date of Last Update: Mar 23, 2026.

  Functional Summary

  Reads a raw age turnout dataset and extracts voter turnout data specifically for 
    the province of Ontario and a user-specified age. It filters the data based on 
    age ranges provided in the source file and outputs a cleaned CSV.

    Usage:
        python3 preprocess_age.py <target_age> <age_turnout_table.csv> > processed_age.csv
    Effect:
        Outputs a CSV stream containing:
            - Year
            - Turnout (normalized to a 100-base percentage)
            - Age Group range label
'''

#
#   Packages and modules
#

# The 'sys' module allows for command line argument handling and standard output writing
import sys

# The 'csv' module provides tools for reading raw data and formatting output as CSV
import csv

# The 're' (Regular Expression) module helps extract numeric age ranges from string labels
import re


##
## Mainline function
##
def main(argv):

    # Verify that the correct number of arguments are provided
    if len(argv) != 3:
        print("Usage: preprocess_age.py <target_age_group> <datasets/age_turnout_table.csv> > processed_age.csv", file=sys.stderr)
        sys.exit(1)

    # Ensure the target age provided is a valid integer
    try:
        target_age_group = int(argv[1])
    except ValueError:
        print("Error: argument <target_age_group> is not an integer.", file=sys.stderr)
        print(print("Usage: preprocess_age.py <target_age_group> <datasets/age_turnout_table.csv> > processed_age.csv", file=sys.stderr))
        sys.exit(1)
    filename = argv[2]

    # Attempt to open the raw data file
    try:
        infile = open(filename, newline = '', encoding="utf-8-sig")
    except IOError:
        print(f"Error: Could not open the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    # Initialize CSV reader for the input and writer for standard output
    reader = csv.DictReader(infile)
    writer = csv.writer(sys.stdout, lineterminator='\n')

    # Write the header row for the new processed CSV
    writer.writerow(["Year", "Turnout", "Age Group"])

    # Process each row in the source dataset
    for row in reader:

        # Use regex to find all numbers in the age group label (e.g., "18-24" -> [18, 24])
        age_group = re.findall(r'\d+', row.get("AGE_GROUP_E"))

        # Check if we successfully found a range (start and end age)
        if (len(age_group) == 2):
            try: 
                age_floor = int(age_group[0])
                age_ceiling = int(age_group[1])
            except ValueError:
                continue

            # We filter out the information to specifically only include rows that are within bounds of target age AND are within Ontario
            if (target_age_group >= age_floor and target_age_group <= age_ceiling and row.get("PROVINCE_E") == "Ontario"):
                year = row.get("YEAR")
                turnout = float(row.get("TURNOUT_ELIGIBLE_ELECTOR")) * 100 # Convert decimal turnout (e.g., 0.65) to percentage (65.0000)
                writer.writerow([year, f'{turnout:.4f}', f'{age_floor} to {age_ceiling}'])
    
    # Close the input file stream
    infile.close()
            

##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)

#
#   End of Script
#
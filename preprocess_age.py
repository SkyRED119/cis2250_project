#!/usr/bin/env python

'''
preprocess_age.py
  Author(s): Amir Kayumov (1386890)

  Module: Question 2 Analyzer
  Date of Last Update: Mar 23, 2026.

  Functional Summary
    
'''

import sys
import csv
import re


def main(argv):

    if len(argv) != 3:
        print("Usage: preprocess_age.py <target_age_group> <datasets/age_turnout_table.csv> > processed_age.csv", file=sys.stderr)
        sys.exit(1)

    try:
        target_age_group = int(argv[1])
    except ValueError:
        print("Error: argument <target_age_group> is not an integer.", file=sys.stderr)
        print(print("Usage: preprocess_age.py <target_age_group> <datasets/age_turnout_table.csv> > processed_age.csv", file=sys.stderr))
        sys.exit(1)
    filename = argv[2]

    try:
        infile = open(filename, newline = '', encoding="utf-8-sig")
    except IOError:
        print(f"Error: Could not open the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)
    writer = csv.writer(sys.stdout, lineterminator='\n')

    writer.writerow(["Year", "Turnout"])

    for row in reader:
        age_group = re.findall(r'\d+', row.get("AGE_GROUP_E"))
        if (len(age_group) == 2):
            try: 
                age_floor = int(age_group[0])
                age_ceiling = int(age_group[1])
            except ValueError:
                continue

            if (target_age_group > age_floor and target_age_group < age_ceiling and row.get("PROVINCE_E") == "Ontario"):
                year = row.get("YEAR")
                turnout = float(row.get("TURNOUT_ELIGIBLE_ELECTOR"))
                writer.writerow([year, f'{turnout:.4f}'])
    
    infile.close()
            

##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)
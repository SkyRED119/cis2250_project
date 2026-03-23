#!/usr/bin/env python

'''
analyer_q2.py
  Author(s): Amir Kayumov (1386890)

  Module: Question 2 Analyzer
  Date of Last Update: Mar 16, 2026.

  Functional Summary
    
'''

import sys
import csv
import re

def load_ages(filename):

    age_data = {}

    try: 
        infile = open(filename, newline='', encoding='utf-8-sig')
    except IOError:
        print(f"Couldn't open the file: {filename}", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)

    for row in reader:
        year = row.get("Year")
        age_group = row.get("Age group")

        ages = re.findall(r"\d+", age_group)

        try:
            for age in range(ages[0], ages[1]+1):
                age_data[int(year)] = int(age)
        except (TypeError, ValueError):
            continue
    
    infile.close()

    return age_data

def main(argv):
    load_ages(argv[1])

##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)
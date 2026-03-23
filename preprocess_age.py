#!/usr/bin/env python

'''
preprocess_age.py
  Author(s): Amir Kayumov (1386890)

  Module: Question 2 Analyzer
  Date of Last Update: Mar 19, 2026.

  Functional Summary
    
'''

import sys
import csv


def main(argv):

    if len(argv) != 2:
        print("Usage: preprocess_age.py <datasets/age_turnout_table.csv> > processed_age.csv", file=sys.stderr)
        sys.exit(1)

    filename = argv[1]

    try:
        infile = open(filename, newline = '', encoding="utf-8-sig")
    except IOError:
        print(f"Error: Could not open the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)
    writer = csv.writer(sys.stdout, lineterminator='\n')

    writer.writerow(["Year", "Age Group"])

    ages = {}

    
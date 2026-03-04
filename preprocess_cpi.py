#!/usr/bin/env python

'''
number_csv_rows.py
  Author(s): Hieu Hoang (1390265), 

  Module: CPI Preprocessor 
  Date of Last Update: Mar 04, 2026.

  Functional Summary
    Reads CPI CSV and outputs processed_inflation.csv for Q1.
	Usage:
        python3 preprocess_cpi_q1.py <cpi_input.csv> > processed_inflation.csv
'''


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

TARGET_GEO = "Ontario"
TARGET_PRODUCT = "All-items"
TARGET_MONTHS = {"2018-10", "2019-10", "2020-09", "2021-09"}

##
## Mainline function
##
def main(argv):
    if len(argv) != 2:
        print("Usage: preprocess_cpi_q1.py <cpi_input.csv>", file=sys.stderr)
        sys.exit(1)
    
    infile = open(argv[1], newline='', encoding="utf-8-sig")
    reader = csv.DictReader(infile)
    writer = csv.writer(sys.stdout)
    writer.writerow(["year", "inflation_rate"])

    cpi = {}  # ref_date -> value
    for row in reader:
        if row.get("GEO") != TARGET_GEO:
            continue
        if row.get("Products and product groups") != TARGET_PRODUCT:
            continue
        ref_date = row.get("REF_DATE")
        if ref_date not in TARGET_MONTHS:
            continue

        try:
            cpi[ref_date] = float(row["VALUE"])
        except (KeyError, ValueError):
            continue

    if "2018-10" in cpi and "2019-10" in cpi:
        infl_2019 = (cpi["2019-10"] - cpi["2018-10"]) / cpi["2018-10"] * 100.0
        writer.writerow([2019, f"{infl_2019:.4f}"])
    else:
        print("Missing CPI months for 2019 inflation.", file=sys.stderr)

    if "2020-09" in cpi and "2021-09" in cpi:
        infl_2021 = (cpi["2021-09"] - cpi["2020-09"]) / cpi["2020-09"] * 100.0
        writer.writerow([2021, f"{infl_2021:.4f}"])
    else:
        print("Missing CPI months for 2021 inflation.", file=sys.stderr)

    infile.close()



##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

#!/usr/bin/env python

'''
preprocess_cpi.py
  Author(s): Hieu Hoang (1390265), Amir Kayumov (1386890)

  Module: CPI Preprocessor 
  Date of Last Update: Mar 19, 2026.

  Functional Summary
    Reads CPI CSV and outputs processed_inflation.csv for Q1.
	Usage:
        python3 preprocess_cpi.py <datasets/cpi_table.csv> > processed_inflation.csv
    Effect:
        Produces a CSV file containing the computed inflation rates
        for Ontario prior from 2004 and 2025 federal elections.

        Output format:
            Year,Inflation Rate
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
TARGET_MONTHS = {"2003-06","2004-06","2005-01","2006-01","2007-10","2008-10","2010-05","2011-05","2014-10","2015-10",
                 "2018-10", "2019-10", "2020-09", "2021-09", "2024-08", "2025-08"}

##
## Mainline function
##
def main(argv):

    if len(argv) != 2:
        print("Usage: preprocess_cpi.py <datasets/cpi_table.csv> > processed_inflation.csv", file=sys.stderr)
        sys.exit(1)

    filename = argv[1]

    try:
        infile = open(filename, newline = '', encoding="utf-8-sig")
    except IOError:
        print(f"Error: Could not open the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["Year", "Inflation Rate"])

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

    if "2003-06" in cpi and "2004-06" in cpi:
        infl_2004 = (cpi["2004-06"] - cpi["2003-06"]) / cpi["2003-06"] * 100.0
        writer.writerow([2004, f"{infl_2004:.2f}"])
    else:
        print("Missing CPI months for 2004 inflation.", file=sys.stderr)

    if "2005-01" in cpi and "2006-01" in cpi:
        infl_2006 = (cpi["2006-01"] - cpi["2005-01"]) / cpi["2005-01"] * 100.0
        writer.writerow([2006, f"{infl_2006:.2f}"])
    else:
        print("Missing CPI months for 2006 inflation.", file=sys.stderr)
    
    if "2007-10" in cpi and "2008-10" in cpi:
        infl_2008 = (cpi["2008-10"] - cpi["2007-10"]) / cpi["2007-10"] * 100.0
        writer.writerow([2008, f"{infl_2008:.2f}"])
    else:
        print("Missing CPI months for 2008 inflation.", file=sys.stderr)

    if "2010-05" in cpi and "2011-05" in cpi:
        infl_2011 = (cpi["2011-05"] - cpi["2010-05"]) / cpi["2010-05"] * 100.0
        writer.writerow([2011, f"{infl_2011:.2f}"])
    else:
        print("Missing CPI months for 2011 inflation.", file=sys.stderr)
    
    if "2014-10" in cpi and "2015-10" in cpi:
        infl_2015 = (cpi["2015-10"] - cpi["2014-10"]) / cpi["2014-10"] * 100.0
        writer.writerow([2015, f"{infl_2015:.2f}"])
    else:
        print("Missing CPI months for 2015 inflation.", file=sys.stderr)

    if "2018-10" in cpi and "2019-10" in cpi:
        infl_2019 = (cpi["2019-10"] - cpi["2018-10"]) / cpi["2018-10"] * 100.0
        writer.writerow([2019, f"{infl_2019:.2f}"])
    else:
        print("Missing CPI months for 2019 inflation.", file=sys.stderr)

    if "2020-09" in cpi and "2021-09" in cpi:
        infl_2021 = (cpi["2021-09"] - cpi["2020-09"]) / cpi["2020-09"] * 100.0
        writer.writerow([2021, f"{infl_2021:.2f}"])
    else:
        print("Missing CPI months for 2021 inflation.", file=sys.stderr)

    if "2024-08" in cpi and "2025-08" in cpi:
        infl_2025 = (cpi["2025-08"] - cpi["2024-08"]) / cpi["2024-08"] * 100.0
        writer.writerow([2025, f"{infl_2025:.2f}"])
    else:
        print("Missing CPI months for 2025 inflation.", file=sys.stderr)

    infile.close()



##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

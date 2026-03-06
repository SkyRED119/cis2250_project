#!/usr/bin/env python

'''
analyer_q1.py
  Author(s): Hieu Hoang (1390265), 

  Module: Question 1 Analyzer
  Date of Last Update: Mar 06, 2026.

  Functional Summary
    Reads the processed CPI and election CSV files for Question 1,compares the 2019 and 2021 Ontario inflation rates and vote
    percentages for the selected party, and reports the computed changes.
	Usage:
        python3 analyzer_q1.py <processed_inflation.csv> <processed_vote_percentages.csv> 
    Effect:
        Produce a report showing:
            - 2019 inflation rate
            - 2021 inflation rate 
            - 2019 Ontario vote percentage
            - 2021 Ontario vote percentage
            - Inflation change
            - Vote percentage change
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


##
## Read infaltion data
## This function reads processed_inflation.csv and returns a dictionary called:
## inflation_data[year] = inflation_rate

def load_inflation(filename):

    inflation_data = {}

    try: 
        infile = open(filename, newline='', encoding='utf-8-sig')
    except IOError:
        print(f"Couldn't open the file: {filename}", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)

    for row in reader:
        year = row.get("Year")
        inflation_rate = row.get("Inflation Rate")

        try:
            inflation_data[int(year)] = float(inflation_rate)
        except (TypeError, ValueError):
            continue
    
    infile.close()

    return inflation_data
        

##
## Read vote percentage data
## This function reads processed_vote_percentages.csv and returns a pair of information:
## party_name and a dictionary called vote_data[year] = ontario_vote_percent 

def load_votes(filename):
    
    vote_data = {}

    party_name = None

    try: 
        infile = open(filename, newline='', encoding='utf-8-sig')
    except IOError:
        print(f"Couldn't open the file: {filename}", file=sys.stderr)
        sys.exit(1)
    
    reader = csv.DictReader(infile)

    for row in reader:
        year = row.get("Year")
        party = row.get("Party")
        vote_percentage = row.get("Ontario Vote Percentage")

        if party_name is None:
            party_name = party
        
        try:
            vote_data[int(year)] = float(vote_percentage)
        except (TypeError, ValueError):
            continue

    infile.close()

    return party_name, vote_data


##
## Mainline function
##
def main(argv):

    if len(argv) != 3:
        print("Usage: analyzer_q1.py <processed_inflation.csv> <processed_vote_percentages.csv>", file=sys.stderr)
        sys.exit(1)
    
    inflation_file = argv[1]
    vote_file = argv[2]

    inflation_data = load_inflation(inflation_file)
    party_name, vote_data = load_votes(vote_file)

    required_year = [2019, 2021]

    for year in required_year:
        if year not in inflation_data:
            print(f"Error: missing inflation data for {year}", file=sys.stderr)
            sys.exit(1)
        if year not in vote_data:
            print(f"Error: missing vote percentage data for {year}", file=sys.stderr)
            sys.exit(1)

    inflation_2019 = inflation_data[2019]
    inflation_2021 = inflation_data[2021]

    vote_2019 = vote_data[2019]
    vote_2021 = vote_data[2021]

    inflation_change = inflation_2021 - inflation_2019
    vote_change = vote_2021 - vote_2019

    #Print report

    print("Question 1 Analysis Report")
    print("--------------------------")
    print(f"Party: {party_name}")
    print(f"Ontario inflation rate in 2019: {inflation_2019:.2f}%")
    print(f"Ontario inflation rate in 2021: {inflation_2021:.2f}%")
    print(f"Ontario vote percentage in 2019: {vote_2019:.2f}%")
    print(f"Ontario vote percentage in 2021: {vote_2021:.2f}%")
    print("Calculating change...")
    print(f"-- Inflation change (2019 to 2021): {inflation_change:.2f}")
    print(f"-- Vote percentage change (2019 to 2021): {vote_change:.2f}")

    #Overall Evaluation

    print("\n\nOverall Evaluation from 2019 to 2021 in Ontario:")
    if inflation_change > 0:
        print("-- Inflation increased between the two elections.")
    elif inflation_change < 0:
        print("-- Inflation decreased between the two elections.")
    else:
        print("-- Inflation did not change between the two elections.")
    
    if vote_change > 0:
        print(f"-- {party_name} gained more vote during the period.")
    elif vote_change < 0:
        print(f"-- {party_name} gained less vote during the period.")
    else:
        print(f"-- {party_name} had no change in vote during the period.")

    #Quick CSV-style summary

    print("\n\nSummary table")
    print("--------------------")
    print("Year,Inflation Rate,Ontario Vote Percentage")
    print(f"2019,{inflation_2019:.2f},{vote_2019:.2f}")
    print(f"2021,{inflation_2021:.2f},{vote_2021:.2f}")
    print(f"Change,{inflation_change:.2f},{vote_change:.2f}")


##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

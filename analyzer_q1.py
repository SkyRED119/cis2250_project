#!/usr/bin/env python

'''
analyer_q1.py
  Author(s): Hieu Hoang (1390265), 

  Module: Question 1 Analyzer
  Date of Last Update: Mar 06, 2026.

  Functional Summary
    Reads the processed CPI and election CSV files for Question 1, checks that all required election years from 2004 to 2025
    are present, then compares Ontario inflation rates and vote percentages for the selected party year by year across consecutive
    elections. 

	Usage:
        python3 analyzer_q1.py <processed_inflation.csv> <processed_vote_percentages.csv> 
    Effect:
        Produce a report showing:
            - inflation rate
            - Ontario vote percentage
            - inflation change
            - vote percentage change
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

# The 'matplotlib.pyplot' module allows us to creates visualizations
# such as bar charts and graphs for data analysis

import matplotlib.pyplot as pyplot


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
## Visualize datas
## This function creates a grouped bar chart comparing inlfation change and vote change
## Parameter: periods (a list of different periods, e.g. ["2004-2006",..] ), inflation_change, vote_change, party_name

def visualization(periods, inflation_changes, vote_changes, party_name):
    
    #Create posistions for bars on the x axis
    x_positions = list(range(len(periods)))
    
    #Plot inflation change bars
    inflation_positions = [i for i in x_positions]
    vote_positions = [i+0.5 for i in x_positions]

    #Create the bar chart
    pyplot.figure(figsize=(15,8))   
    pyplot.bar(inflation_positions, inflation_changes, width=0.5, label="Inflation Changes")
    pyplot.bar(vote_positions, vote_changes, width=0.5, label="Vote Changes")

    #Draw a horizontal line at y = 0 to seperate the positive changes and negative changes
    pyplot.axhline(0, linewidth=1)

    #Label the axes and title
    pyplot.xlabel("Election Period")
    pyplot.ylabel("Percentage Change")
    pyplot.title(f"Ontario Inflation Change vs Vote Percentage Change for {party_name}")

    #Put the election periods labels at the center at the end of each bar pair
    pyplot.xticks(x_positions, periods, rotation=45)

    #Add a legend and adjust spacing
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.savefig("q1_visualiztion.png")

    #Show the visualization
    pyplot.show()
    

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

    required_years = [2004, 2006, 2008, 2011, 2015, 2019, 2021, 2025]

    for year in required_years:
        if year not in inflation_data:
            print(f"Error: missing inflation data for {year}", file=sys.stderr)
            sys.exit(1)
        if year not in vote_data:
            print(f"Error: missing vote percentage data for {year}", file=sys.stderr)
            sys.exit(1)

    print("\nQuestion 1 Analysis Report")
    print("----------------------------")
    print(f"Party: {party_name}")

    # Create lists for visualization 

    periods = []
    inflation_changes = []
    vote_changes = []

    for i in range(len(required_years) - 1):
        year1 = required_years[i]
        year2 = required_years[i+1]

        inflation1 = inflation_data[year1]
        inflation2 = inflation_data[year2]
        vote1 = vote_data[year1]
        vote2= vote_data[year2]

        inflation_change = inflation2 - inflation1
        vote_change = vote2 - vote1

        #Save datas inside created lists for plotting visualization
        periods.append(f"{year1}-{year2}")
        inflation_changes.append(inflation_change)
        vote_changes.append(vote_change)

        print(f"\nComparison: {year1} to {year2}")
        print(f"Ontario inflation rate in {year1}: {inflation1:.2f}%")
        print(f"Ontario inflation rate in {year2}: {inflation2:.2f}%")
        print(f"Ontario vote percentage in {year1}: {vote1:.2f}%")
        print(f"Ontario vote percentage in {year2}: {vote2:.2f}%")
        print(f"Inflation change: {inflation_change:.2f}%")
        print(f"Vote percentage change: {vote_change:.2f}%")
        
        if (inflation_change > 0):
            print("-- Inflation increased in this period")
        elif (inflation_change < 0):
            print("-- Inflation decreased in this period")
        else:
            print("-- Inflation did not change in this period")

        if (vote_change > 0):
            print(f"-- {party_name} gained vote in this period")
        elif (vote_change < 0):
            print(f"-- {party_name} lost vote in this period")
        else:
            print(f"-- {party_name} had no vote change in this period")
    
    print("\nSummary Table")
    print("-----------------")
    print(f"From-To,Inflation Change, Vote Percentage Change for {party_name}")

    for i in range(len(required_years) - 1):
        year1 = required_years[i]
        year2 = required_years[i+1]

        inflation_change = inflation_data[year2] - inflation_data[year1]
        vote_change = vote_data[year2] - vote_data[year1]

        print(f"{year1}-{year2},{inflation_change:.2f},{vote_change:.2f}")

    visualization(periods, inflation_changes, vote_changes, party_name)

##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

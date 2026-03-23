#!/usr/bin/env python

'''
analyer_q2.py
  Author(s): Amir Kayumov (1386890)
  Special Note: A majority of this code is inspired by the work done by Hieu "Talon" Hoang in "analyzer_q1.py".

  Module: Question 2 Analyzer
  Date of Last Update: Mar 23, 2026.

  Functional Summary
    
'''

import sys
import csv
import matplotlib.pyplot as pyplot
from scipy import stats

def load_ages(filename):

    age_data = {}
    age_group = ''

    try: 
        infile = open(filename, newline='', encoding='utf-8-sig')
    except IOError:
        print(f"Couldn't open the file: {filename}", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)

    for row in reader:
        age_group = row.get("Age Group")
        year = row.get("Year")
        turnout = row.get("Turnout")

        try:
            age_data[int(year)] = float(turnout)
        except (TypeError, ValueError):
            continue
    
    infile.close()

    return age_group, age_data

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
## Parameter: periods (a list of different periods, e.g. ["2004-2006",..] ), turnout_changes, vote_change, party_name

def visualization(periods, turnout_changes, vote_changes, party_name, age_group):
    
    #Create posistions for bars on the x axis
    x_positions = list(range(len(periods)))
    
    #Plot inflation change bars
    inflation_positions = [i for i in x_positions]
    vote_positions = [i+0.5 for i in x_positions]

    #Create the bar chart
    pyplot.figure(figsize=(15,8))   
    pyplot.bar(inflation_positions, turnout_changes, width=0.5, label="Turnout Changes")
    pyplot.bar(vote_positions, vote_changes, width=0.5, label="Vote Changes")

    #Draw a horizontal line at y = 0 to seperate the positive changes and negative changes
    pyplot.axhline(0, linewidth=1)

    #Label the axes and title
    pyplot.xlabel("Election Period")
    pyplot.ylabel("Percentage Change")
    pyplot.title(f"Ontario Turnout Percentage Change for {age_group} Year Olds vs Vote Percentage Change for {party_name}")

    #Put the election periods labels at the center at the end of each bar pair
    pyplot.xticks(x_positions, periods, rotation=45)

    #Add a legend and adjust spacing
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.savefig("q2_visualization.png")

    #Show the visualization
    pyplot.show()


def run_statistical_analysis(turnout_list, vote_list, party_name):
    print("\nStatistical Correlation Analysis")
    print("--------------------------------")
    
    # Calculate Pearson Correlation
    # r = correlation coefficient, p = probability it's due to chance
    r, p = stats.pearsonr(turnout_list, vote_list)
    
    print(f"Analysis for {party_name}:")
    print(f"Pearson Correlation Coefficient (r): {r:.4f}")
    print(f"P-value: {p:.4f}")
    
    # Interpretation
    if p < 0.05:
        print("Result: Statistically Significant (p < 0.05)")
    else:
        print("Result: Not Statistically Significant (p > 0.05)")
        
    if r > 0.7:
        print("Strength: Strong Positive Correlation")
    elif r < -0.7:
        print("Strength: Strong Negative Correlation")
    elif abs(r) < 0.3:
        print("Strength: Weak or No Correlation")

def main(argv):

    if (len(argv) != 3):
        print("Usage: analyzer_q2.py <processed_age_turnout.csv> <processed_vote_percentages.csv>", file=sys.stderr)
        sys.exit(1)

    age_turnout_file = argv[1]
    votes_file = argv[2]

    age_group, age_turnout_data = load_ages(age_turnout_file)
    party_name, vote_data = load_votes(votes_file)

    required_years = [2004, 2006, 2008, 2011, 2015, 2019, 2021, 2025]

    for year in required_years:
        if year not in age_turnout_data:
            print(f"Error: missing age turnout data for {year}", file=sys.stderr)
            sys.exit(1)
        if year not in vote_data:
            print(f"Error: missing vote percentage data for {year}", file=sys.stderr)
            sys.exit(1)

    print("\nQuestion 2 Analysis Report")
    print("----------------------------")
    print(f"Party: {party_name}")

    # Create lists for visualization 

    periods = []
    turnout_changes = []
    vote_changes = []

    for i in range(len(required_years) - 1):
        year1 = required_years[i]
        year2 = required_years[i+1]

        turnout1 = age_turnout_data[year1]
        turnout2 = age_turnout_data[year2]
        vote1 = vote_data[year1]
        vote2= vote_data[year2]

        turnout_change = turnout2 - turnout1
        vote_change = vote2 - vote1

        #Save datas inside created lists for plotting visualization
        periods.append(f"{year1}-{year2}")
        turnout_changes.append(turnout_change)
        vote_changes.append(vote_change)

        print(f"\nComparison: {year1} to {year2}")
        print(f"Ontario turnout percentage for {age_group} years olds in {year1}: {turnout1:.2f}%")
        print(f"Ontario turnout percentage for {age_group} years olds in {year2}: {turnout2:.2f}%")
        print(f"Ontario vote percentage in {year1}: {vote1:.2f}%")
        print(f"Ontario vote percentage in {year2}: {vote2:.2f}%")
        print(f"Turnout percentage change: {turnout_change:.2f}%")
        print(f"Vote percentage change: {vote_change:.2f}%")
        
        if (turnout_change > 0):
            print(f"-- Turnout for {age_group} years olds increased in this period")
        elif (turnout_change < 0):
            print(f"-- Turnout for {age_group} years olds decreased in this period")
        else:
            print(f"-- Turnout for {age_group} years olds did not change in this period")

        if (vote_change > 0):
            print(f"-- {party_name} gained vote in this period")
        elif (vote_change < 0):
            print(f"-- {party_name} lost vote in this period")
        else:
            print(f"-- {party_name} had no vote change in this period")
    
    print("\nSummary Table")
    print("-----------------")
    print(f"From-To,Turnout Percentage Change for {age_group} years olds, Vote Percentage Change for {party_name}")

    for i in range(len(required_years) - 1):
        year1 = required_years[i]
        year2 = required_years[i+1]

        turnout_change = age_turnout_data[year2] - age_turnout_data[year1]
        vote_change = vote_data[year2] - vote_data[year1]

        print(f"{year1}-{year2},{turnout_change:.2f},{vote_change:.2f}")

    run_statistical_analysis(turnout_changes, vote_changes, party_name)

    visualization(periods, turnout_changes, vote_changes, party_name, age_group)


##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)
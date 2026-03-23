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
            print(f"Error: missing inflation data for {year}", file=sys.stderr)
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



##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)
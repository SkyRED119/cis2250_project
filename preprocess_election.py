#!/usr/bin/env python

'''
preprocess_election.py
  Author(s): Hieu Hoang (1390265), 

  Module: Election Preprocessor 
  Date of Last Update: Mar 04, 2026.

  Functional Summary
    Reads 2019 and 2021 election Table 9 CSV files and outputs processed_votes_percentage.csv for question 1
	Usage:
        python3 preprocess_election.py <datasets/2019_election.csv> <datasets/2021_election.csv> <party_name> > processed_vote_percentages.csv
    Effect:
        Produce a CSV file containing the Ontario percentage of valid votes
        for the specified political party in the 2019 and 2021 elections.

        Output format:
            Year,Party,Ontario Vote Percentage

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
## Helper function
##

def extract_party_vote(filename, target_party):
    # We need this function because we need to extract each csv file and return the Ontario
    # percentage of valid votes for the selected party

    try:
        infile = open(filename, newline = '', encoding="utf-8-sig")
    except IOError:
        print(f"Error: Could not open the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(infile)

    vote_percentage = None

    for row in reader:
        party = row.get("Political Affiliation")
        ont_vote = row.get("Ont. Percentage of Valid Votes")

        if party == target_party:
            try:
                vote_percentage = float(ont_vote)
            except (TypeError, ValueError):
                vote_percentage = None
                print("Error: Could not assign value for variable: vote_percentage",file=sys.stderr)
            break #Breaks the loop once selected party found

    
    infile.close()

    return vote_percentage


##
## Mainline function
##
def main(argv):

    if len(argv) != 4:
        print("Usage: preprocess_election.py <datasets/2019_election.csv> <datasets/2021_election.csv> <party_name>", file=sys.stderr)
        sys.exit(1)

    election_2019 = argv[1]
    election_2021 = argv[2]
    target_party = argv[3]

    vote_2019 = extract_party_vote(election_2019, target_party)
    vote_2021 = extract_party_vote(election_2021, target_party)

    writer = csv.writer(sys.stdout)
    writer.writerow(["Year", "Party", "Ontario Vote Percentage"])

    if vote_2019 is not None:
        writer.writerow([2019, target_party, round(vote_2019, 2)])
        writer.writerow([2021, target_party, round(vote_2021, 2)])


##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

#!/usr/bin/env python

'''
preprocess_election.py
  Author(s): Hieu Hoang (1390265), 

  Module: Election Preprocessor 
  Date of Last Update: Mar 06, 2026.

  Functional Summary
    Reads 2019 and 2021 election Table 9 CSV files and outputs processed_votes_percentage.csv for question 1
	Usage:
        python3 preprocess_election.py <party_name> <datasets/2004_election.csv> <datasets/2006_election.csv> <datasets/2008_election.csv> <datasets/2011_election.csv> <datasets/2015_election.csv> <datasets/2019_election.csv> <datasets/2021_election.csv> <datasets/2025_election.csv> > processed_vote_percentages.csv
    Effect:
        Produce a CSV file containing the Ontario percentage of valid votes
        for the specified political for elections from 2004 to 2025.

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

        reader = csv.DictReader(infile)

        vote_percentage = None

        for row in reader:
            party = row.get("Political affiliation/Appartenance politique")
            ont_vote = row.get("Ont. Percentage of Valid Votes/Pourcentage des votes valides Ont.")

            if party is not None:
                party = party.strip()

            if party is not None and target_party in party:
                try:
                    vote_percentage = float(ont_vote)
                except (TypeError, ValueError):
                    vote_percentage = None
                    print("Error: Could not assign value for variable: vote_percentage",file=sys.stderr)
                break #Breaks the loop once selected party found

        infile.close()
        return vote_percentage

    except UnicodeDecodeError:
        pass


    try:
        infile = open(filename, newline = '', encoding="cp1252")

        reader = csv.DictReader(infile)

        vote_percentage = None

        for row in reader:
            party = row.get("Political affiliation/Appartenance politique")
            ont_vote = row.get("Ont. Percentage of Valid Votes/Pourcentage des votes valides Ont.")

            if party is not None:
                party = party.strip()

            if party is not None and target_party in party:
                try:
                    vote_percentage = float(ont_vote)
                except (TypeError, ValueError):
                    vote_percentage = None
                    print("Error: Could not assign value for variable: vote_percentage",file=sys.stderr)
                break #Breaks the loop once selected party found

        infile.close()
        return vote_percentage

    except IOError:
        print(f"Error: Could not open the the selected file {filename}.", file=sys.stderr)
        sys.exit(1)

    return None
    


##
## Mainline function
##
def main(argv):

    if len(argv) != 10:
        print("Usage: preprocess_election.py <party_name> <datasets/2004_election.csv> <datasets/2006_election.csv> <datasets/2008_election.csv> <datasets/2011_election.csv> <datasets/2015_election.csv> <datasets/2019_election.csv> <datasets/2021_election.csv> <datasets/2025_election.csv> > processed_vote_percentages.csv", file=sys.stderr)
        sys.exit(1)

    target_party = argv[1].strip() 

    election_files = [
        (2004, argv[2]),
        (2006, argv[3]),
        (2008, argv[4]),
        (2011, argv[5]),
        (2015, argv[6]),
        (2019, argv[7]),
        (2021, argv[8]),
        (2025, argv[9])
    ]

    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["Year", "Party", "Ontario Vote Percentage"])

    for year, filename in election_files:
        vote_percentage = extract_party_vote(filename, target_party)
        if vote_percentage is not None:
            writer.writerow([year, target_party, f"{vote_percentage:.2f}"])
        else:
            print(f"Error: Could not find {target_party} in {filename},", file=sys.stderr)
    

##
## Call our main function, passing the system argv as the parameter
##
if __name__ == "__main__": main(sys.argv)


#
#   End of Script
#

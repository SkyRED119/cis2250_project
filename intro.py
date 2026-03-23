"""
Authors: Andrea Bujold (1391778), Amir Kayumov (1386890)

This program will act as the introduction for the user. It will provide some context to both questions, 
what the program is and inquire about what question the user wants answerd. Once the user selects their choice, 
the program will then call the appropriate function to answer the question.
"""

import subprocess
import sys

def intro():
    print("Welcome to the Ontario Election and Inflation Analysis Program!\n\n______________________________________________________________________________________")
    print("This program will analyze the relationship between Ontario's inflation rates OR Ontario's age demographics, and the vote percentages of all the major political parties from the 38th to the 45th general elections. \n\n")
    print("Your choices for analysis are: \n 1. How does pre-election inflation in Ontario correlate with the change in the percentage of votes that a specific party receives? \n 2. How does the density of a specific age demographic in Ontario correlate with the percentage voter turnout?\n\n")
    choice = input("Please enter the number corresponding to the question you want answered (1 or 2): ")
    if choice == "1":
        party = input("Question 1 requires a parameter for the party whose vote percentages are meant to be analyzed.\nPlease selection your desire party: ")
        with open("processed_vote_percentages.csv", "w", newline="", encoding="utf-8-sig") as f:
            subprocess.run([sys.executable, "preprocess_election.py", f'{party}', "datasets/2004_election.csv", "datasets/2006_election.csv", "datasets/2008_election.csv", "datasets/2011_election.csv", "datasets/2015_election.csv", "datasets/2019_election.csv", "datasets/2021_election.csv", "datasets/2025_election.csv"], stdout=f, check=True)
        subprocess.run([sys.executable, "analyzer_q1.py", "processed_inflation.csv", "processed_vote_percentages.csv"], check=True)
    elif choice == "2":
        subprocess.run([sys.executable, "analyzer_q2.py", "processed_age_turnout.csv", "processed_vote_percentages.csv"], check=True)  
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__": 
    intro()
        
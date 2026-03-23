"""
Authors: Andrea Bujold (1391778), Amir Kayumov (1386890)

This program will act as the introduction for the user. It will provide some context to both questions, 
what the program is and inquire about what question the user wants answerd. Once the user selects their choice, 
the program will then call the appropriate function to answer the question.
"""

import subprocess
import sys

def intro():
    print("\nWelcome to the Ontario Election and Inflation Analysis Program!")
    print("This program analyzes the relationship between Ontario's inflation rates OR age demographics and vote percentages.\n")
    while True:
        print("______________________________________________________________________________________\n")
        print("Your choices for analysis are:")
        print(" 1. Inflation vs Vote Percentage")
        print(" 2. Age Demographics vs Voter Turnout")
        print(" 0. Exit\n")
        choice = input("Enter your choice (0, 1, or 2): ").strip()

        if choice == "0":
            print("Exiting program. Goodbye!")
            break

        elif choice == "1":
            while True:
                party = input("\nEnter the party name (or type 'back' to return): ").strip()
                
                if party.lower() == "back":
                    break

                if party == "":
                    print("Invalid input. Please enter a valid party name.")
                    continue

                try:
                    with open("processed_vote_percentages.csv", "w", newline="", encoding="utf-8-sig") as f:
                        subprocess.run([sys.executable, "preprocess_election.py", party, "datasets/2004_election.csv",
                            "datasets/2006_election.csv", "datasets/2008_election.csv", "datasets/2011_election.csv",
                            "datasets/2015_election.csv", "datasets/2019_election.csv", "datasets/2021_election.csv",
                            "datasets/2025_election.csv"], stdout=f, check=True)

                    subprocess.run([
                        sys.executable, "analyzer_q1.py",
                        "processed_inflation.csv",
                        "processed_vote_percentages.csv"
                    ], check=True)

                    break  # success → go back to main menu

                except subprocess.CalledProcessError:
                    print("Error occurred while running analysis. Please try again.")

        elif choice == "2":
            try:
                subprocess.run([sys.executable, "analyzer_q2.py", "processed_age_turnout.csv", "processed_vote_percentages.csv"], check=True)
            except subprocess.CalledProcessError:
                print("Error occurred while running analysis.")
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")

if __name__ == "__main__": 
    intro()
        
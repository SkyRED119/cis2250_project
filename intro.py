"""
Author: Andrea Bujold (1391778)

This program will act as the introduction for the user. It will provide some context to both questions, 
what the program is and inquire about what question the user wants answerd. Once the user selects their choice, 
the program will then call the appropriate function to answer the question.
"""

import subprocess

def intro():
    print("Welcome to the Ontario Election and Inflation Analysis Program! \n ___________________________________________________________")
    print("This program will analyze the relationship between Ontario's inflation rates and the vote percentages of all the major political parties in the 2004, 2006, 2008, 2011, 2015, 2019, 2021 and 2025 elections. \n")
    print("Your choices for analysis are: \n 1. How does pre-election inflation in Ontario correlate with the change in the number of votes that a specific party receives? \n 2. How does the density of a specific age demographic in Ontario correlate with the voter turnout (ie, the total number of votes cast)?")
    choice = input("Please enter the number corresponding to the question you want answered (1 or 2): ")
    if choice == "1":
        subprocess.run(["python3", "analyzer_q1.py", "datasets/cpi_table.csv"], check=True)
    elif choice == "2":
        subprocess.run(["python3", "analyzer_q2.py", "datasets/age_turnout_table.csv"], check=True)  
    else:
        print("Invalid choice. Please enter 1 or 2.")

    if __name__ == "__main__": 
        intro()
        
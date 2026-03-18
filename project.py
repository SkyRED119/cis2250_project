"""
Author: [Andrea Bujold]
ID: [1391778]
To do List steps to complete the project:(question 1)

Question to answer: How does pre-election inflation in Ontario correlate
with the change in the number of votes that a specific party receives? 

1. Collect data on pre-election inflation in Ontario for the past few elections.
2. Collect data on the number of votes received by the specific party in those elections.
3. Analyze the data to identify any correlations between pre-election inflation and the change in votes for the specific party.
4. Use statistical methods to determine the strength and significance of any correlations found.
5. Interpret the results and draw conclusions about the relationship between pre-election inflation and voting patterns for the specific party.

1. Use Python libraries such as pandas to organize and analyze the data.
2. Use visualization libraries such as matplotlib or seaborn to create graphs that illustrate the relationship between pre-election inflation and voting patterns.
3. Use statistical libraries such as scipy to perform correlation analysis and determine the significance of the findings. 
"""

"""
Initial Draft of Running Program:
- Inform the user about the purpose of the program and the question being investigated.
- Prompt user to specify the specific party they want to analyze.
- Only analyzing 43rd and 44th, so no need to prompt for election years.(will be hard coded in the program)
- Loads all datasets needed and only displays the specific party's data for the 43rd and 44th elections.
- Displays all inflation rates and the change in votes for the specific party for the 43rd and 44th elections.
- Displays a graph showing the relationship between pre-election inflation and the change in votes for the specific party.
- Provides an interpretation of the results and any conclusions drawn from the analysis.
"""


def question1():
    print("Welcome to the Ontario Pre-Election Inflation and Voting Analysis Program!")
    print("This program investigates the correlation between pre-election inflation in Ontario and the change in votes for a specific party.")
    party = input("Please enter the name of the specific party you want to analyze: ")
    # Load datasets and perform analysis (this is a placeholder, actual implementation will depend on the data format and structure)
    print(f"Analyzing data for {party} in the 43rd and 44th elections...")
    # Display results and graphs (this is a placeholder, actual implementation will depend on the analysis performed)
    print("Displaying results and graphs...")
    print("Interpretation of results and conclusions...")   

question1()

"""
To do List steps to complete the project:(question 2)

Question: How does the density of a specific age demographic in Ontario
correlate with the voter turnout (ie, the total number of votes cast)?

1. Collect data on the density of the specific age demographic in Ontario for the past few elections.
2. Collect data on the voter turnout for those elections.
3. Analyze the data to identify any correlations between the density of the specific age demographic and voter turnout.
4. Use statistical methods to determine the strength and significance of any correlations found.
5. Interpret the results and draw conclusions about the relationship between the density of the specific age demographic and voter turnout in Ontario.

1. Use Python libraries such as pandas to organize and analyze the data.
2. Use visualization libraries such as matplotlib or seaborn to create graphs that illustrate the relationship between the density of the specific age demographic and voter turnout.
3. Use statistical libraries such as scipy to perform correlation analysis and determine the significance of the findings.
"""

"""
Initial Draft of Running Program:
- Inform the user about the purpose of the program and the question being investigated.
- Prompt user to specify the specific age demographic they want to analyze.
- Only analyzing 43rd and 44th, so no need to prompt for election years.(will be hard coded in the program)
- Loads all datasets needed and only displays the specific age demographic's density and voter turnout data for the 43rd and 44th elections.
- Displays all density rates for the specific age demographic and the voter turnout for the 43rd and 44th elections.
- Displays a graph showing the relationship between the density of the specific age demographic and voter turnout.
- Provides an interpretation of the results and any conclusions drawn from the analysis.
"""

def question2():
    print("Welcome to the Ontario Age Demographic Density and Voter Turnout Analysis Program!")
    print("This program investigates the correlation between the density of a specific age demographic in Ontario and voter turnout.")
    age_demographic = input("Please enter the specific age demographic you want to analyze (e.g., 18-24, 25-34, etc.): ")
    # Load datasets and perform analysis (this is a placeholder, actual implementation will depend on the data format and structure)
    print(f"Analyzing data for the {age_demographic} age demographic in the 43rd and 44th elections...")
    # Display results and graphs (this is a placeholder, actual implementation will depend on the analysis performed)
    print("Displaying results and graphs...")
    print("Interpretation of results and conclusions...")

question2()
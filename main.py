# Tyler Beck
# CISP 300
# September 5, 2024

# This program calculates the average number of wins over the past five years for a football team.

# Ask for user input (number of wins for each year)
year1 = float(input("Enter number of wins for year 1: "))
year2 = float(input("Enter number of wins for year 2: "))
year3 = float(input("Enter number of wins for year 3: "))
year4 = float(input("Enter number of wins for year 4: "))
year5 = float(input("Enter number of wins for year 5: "))

# Calculate the average number of wins
yearlyAverage = (year1 + year2 + year3 + year4 + year5) / 5

# Display the calculated average number of wins
print("The average number of wins over the past five years is", yearlyAverage)

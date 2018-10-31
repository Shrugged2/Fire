# Start Fire insurance project
# Ctrl shift B to run in Atom
# Inputs here below
PropertyName = input("Property Name? ")
City = input("City: ")
print ("Ahhhh,", City, "the city of brotherly love.")
#sleep 3 seconds
import time
# time.sleep(3)
#delete this
print ("Just kidding. Philly is the city of brotherly love.", City, "is a shithole.")
# ZipCode = input("Zip Code: ")
Smoking = int(input("Smoking occurance: "))
YearBuilt = int(input("What year was the property built? "))
# Sprinklers = input("Sprinklers (Y/N)? ")
# Supression = input("Stove Suppression System (Y/N)?")
# Elctrical = input("Electrical? ")
# Construction = input("Construction: ")
# FireAlarm = input("Fire Alarm/ Smoke Detectors: ")
# PerCapitaIncome = input("PerCapita Income in 1 Mile Radius:")
# SquareFeet = int(input("Square Feet: "))
# AnnualRentIncome = int(input("Annual Rental Income: "))
# HabitationalStories = int(input("Habitational Stories: "))
# RentableSqFt = int(input("Average rentable sq ft per structure: "))
# MaxSqFtBetween = input("Max. sq. ft between structures")
# placeholder input because I'm sure I'll think of more
#  = input("")

# pulling current date for building age comparisons.
# "now.year, now.month, now.day, now.hour, now.minute, now.second" is format.
import datetime
now = datetime.datetime.now()

# output so I have something to show here
print ("Ahhhh yes, the", PropertyName, "Property. Circa", YearBuilt)
print ("That mothafucka is", now.year - YearBuilt, "years old")
# I know it's stupid but it's 4am
if YearBuilt > now.year:
    print ("burn it down")



import csv #bringing in CSV file from Will

with open("desktop/fireins/FireData1.csv") as Fire: #filepath unique to comp.
    reader = csv.DictReader(Fire)
    for row in reader:
        if Smoking > 69: #69 because its 5am now
            match = row["Construction Year"]
            #print(row["Property"], "is subject to termination.")

#more shit to do.
#store input on a longer basis.
#transform and modify info.
    #This is crap RN but I don't know how to assign significance inputs
#Not sure how to get this past spreadsheet level crap.
    # can give weights to inputs. Output a fancy number pretty easily
    # where to find smoking data?

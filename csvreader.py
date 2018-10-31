import csv

with open("C:\Users\RCWil\Desktop\Fireins\FireData1.csv") as Fire:
    reader = csv.DictReader(Fire)
    for row in reader:
        print(row["Property"], row["City"], row["Construction Year"])

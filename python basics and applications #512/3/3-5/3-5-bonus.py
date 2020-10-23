import csv

crimes = [row[5] for row in csv.reader(open("Crimes.csv"))]
print(max(set(crimes), key=lambda x: crimes.count(x)))
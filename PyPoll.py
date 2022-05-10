import datetime as dt
import csv

now = dt.datetime.now()
print("The time right now is ", now)

#writing into a csv file
with open("tryme.csv", "w") as fh:
    fh.write("Counties in the election\n---------------\nArapahoe\nDenver\nJefferson")

#reading from csv file to print out all the rows 
with open ("Resources/election_results.csv", "r") as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)



    


# Python Module 3 Challenge #

## Overview of Election Audit ##

After providing the Winning candidate name, votes and percentage. The Election commission wanted us to find out the following information for each county.
1) The voter turnout for each county.
2) The percentage of votes from each county out of the total count.
3) The county with the highest turnout.

## Election-Audit Results ##
- This congressional election had total of 369,711 votes.

![This is an image](https://github.com/dhwaniagrawal/Election-Analysis/blob/main/Total%20Votes.png)

- County Votes

![this is an image](https://github.com/dhwaniagrawal/Election-Analysis/blob/main/County%20Votes.png)

- Largest County Turnout

![this is an image](https://github.com/dhwaniagrawal/Election-Analysis/blob/main/Largest%20County%20Turnout.png)

- Candidate Votes

![this is an image](https://github.com/dhwaniagrawal/Election-Analysis/blob/main/Candidate%20Votes.png)

- Winner(Candidate)

![this is an image](https://github.com/dhwaniagrawal/Election-Analysis/blob/main/Winner(Candidate).png)

## Election-Audit Summary ##

In this election, csv file is in the format of "Ballot ID, County, Candidate". If the format remains the same but number of counties and/or candidate changes, even then there will be no modification in the code.

Example#1 - If the format of the csv file changes to "Candidate, County, Ballot ID" then the following lines will be modified:
- existing line of code - "candidate_name = row[2]"
- modified line of code - "candidate_name = row[0]"
  
Example#2 - If the format of the csv file changes to  "County, Ballot ID, Candidate" then the following lines will be modified:
- existing line of code - "county_name = row[1]"
- modified line of code - "county_name = row[0]"
  
Example#3 - If the format of the csv file changes to "Ballot ID, Candidate, County" then the following lines will be modified:
- existing line of code - "candidate_name = row[2]"
- existing line of code - "county_name = row[1]"
- modified line of code - "candidate_name = row[1]"
- modified line of code - "county_name = row[2]"

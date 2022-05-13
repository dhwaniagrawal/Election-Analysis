"""counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

grade =int(input("what is your grade?"))
if grade >= 90:
    print("Your grade is an A")
elif grade >= 80:
     print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
     print("Your grade is D")
else:
      print("Your grade is F")"""      



"""""
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("True")
else:
    print("False")     


counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties")
else:
    print("Arapahoe or El Paso are not in the list of counties")


x = 0
while x <= 5:
    print(x)
    x = x+1


for county in counties:
    print(county)

counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict.keys():
     print(county)
for voters in counties_dict.values():
     print(voters)    



counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(counties_dict[county])
     


counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for key,value in counties_dict.items():
    print(key,value)


counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for key,value in counties_dict.items():
    #print(f'{key} county has {value} registered voters.')
     print(key + " county has " + str(value)  + " registered voters")
"""
"""
name = 'Mosh'
message = f'Hi, my name is {name}'
print(message.find('m'))


mylist = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly" ]
mylist.remove('Peanut Butter') 
print(mylist)
mylist.insert(3,'Almond Butter')
print(mylist)
mylist.remove('Jelly')
print(mylist)
mylist.append('Coffee')
print(mylist)

pet_dict = {"name" : "Ruby",
            "age"  : 4,
            "hobbies" : ["sleeping","eating","barking"],
            "wakeup" : {"M" : "4:30", "T" : "8:30", "W" : "10:30"}
           }
print(f'My pets name is {pet_dict["name"]}')

name = "'Dhwani'"

print(f"My name is '{name}'")

"""
""""
names = ["Ruby","Viha","Shivam","Dhwani"]
user = input('Enter any name')
if user in names:
    print(f"Yes {user} matches")
else:
    print(f"no {user} does not match")
"""
"""
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

print(voting_data)

for county_dict in voting_data:
    print(county_dict)

    """
"""
counties_dict = {"Arapahoe":369237,"Denver":413229,"Jefferson":390222}
for county, voters in counties_dict.items():
  #  print(county + " county has " + str(voters) + " registered voters. ")
    print(f'{county} county has {voters} registered voters.')

    """
"""
counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
for county, registered_voters in counties_dict.items():
    print(f'{county} county has {registered_voters} registered voters')
"""
"""
from xml.dom.domreg import registered


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters":422829}, {"county":"Denver", "registered_voters":463353}, {"county":"Jefferson", "registered_voters":432438}]
for counties_dict in voting_data:
    print(f'{counties_dict["county"]} county has {counties_dict["registered_voters"]} registered voters.')
"""
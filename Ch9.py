#Chapter 9 - Working with If Statements:

#Example 1: Selective Conversion to Upper Case
countries = ["germany", "usa", "brazil", "uk", "argentina"]
for country in countries:
  if country == ("usa"):
    print(country.upper())
  elif country == ("uk"):
    print(country.upper())
  else:
    print(country.title())
#Germany
#USA
#Brazil
#UK
#Argentina
#An If If Else statement: prints USA, usa, brazil etc

#Example 2: Tracking a Criminal:
criminal_suspects = ["Bill", "Bull", "Billy"]
for criminal in criminal_suspects:
  if criminal_suspects == "Fred":
    print("Detain for further investigations.")
  else:
    print("Release from detention.")
#Prints "Release from detention x3"


#Example 3: Using the Inequality Sign:
for criminal in criminal_suspects:
  if criminal != "Fred":
    print("Release from detention immediately.")


#Example 4: Addressing Each Suspect by Name:
criminal_suspects = ["Bill", "Fred", "Billy"]
if criminal_suspects[0] == "Fred":
  print("Detain " + criminal_suspects[0] + " for further investigations.")
else:
  print("Release " + criminal_suspects[0] + " from detention.")
if criminal_suspects[1] == "Fred":
  print("Detain " + criminal_suspects[1] + " for further investigations.")
else:
  print("Release " + criminal_suspects[1] + " from detention.")
if criminal_suspects[2] == "Fred":
  print("Detain " + criminal_suspects[2] + " for further investigations.")
else:
  print("Release " + criminal_suspects[2] + " from detention.")
#Prints: Release Bill from detention. Detain Fred for further investigations.,Release Billy from detention.

#Example 5: Separate Camping Instructions to Males and Females:
gender = "male"
if gender is "male":
  print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
elif gender is "female":
  print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
elif gender is "child":
  print("Hello. One parent should accompany you to Block A.")

#prints out statement for "male".

#Example 6: Female Participant:
gender = "female"
if gender is "male":
  print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
elif gender is "female":
  print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
elif gender is "child":
  print("Hello. One parent should accompany you to Block A.")

#prints out statement for "female".


#Example 7: Child participant:
gender = "child"

if gender is "male":
  print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
elif gender is "female":
  print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
elif gender is "child":
  print("Hello. One parent should accompany you to Block A.")

#prints out statement for "child".

#Summary: Learned about conditional statements If/Elif/Else statements.
#Exercise 1: Design a traffic control system that moderates the kind of vehicles that are allowed to use a particular lane. Prepare a list of vehicles allowed to use the lane, and, using the If  statement, instruct Python to print a message that permits them to use the lane when they approach traffic control:

#List of vehicles allowed to use the lane:
permitted_vehicles = ["motorcycle", "car", "truck", "bus"]

# #Permit statement:
vehicle = "motorcycle"

for vehicle in permitted_vehicles:
  if vehicle is ("car"):
    print("Your vehicle is permitted to use the lane.")


#Exercise 2: Still on the traffic control system above, there are other kinds of vehicles that are not allowed to use this particular lane.  Using the != if if statement, print a message that forbids them from using the lane as they approach:

#updated permit statement:


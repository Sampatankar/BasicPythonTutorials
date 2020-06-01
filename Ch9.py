#Chapter 9 - Working with If Statements:

#Example 1: Selective Conversion to Upper Case
# countries = ["germany", "usa", "brazil", "uk", "argentina"]
# for country in countries:
#   if country == ("usa"):
#     print(country.upper())
#   elif country == ("uk"):
#     print(country.upper())
#   else:
#     print(country.title())
#Germany
#USA
#Brazil
#UK
#Argentina
#An If If Else statement: prints USA, usa, brazil etc

# #Example 2: Tracking a Criminal:
# criminal_suspects = ["Bill", "Bull", "Billy"]
# for criminal in criminal_suspects:
#   if criminal_suspects == "Fred":
#     print("Detain for further investigations.")
#   else:
#     print("Release from detention.")
# #Prints "Release from detention x3"


#Example 3: Using the Inequality Sign:
# for criminal in criminal_suspects:
#   if criminal != "Fred":
#     print("Release from detention immediately.")


#Example 4: Addressing Each Suspect by Name:
# criminal_suspects = ["Bill", "Fred", "Billy"]
# if criminal_suspects[0] == "Fred":
#   print("Detain " + criminal_suspects[0] + " for further investigations.")
# else:
#   print("Release " + criminal_suspects[0] + " from detention.")
# if criminal_suspects[1] == "Fred":
#   print("Detain " + criminal_suspects[1] + " for further investigations.")
# else:
#   print("Release " + criminal_suspects[1] + " from detention.")
# if criminal_suspects[2] == "Fred":
#   print("Detain " + criminal_suspects[2] + " for further investigations.")
# else:
#   print("Release " + criminal_suspects[2] + " from detention.")
#Prints: Release Bill from detention. Detain Fred for further investigations.,Release Billy from detention.

#Example 5: Separate Camping Instructions to Males and Females:
# gender = "male"
# if gender is "male":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
# elif gender is "female":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
# elif gender is "child":
#   print("Hello. One parent should accompany you to Block A.")

#prints out statement for "male".

# #Example 6: Female Participant:
# gender = "female"
# if gender is "male":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
# elif gender is "female":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
# elif gender is "child":
#   print("Hello. One parent should accompany you to Block A.")

#prints out statement for "female".


#Example 7: Child participant:
# gender = "child"

# if gender is "male":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block H.")
# elif gender is "female":
#   print("Hi. Welcome to our weekend picnic. Your room is in Block F.")
# elif gender is "child":
#   print("Hello. One parent should accompany you to Block A.")

#prints out statement for "child".

#Summary: Learned about conditional statements If/Elif/Else statements.
#Exercise 1: Design a traffic control system that moderates the kind of vehicles that are allowed to use a particular lane. Prepare a list of vehicles allowed to use the lane, and, using the If  statement, instruct Python to print a message that permits them to use the lane when they approach traffic control:

#List of vehicles allowed to use the lane:
# permitted_vehicles = ["motorcycle", "car", "truck", "bus"]

# #Permit statement:
#vehicle = "motorcycle"
# for vehicle in permitted_vehicles:
#   if vehicle == "other":
#     print("You are forbidden from using this lane.")
#   else:
#     print("You are permitted to use this lane.")


#Exercise 2: Still on the traffic control system above, there are other kinds of vehicles that are not allowed to use this particular lane.  Using the != if if statement, print a message that forbids them from using the lane as they approach:

#updated permit statement:
# for vehicle in permitted_vehicles:
#   if vehicle != "other":
#     print("You are permitted to use this lane.")
#   else:
#     print("You are forbidden from using this lane.")


#Exercise 3: You want to build an online game in which a person has only three shots before the game is up.  Using the if and elif statements, write a program that tells the player how many shots he has left after each shot is fired:
#shots_fired = [1, 2, 3]

# for shots in shots_fired:
#   if shots == 1:
#     print("You have two shots left.")
#   elif shots == 2:
#     print("You have one shot left.")
#   elif shots == 3:
#     print("You have NO shots left.")


#Exercise 4: In the game in ex.3, you want to disqualify any player that fires another shot even after being told at the end of his third shot that he has no more shots to fire:

# shots_fired = [1, 2, 3, 4]

# for shots in shots_fired:
#   if shots == 1:
#     print("You have two shots left.")
#   elif shots == 2:
#     print("You have one shot left.")
#   elif shots == 3:
#     print("You have NO shots left.")
#   elif shots > 3:
#     print("YOU ARE DISQUALIFIED!")


#Exercise 5: Perhaps you want to be more lenient to your players and decide to give them one last warning at their fourth shot before disqualifying them if they fire any other shots.  Using the if-elif-else statements write a program for this with the final warning after the fourth shot and a notice of disqualification following any other number of shots after the fourth:

shots_fired = [1, 2, 3, 4, 5]

for shots in shots_fired:
  if shots == 1:
    print("You have two shots left.")
  elif shots == 2:
    print("You have one shot left.")
  elif shots == 3:
    print("You have NO shots left.")
  elif shots == 4:
    print("WARNING! This shot does not count. Any further shots risk disqualification.")
  else:
    print("YOU ARE DISQUALIFIED!")

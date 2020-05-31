#Chapter 8 - Working with Loops:

#Example 1: Looping through a List:
countries = ["United States", "Great Britain", "Russia", "Japan", "South Korea", "Nigeria"]
for country in countries:
  print(country)
  #printed:
  #United States
  #Great Britain
  #Russia
  #Japan
  #South Korea
  #Nigeria

#Example 2: Automating Tasks with a Loop:
successful_students = ["Andy", "Tom", "Tony", "Susan", "Annie"]
for student in successful_students:
  print("Congratulations " + student + "! Welcome to Abraham Lincoln U'.")
  #cycles through each name and adds the greeting.
  #we can have multiple print statements under the for loop.

#Summary: Learned how to perform operations using a for loop, which enables Python to perform repetitive actions on all items on a list.
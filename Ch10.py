# Chapter 10: Operations Involving Dictionaries:

# In Python, a dictionary is a collection of well-arranged pieces of information. You may create a  dictionary in order to collate and store in one place, all the information relating to a particular person or subject:

# #Example 1: Building a Basic Dictionary:
immigrant_1 = {"age": "35", "gender": "Male", "nationality": "German",
               "religion": "Christian", "occupation": "Teacher"}
print(immigrant_1["gender"])
print(immigrant_1["nationality"])
print(immigrant_1["occupation"])


# Example 2: A Little 'Larger' Dictionary:
immigrant_1 = {"age": "35", "gender": "Male", "nationality": "German",
               "religion": "Christian"}
immigrant_2 = {"age": "40", "gender": "Female", "nationality": "Indian",
               "religion": "Buddhist"}
immigrant_3 = {"age": "43", "gender": "Male", "nationality": "American",
               "religion": "Christian"}
immigrant_4 = {"age": "54", "gender": "Female",
               "nationality": "Sudanese", "religion": "Muslim"}
immigrant_5 = {"age": "60", "gender": "Female", "nationality": "British",
               "religion": "Other"}

print(immigrant_1["nationality"])
print(immigrant_2["nationality"])
print(immigrant_3["nationality"])
print(immigrant_4["nationality"])
print(immigrant_5["nationality"])


# Example 3: Composing Messages with the Information in the Dictionary:
nationality_1 = immigrant_1["nationality"]
religion_1 = immigrant_1["religion"]
print("The first immigrant is a " + nationality_1 + " " + religion_1 + ".")

nationality_5 = immigrant_5["nationality"]
print("The first candidate for immigration is " + nationality_1 +
      ", while the fifth candidate for immigration is " + nationality_5 + ".")

# Example 4: Adding New Entries into a Dictionary:
print(immigrant_1)
immigrant_1["reason"] = "Political"
print(immigrant_1)

# Example 5: Building a Dictionary from Scratch:
student_1 = {}
student_2 = {}
student_3 = {}
student_1['English Language'] = 60
student_2['English Language'] = 54
student_3['English Language'] = 68
student_1['Comment'] = 'Good!'
student_2['Comment'] = 'Pass'
student_3['Comment'] = 'Very good!'
print(student_1)
print(student_2)
print(student_3)


# Example 6: Changing the Value of a Key in a Dictionary:
print(student_3)
student_3["English Language"] = 70
student_3["Comment"] = "Excellent"
print(student_3)


# Example 7: Removing a Key-Value Pair from a Dictionary:
print(immigrant_1)
del immigrant_1["religion"]
print(immigrant_1)

print(immigrant_2)
del immigrant_2["religion"]
print(immigrant_2)

print(immigrant_3)
del immigrant_3["religion"]
print(immigrant_3)

print(immigrant_4)
del immigrant_4["religion"]
print(immigrant_4)

print(immigrant_5)
del immigrant_5["religion"]
print(immigrant_5)


# Example 8: Building a Dictionary for only One Kind of Information:
feedback = {"Bill": "Fantastic", "Ciara": "Boring",
            "Fred": "Indifferent", "Mills": "Fair"}
print(feedback)


# Example 9: Using the For Loop in a Dictionary:
# Using a for loop to show everything held in the dictionary about one thing:
english_language = {
    'Fred': '60',
    'Annie': '56',
    'Andie': '50',
    'Ann': '45',
    'Clement': '65'
}
for student, score in english_language.items():
    print("\nStudent:" + student)
    print("Score: " + score)

# \n starts a new line, putting a space between the previous output and then this one.


# Example 10: Making the For loop through only keys:
print("These are the names of the students who sat for the exam: ")
for student in english_language.keys():
    print(student.title())


# Example 11:
english_language = {
    'Fred': '60',
    'Annie': '56',
    'Andie': '50',
    'Ann': '45',
    'Clement': '65'
}

complainants = ["Johnson", "Andie"]

for student in english_language.keys():
    print(student.title())

    if student in complainants:
        print('Dear ' + student.title() + ', we are sorry for not displaying your result earlier.' +
              ' Your score is ' + english_language[student] + '.')

if complainants != english_language:
    print('Sorry ' + complainants[0].title() +
          ', you did not sit the exam.  Therefore, you have no score.')


# Example 12: Printing Only the Values in the Dictionary:
# Use the values() method:
english_language = {
    'Fred': '60',
    'Annie': '56',
    'Andie': '50',
    'Ann': '45',
    'Clement': '65'
}
print('These are the scores made by the students: ')
for score in english_language.values():
    print(score)
# prints: 60 56 50 45 65


# Summary:
# Exercise 1: The prison service in your country is worried about it's reputation for poor record-keeping. It's inability to keep proper records has caused a lot of injustice to some of its inmates who end up spending more time in jail than is neccessary because no one remembers when their jail term expires. As part of its upgrade, it has hired you to help with organising the data of the inmates. Now with your knowledge of Python, create a simple dictionary for one inmate with the following keys: name, age, gender, crime, due for release and option of fine:

prisoner_1 = {"name": "Rob Burr", "age": "40", "gender": "male",
              "crime": "larceny", "DfR": "25/12/20", "Fine": "false"}


# Exercise 2: Now, while working on the same project, create the dictionary above for one more inmate. This time, print simple messages about their stay in jail, stating their crimes and dates of release.

prisoner_2 = {"name": "Ray Pist", "age": "57", "gender": "male",
              "crime": "frottage", "DfR": "05/08/47", "Fine": "false"}

pName = prisoner_1["name"] + " and " + prisoner_2["name"]
pCrime = prisoner_1["crime"] + " and " + prisoner_2["crime"]
pRelease = prisoner_1["DfR"] + " and " + prisoner_2["DfR"]

print("The prisoners, " + pName + ", are in prison for " + pCrime +
      " respectively. They are due for release on " + pRelease + " respectively.")


# Exercise 3: A Human rights group has sued the prison service on account of three of the prisoners (Murray, Tim and Frank) whom it claims have over-stayed their jail sentence.
# First, create two lists of prisoners, one for all those due for release, and the other for those already released.
# Using everything you have learned so far in Python, search the two lists. If you find any prisoner due for release but who has not been released yet, print a message of apology to them, stating that they will be released immediately.  However, if their sentences have not expired, print a different message to them, telling them their term is still running, and wishing them good luck the next time they check.


releasedPrisoners = {
    'Fred',
    'Annie',
    'Andie',
    'Ann',
    'Clement'
}

tBReleased = ['Murray', 'Tim', 'Frank', 'Fred', 'Annie', 'Ann']

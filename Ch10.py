#Chapter 10: Operations Involving Dictionaries:

#In Python, a dictionary is a collection of well-arranged pieces of information. You may create a  dictionary in order to collate and store in one place, all the information relating to a particular person or subject:

# #Example 1: Building a Basic Dictionary:
# immigrant_1 = {"age": "35", "gender":"Male", "nationality": "German", "religion": "Christian", "occupation": "Teacher"}
# print(immigrant_1["gender"])
# print(immigrant_1["nationality"])
# print(immigrant_1["occupation"])


#Example 2: A Little 'Larger' Dictionary:
immigrant_1 = {"age": "35", "gender": "Male", "nationality": "German",
               "religion": "Christian"}
immigrant_2 = {"age": "40", "gender": "Female", "nationality": "Indian",
               "religion": "Buddhist"}
immigrant_3 = {"age": "43", "gender": "Male", "nationality": "American",
               "religion": "Christian"}
immigrant_4 = {"age": "54", "gender": "Female", "nationality": "Sudanese", "religion": "Muslim"}
immigrant_5 = {"age": "60", "gender": "Female", "nationality": "British",
               "religion": "Other"}

print(immigrant_1["nationality"])
print(immigrant_2["nationality"])
print(immigrant_3["nationality"])
print(immigrant_4["nationality"])
print(immigrant_5["nationality"])


#Example 3: Composing Messages with the Information in the Dictionary:
nationality_1 = immigrant_1["nationality"]
religion_1 = immigrant_1["religion"]
print("The first immigrant is a " + nationality_1 + " " + religion_1 + ".")

nationality_5 = immigrant_5["nationality"]
print("The first candidate for immigration is " + nationality_1 + ", while the fifth candidate for immigration is " + nationality_5 + ".")

#Example 4: Adding New Entries into a Dictionary:

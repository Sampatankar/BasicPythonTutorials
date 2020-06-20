# Chapter 11: Nesting Dictionaries & Lists:

# Example 1: Nesting Dictionaries in a List:
student_1 = {'favourite': 'Mathematics', 'worst': 'English'}
student_2 = {'favourite': 'Arts', 'worst': 'Mathematics'}
student_3 = {'favourite': 'Religion', 'worst': 'Mathematics'}
student_4 = {'favourite': 'English', 'worst': 'Arts'}
student_5 = {'favourite': 'Agriculture', 'worst': 'Religion'}

students = [student_1, student_2, student_3, student_4, student_5]
for student in students:
    print(student)


# Example 2: Working with a Larger Number of Dictionaries:

# Creating a mother list to house the puppies:
puppies = []

# Making 100 new puppies:
for total_puppies in range(100):
    new_puppy = {'color': 'grey', 'speed': '10'}
    puppies.append(new_puppy)

# Let us show the first 5 puppies:
for puppy in puppies[:5]:
    print(puppy)
    print('...')

# Let us now show the total number of puppies created:
print("The complete number of puppies is " + str(len(puppies)))


# Example 3: Modifying the Dictionaries in a List:

# Creating a mother list to house the puppies:
puppies = []

# Making 100 new puppies:
for total_puppies in range(100):
    new_puppy = {'color': 'grey', 'speed': '10'}
    puppies.append(new_puppy)

for puppy in puppies[0:2]:
    if puppy['color'] == 'grey':
        puppy['color'] = 'black'
        puppy['speed'] = 12

# Let us show the first five puppies:
for puppy in puppies[:5]:
    print(puppy)
    print('...')

# Let us show the total number of puppies created:
print("The complete number of puppies is " + str(len(puppies)))


# Chapter summary:
# You have learned about what is called nesting in Python.  This involves putting dictionaries into lists and putting lists into dictionaries.  You have learned how to access the individual dictionaries that are nested in a list.

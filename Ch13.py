# Chapter 13 - Operations Using Defined Functions:

# Example 1:
def welcome_user():
    """Write a short welcome message."""
    print("Welcome, buddy!")


welcome_user()


# Example 2:
def welcome_user(username):
    """Write a short welcome message."""
    print("Welcome, " + username.title() + "!")


welcome_user("fred")


# Example 3:
def welcome_user(username):
    """Write a short welcome message."""
    print("Welcome, " + username.title() + "!")


welcome_user("fred")
welcome_user("Jessica")
welcome_user("fred")


# Example 4:
def describe_institution(institution_type, institution_name):
    print("My institution is a " + institution_type + ".")
    print("The name of my " + institution_type +
          " is " + institution_name.title() + ".")


describe_institution("school", "lincoln university")


def describe_institution(institution_type, institution_name):
    """Compose a short sentence about my institution."""
    print("My institution is a " + institution_type + ".")
    print("The name of my " + institution_type +
          " is " + institution_name.title() + ".")


describe_institution("lincoln university", "school")


# Example 5:
def describe_institution(institution_type, institution_name):
    """Compose a short sentence about my institution."""
    print("My institution is a " + institution_type + ".")
    print("The name of my " + institution_type +
          " is " + institution_name.title() + ".")


describe_institution(institution_name="lincoln university",
                     institution_type="school")


# Chapter Summary:
# In this chapter you have learned how to create or build new functions which enclose a body of codes for performing a particular task.  You have learned how to add parameters when defining a function and how to enter arguments when calling that function.  In addition, you have learned how to compose messages with the arguments in a function by simply calling that function.

# Exercises:
# 1. Define a simple function bye_bye, and use it to print a simple bye message.


# 2. Modify the function above to include a parameter, name, and enter the argument when calling the function to print the same bye message, this time mentiioning your friends name:


# 3. An elementary school in your town has hired you to build them a simple mobile app to help the pupils with reciting a poem. The poem is to accommodate in specific places, the name of the pupil, age of the pupil, the pupil's class, the name of the pupil's favourite teacher, and a line stating that the pupil is proud of the teacher. Define a function, pupils_identity, with the following paramters: pupil_name, pupils_age, pupils_class, and favourite_teacher.  Write the program to execute the following poem:
# My name is Jane.
# I am 8 years old.
# I am in Class 4.
# My favourite teacher is Ferguson.
# I am proud of him.


# 4. Call the function in the last exercise and enter the arguments for three pupils in order to print the poem the way each pupil would recite it:

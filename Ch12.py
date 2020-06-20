# Chapter 12 - Operations Involving User Input & While Loops:

# Example 1:
message = input("Please enter your name: ")
print("Dear " + message + ", we are glad to have you.")


# Example 2:
message = input("Age of tyre(months): ")
message = int(message)
if message >= 3:
    print("Your tyre is expired. Try and replace it.")


# Example 3:
message = input("Age of tyre(months): ")
message = int(message)
if message >= 3:
    print("Your tyre is expired. Try and replace it. ")
else:
    print("Congratulations! Your tyre has not expired. \nPlease, note that it expires after 3 months of use.")


# Example 4:
prompt = "\nThrow anything to me, and I throw it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(message)


# Chapter Summary:
# In this chapter, you learned the input and while functions, and how to use them in Python. You have seen how the input function allows Python to pause while executing a program in order to receive input from the user. You have also seen that with the while function, you can make Python continue to execute a repeated sequence of action while receiving input from the user.

# Exercises:

# 1. You are hired by a client in the hospitality industry to write a program that welcomes a guest to the hotel when they check into their rooms. The client wants you to make Python welcome these guests by their names. Using the input function, write a program that asks them for their names and then types a message for them when they enter their names.

message = input("Please enter your name: ")
print("Welcome " + message + ".  We hope you enjoy your stay at out hotel.")


# 2. You are the students' affairs officer of your institution, and the management of the institution has noticed that students are deceiving their parents and extorting money from them in the guise of purchasing some items from the school. You have decided to design an app that enables parents to secretly verify whether the school actually sells an item or gives it to students for free.


# 3. You are hired by the drugs regulatory agency in your country to design them an app that enables the general public to verify the actual expiry status of each medicine they buy. This has become necessary because dishonest medicine sellers have been erasing and extending the expiry date on the medicines in their store each time they expire. The drugs are to henceforth come labelled with unique codes which only get interpreted when tested in this app. Write a program in Python that asks users for the number on their medicines, cross-checks with the system, and returns a message about the status of the medicine.

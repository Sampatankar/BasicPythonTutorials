#Chapter 3: Strings & Methods


#CASE CHANGE:
#Example 1: Lower case to Title Case:
official = "high commissioner"

print(official.title()) #prints: High Commissioner

#Example 2: Title Case to Upper Case:
print(official.upper()) #prints: HIGH COMMISSIONER

#Example 3: Upper Case to Lower Case:
print(official.lower()) #prints: high commissioner


#CONCATENATION:
#Example 4: Joining a title and first name:
title = "Professor"
last_name = "McCaine"
salutation = title + " " + last_name
print(salutation)  #prints: "Professor McCaine"

#Example 5: Simple Salutation Message:
print("Good afternoon, " + salutation + ".") #prints: "Good afternoon, Professor McCaine"

#Example 6: Whole Message in a Variable:
greeting = "Good afternoon, " + salutation + "."
print(greeting) #prints: "Good afternoon, Professor McCaine"

#Summary Exercises:
#1.Create a string variable, name, and attach the value, catherine stone, to it.  Now, use the upper, title and lower methods to print it:
name = "Catherine Stone"
print(name.upper())
print(name.title())
print(name.lower())

#2.Create the following variables with their corresponding values:
first_name = "James"
last_name = "Bull"
full_name = first_name + " " + last_name + "."
print(full_name)

#3.Ask Python to display this message, "My most attractive high school friend was" with full_name:
print("My Most attractive high school friend was " + full_name)

#4.Repeat number 2 and 3 for three more of your high school classmates. When you print the message, it is going to help you appreciate that it is easier to make sentences using the names as coded than trying to remember every person's names:


#5.Create a new variable, message, which should contain the statement in 3 above. Now, ask Python to display it:
message = "My Most attractive high school friend was " + full_name
print(message)
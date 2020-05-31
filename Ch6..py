#Chapter 6 - Operations with Lists:

#A list is a group of items that are related by certain features.

classmates_names = ["Jane", "Francisca", "Ann", "Philips"]
print(classmates_names)

#Example 1: Displaying specific items on a List:
print(classmates_names[0]) #Jane

print(classmates_names[-1]) #Philips

#Wider applications of Items on a List:

classmates_names = ["Jane", "Francisca", "Ann", "Philips", "Andrew", "James", "Fred"]
print(classmates_names)

print("Congratulations " + classmates_names[0] + ". " + "You are top of the class.")


#Adjusting the Items on a List:
classmates_names[0] = "Philips"
classmates_names[3] = "Jane"
print(classmates_names)


#Example 3: Including New Items on a List (Using the Append method):
classmates_names = ["Jane", "Francisca", "Ann", "Philips", "Andrew", "James", "Fred"]
classmates_names.append("Chris")
classmates_names.append("Alex")
print(classmates_names)
#['Jane', 'Francisca', 'Ann', 'Philips', 'Andrew', 'James', 'Fred', 'Chris', 'Alex']

#using the insert() method:
classmates_names = ["Jane", "Francisca", "Ann",
                    "Philips", "Andrew", "James", "Fred"]
classmates_names.insert(5, "Tony")
print(classmates_names)
#Put Tony in the 6th position.


#Example 4: Removing Items from a List:
classmates_names = ["Jane", "Francisca", "Ann",
                    "Philips", "Andrew", "James", "Fred"]
del classmates_names[2]
print(classmates_names)
#Removed Ann from the list

#del removes an item permanantly. Using the pop() method allows you to remove an item for use in another list, or to compose a message.

#pop() method:
classmates_names = ["Jane", "Francisca", "Philips", "Andrew", "James", "Fred"]
print(classmates_names)
popped_names = classmates_names.pop()
print(classmates_names)  # ['Jane', 'Francisca', 'Philips', 'Andrew', 'James']
print(popped_names) #Fred

#popping in a different position:
classmates_names = ["Jane", "Francisca", "Philips", "Andrew", "James", "Fred"]
print(classmates_names)
popped_names = classmates_names.pop(1)
print(classmates_names)  # ['Jane', Philips', 'Andrew', 'James', 'Fred']
print(popped_names)  # Francisca

#don't know position BUT you know what you want to remove:
#remove() method:
classmates_names = ["Jane", "Francisca", "Philips", "Andrew", "James", "Fred"]
print(classmates_names)
classmates_names.remove("Philips")
print(classmates_names) #removes Philips

#Prisoners and Parole List:
Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Parole = Prisoners.pop(3)
print(Prisoners)
print(Parole)
Parole = Prisoners.pop(6)
print(Prisoners)
print(Parole)

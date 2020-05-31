#Chapter 7: Further Operations with Lists:

#Example 1: Sorting a list alphabetically:
countries = ["United States", "Great Britain", "Russia", "Japan", "South Korea", "Nigeria"]
print(countries)
countries.sort()
print(countries)

#reverse order:
countries.sort(reverse=True)
print(countries)

#temporary reverse order:
print(countries)
print(sorted(countries))
print(countries)

#Example 2: Reversing the list:
#Reverse() - just reverses the list, no order, alphabetical or otherwise:
print(countries)
countries.reverse()
print(countries)

#Example3: Length of a List:
print(len(countries))
#prints '6'

#Learned additional operations using lists, such as sorting a list, reversing a list and determining the length of a list.
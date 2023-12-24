# Lists are used to store multiple items in a single variabl
mylist = ["apple", "banana", "cherry"]

# append() - adds an element to the end
# pop(index) - removes the item by the index I passed
# extend(other list) - adds all elements in the list to the end
# sort() - sorts the list
# reverse() - reverse the list
# To determine how many items a list has, use the len() function:
# print(len(mylist))

# ==================
# Tuples are used to store multiple items in a single variable. (don't change)
mytuple = ("apple", "banana", "cherry")

# index(element) - returns the index of the element
# count(element) - returns the number of elements found

# ==================
# Sets are used to store multiple items in a single variable. (preserves unique elements) - does not keep order 
myset = {"apple", "banana", "cherry"}

# add(element)- adds an element to the end
# remove(element) - removes the item by the value I passed
# intersection(other set) - returns elements that intersect with the passed set
# symmetric_difference(other set) - returns elements that do not overlap with the passed set
# difference(other set) - returns values that are not in the transmitted set

# ==================
# Dictionaries are used to store data values in key:value pairs. - does not keep order 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# user["key"] = "value" - adds an element
# del user["value"] - removes the item by the value
# update(other dictionaries) - adds all dictionaries
# get(what search, what to return if this value is not present) - checks if the value is
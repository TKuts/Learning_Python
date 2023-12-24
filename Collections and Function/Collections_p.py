# ===== List =====
# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers)

# numbers.append(99)
# print(numbers)

# numbers.pop(0)
# print(numbers)

# other = [11, 12, 13]
# numbers.extend(other)
# print(numbers)

# numbers = [1, 4, 10,  2, 3, 55, 66, 5, 9]
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# ===== Tuple =====
# numbers = (1, 4, 10, 2, 3, 55, 66, 5, 9)
# print(numbers.index(2))
# print(numbers.count(2))

# ===== Sets =====
numbers1 = set([1, 2, 3, 4, 5])
numbers2 = {3, 4, 5, 6, 7, 8}

# print(numbers1)

# numbers1.add(11)
# print(numbers1)

# numbers1.remove(11)
# print(numbers1)

# intersection = numbers1.intersection(numbers2)
# print(intersection)

# symmetric_difference = numbers1.symmetric_difference(numbers2)
# print(symmetric_difference)

# difference = numbers1.difference(numbers2)
# print(difference)

# ===== Dictionaries =====
user = {"name" : "Anton", "age" : 26, "country" : "Ukraine"}
# print(user)

# user["key"] = "value"
# print(user)

# del user["age"]
# print(user)

# user_info = {"surname" : "Kuts", "gender" : "male"}

# user.update(user_info)
# print(user)

# print(user["age"])

age = user.get("age1", 0)
print(age)
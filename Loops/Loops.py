# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
students = ["Vlad", "Anton", "Ivan", "Dima"]

for student in students:
	print(f"Student: {student} is here!")

print("Done")


# With the while loop we can execute a set of statements as long as a condition is true.
t_borsh = 30

while t_borsh <= 99:
	print("It is necessary to mix")
	t_borsh += 1
	print(t_borsh)


print("Borsh is ready")
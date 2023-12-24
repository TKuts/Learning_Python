# Task #1
n = int(input("Enter number: "))

for i in range(1, n + 1):
	if i % 2 == 0:
		print(i)

print("Done")

# Task #2
result = 0
number_or_stop = input("Enter number or stop: ")

while number_or_stop != "stop":
	result += int(number_or_stop) 
	number_or_stop = input("Enter number or stop: ")

print(result)

# Task #3 (break)
students = ["Vlad", "Anton", "Dima", "Ivan", "Vasya", "Sergiy"]

for st in students:
	if st == "Dima":
		break
	else:
		print("This is't Dima!")
	
print("Done")

# Task #4 (continue)
students = ["Vlad", "Anton", "Dima", "Ivan", "Vasya", "Sergiy"]

for st in students:
	if st == "Dima":
		continue
	print(st)
	
print("Done")

# Task multiplication table
for i in range(1, 10):
	for add in range(1, 10):
		print(f"{i} * {add} = " + str(i * add))
	print("=====")
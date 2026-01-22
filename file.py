
name = "Ahmed"
age = 20
height = 1.75
is_student = True

print(type(name), type(age), type(height), type(is_student))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}, Diff: {num1 - num2}, Prod: {num1 * num2}, Div: {num1 / num2}")

x = int(input("Enter an integer: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")


secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the secret number: "))
print("Correct!")



nums = [10, 25, 5, 40, 15]
print(f"Sum: {sum(nums)}, Max: {max(nums)}")
nums.reverse()
print(f"Reversed list: {nums}")

cities = ("Cairo", "Alex", "Giza", "Aswan")
print(f"First: {cities[0]}, Last: {cities[-1]}")


group1 = {"Ahmed", "Sara", "Ali"}
group2 = {"Ali", "Mona", "Sara"}
both = group1.intersection(group2)
print(f"Students in both groups: {both}")


try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")



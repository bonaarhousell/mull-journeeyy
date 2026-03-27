number = [1, 2, 3, 4, 6, 8, 9, 10]

for num in number:
    if num % 2 == 0:
        print(num)

def add_number (num1, num2):
    return num1 + num2

result = add_number(5, 3)
print(result)

claude_test = int(input("Enter the number:"))
if claude_test > 0:
    print(f"{claude_test} is a positive number.")
elif claude_test < 0:
    print(f"{claude_test} is a negative number.")
else:    
    print("The number is zero.")

largest = None
for num in number:
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
print(f"The largest number is: {largest}")

scores = [85, 92, 78, 90, 88]
for avarage in scores:
    avarage = sum(scores) / len(scores)
if avarage > 85:
    total = len(scores)
    print(f"score yang di atas 85 adalah {total}")
print(f"The average score is: {avarage}")

x = 10 

def my_function():
    x = 5
    print (x)

my_function()

for i in range(5):
    print(i)

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        print("Not Weird")
    else:
        print("Weird")

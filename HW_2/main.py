#Task1

hello = "Hello World!"
print(hello)

#Task2

a = int(input("Введіть перше число "))
b = int(input("Введіть друге число "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Task3

string_1 = "help "
string_2 = "me"
string_sum = string_1 + string_2
print(string_sum)

#Task4

def is_even(num):
    if num%2 == 0:
        return "Парне"
    return "Непарне"
print(is_even(4))

#Task5

for i in range(10):
    print(i+1)

#Task6

def is_positive(num):
    if num < 0:
        return "Негативне"
    elif num > 0:
        return "Позитивне"
    return "Нуль"
print(is_positive(3))

#Task7

numbers = range(10)
for i in numbers:
    if ((i+1)%2) == 0:
        print(i+1)

#Task8

def sum_numbers(number):
    sum1 = 0
    for i in range(number+1):
        sum1 += i
    return sum1
print(sum_numbers(5))

#Task9

for i in range(10,0,-1):
    print(i)

#Task10

for i in range(10):
    if (i+1) == 5:
        continue
    elif (i+1) == 7:
        break
    print(i+1)
    
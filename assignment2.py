# #1. Find the largest of three numbers.
#  2. Find the smallest of three numbers.  
# 3. Read the list of fruits and perform the following:  If number of fruits are more than 4, add one more fruit and display 'EXCELLENT'. If banana is in list, change any one fruit and display 'GOOD'. If apple is in list, delete any one fruit and display 'AVERAGE' otherwise 'BAD' 
# 4. Read a variable, find whether it is number or string. If it is a string whether it is in upper case, lower case or something else. 
# 5. Find those numbers which are divisible by 9 and multiples of 5.
#  6. Display the multiplication table from 1 to n in the form 1*1 = 1 …… 
# 7. Display depending on the number of rows. 8. Read a list of numbers and display the even numbers and odd numbers separately. Sum the even numbers and odd numbers and display the same. 9. Read a list of numbers and display the numbers whose sum of individual digits is an even number.   10. Check whether an alphabet of a string inputted by the user is a vowel or consonant. 11. Check whether a string inputted by the user is representing an integer or not. 
# 12. Display  depending on the number of rows. 

#1.
# number1 = int(input("enter the 1st number"));
# number2 = int(input("enter the second number"));
# number3 = int(input("enter the third number"));
# if(number1 > number2):
#     if(number1 > number3):
#         print(number1, "is greater");
#     else:
#         print(number3, "is greater");
# else:
#     print(number2, "is greater");

#2.
# n1 = int(input("enter the 1st number"));
# n2 = int(input("enter the second number"));
# n3 = int(input("enter the third number"));
# if(n1 < n2):
#     if(n1 < n3):
#         print(n1, "is smaller");
#     else:
#         print(n3, "is smaller");
# else:
#     print(n2, "is smaller");

#3.
# fruits = (input('Enter fruits'));

# f1 = fruits.split(',')

# if len(f1) > 4:
#     f1.append('watermelon')
#     print('EXCELLENT')

# for i in f1:
#     if i == 'banana':
#         print('GOOD')
#         f1[0] = 'roseberry'
#     if i == 'apple':
#         print('AVERAGE')
#         del f1[0]
# else:
#     print('BAD')

#4.
# value = (input("enter something"));
# if(value.isalpha()):
#     if(value.isupper()):
#         print("it is in uppercase");
#     else:
#         print("it is lowercase");
# else:
#     print("it is a number");

#5.
# input = range(0, 100, 5);
# for i in input:
#     if(i % 9 == 0):
#         print(i);

#6.
# value = int(input("enter the range"));
# for i in range(1, value+1):
#     for j in range(1, 11, 1):
#         print(i,"x",j,"=",i*j)

#7.
# num = int(input('Enter a number:'))

# for i in range(0, num - 1):
#         for j in range(0,i+1):
#                 print('*', end = ' ')
#         print('\n')

# for k in range(num - 1, -1, -1):
#         for value in range(0, k+1):
#                 print('*', end = ' ')
#         print('\n')

#8.
# numbers = str(input('Enter numbers'))

# n1 = numbers.split(',')

# evenSum = 0
# oddSum = 0

# print('Even numbers are:')
# for i in n1:
#     if int(i) % 2 == 0:
#         print(i)
#         evenSum += int(i)
# print('even sum is:', evenSum)

# print('Odd numbers are:')
# for i in n1:
#     if int(i) % 2 != 0:
#         print(i)
#         oddSum += int(i)

# print('odd sum is:', oddSum)

# 9
# numbers = str(input('Enter numbers seperated by comma:'))

# n1 = numbers.split(',')

# for i in n1:
#     num = int(i)
#     total = 0
#     while num > 0:
#         digit = int(num) % 10
#         total = int(total) + int(digit)
#         num = int(num) / 10
#     if total % 2 == 0:
#         print(i)

#11
# value = input("enter something");
# if(value.isdigit()):
#     print(True);
# else:
#     print(False);

#10
# vowels = ['a', 'e', 'i', 'o', 'u'];
# input = input("enter the string");
# print(input[1]);
# for alphabet in vowels:
#     if(input[1] == alphabet):
#         print("the selected letter is vowel");
#     else:
#         print("the selected word is not vowel");

#12
# row = int(input("enter the number of rows"));
# for i in range(1, row):
#     print("*");
#     for j in range(1, i+1):
#         print("*", end = "");

#











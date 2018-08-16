# #3] question
# n = input("enter the number");
# n1 = n * 2;
# n2 = n * 3;
# total = int(n) + int(n1) + int(n2);
# print(total);# input:2, output:246

#4 swap the strings
# input = str(input("enter a string"));
# newstring = input[-1]+ input[1:len(input)-1]+input[0];
# print(newstring);

#13 calculate BMI
# import math
# height = int(input("enter the height"));
# weight = int(input("enter the weight"));
# bmi = weight/height;
# print(math.floor(bmi));

# #15 concatenate two tuples
# result = (1, 2, 3, 4);result1 = (5, 6, 7);
# # type(result));
# print(result + result1);

# # 16-create tuple of two tuples
# tuple1 = tuple(input("enter the 1 tuple"));
# print(tuple1);
# tuple2 = tuple(input("enter the second tuple"));
# print(tuple2);
# tuple3 = [tuple1, tuple2];
# print(tuple3);

# #7-calculate radius and circumference of the circle
# import math
# radius = int(input("enter the radius"));
# area = (math.pi * (radius * radius));
# circumference = 2 * math.pi * radius;
# print("Area:", area, "circumference:",circumference);

# #11 caclculate the area of the triangle
# base = int(input("enter the base"));
# height = int(input("enter the height"));
# area = 0.5 * base * height;
# print(area);

#12 calculate the simple interest with given principle, time, rate
# principle = int(input("enter the principle"));
# time = int(input("enter the time"));
# rate = int(input("enter the rate"));
# si = (principle*time*rate)/100;
# print(si);

#14- sort the three integers without using conditions
# numbers = [21, 20, 1];
# numbers.sort();
# print(numbers);

#9 - seperate the filename and their extensions
# import os
# file = str(input("enter the filename"));
# name, extension = os.path.splitext(file);
# print("fileName:", name, "Extension:", extension);

# 2 -simple calculator
# n1 = int(input("enter the number"));
# n2 = int(input("enter the second number"));
# add = n1 + n2;
# subtract = n1 - n2;
# divide = n1 /n2;
# multiply = n1 * n2;
# print("addition", add, "subtraction", subtract, "divide", divide, "multiply", multiply);

#6-union, intersection, difference
# set1 = set(input("enter the set"));
# set2 = set(input("enter the 2nd set"));
# print(set1.union(set2));
# print(set1.difference(set2));
# print(set1.intersection(set2));
# print(set1.symmetric_difference(set2));

#1.Anagrams
# str1 = str(input("enter the string"));
# str2 = str(input("enter the second string"));
# string1 = sorted(str1);
# string2 = sorted(str2);
# print(string1 == string2);

#5.remove spaces from string
# str1 = str(input("enter the string"));
# print(str1.replace(" ", ""));

# 17
# str1 = str(input("enter first strings"));
# str2 = str(input("enter second string"));
# str3 = str1[1]+str1[0]+str1[2:] + ' '+ str2[1]+str2[0] + str2[2:];
# print(str3);

#18
str1 = str(input("enter the string"));
str2 = str1.replace(str1[1], str1[len(str1)-2]);
str2[1] = str1[1];
print(str2);
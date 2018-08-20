# number = int(input("enter the number"));
# if(number > 0):
#     print("it is positive");
# elif(number < 0):
#     print("it is negative");
# else:
#     print("it is zero");

#accept anumber and check if number is multiple of 3if it is 6,if it is 9
# number = int(input("enter the number"));
# if(number % 3 == 0):
#     if(number % 6 == 0):
#         if(number % 9 == 0):
#             print(number, "will be divided from 3, 6, 9");
# else:
#     print(number, "is not dvisible by 3");

#write a python program to check whether the given year is leap year or not
 
# year = int(input("enter the year"));
# if(year % 4 == 0):
#     if(year % 100 != 0):
#         print(year, "is a leap year");
#     else:
#         print(year, "is not a leap year");
# else:
#     print(year, "Dear, is not at all a leap year");

num = int(input("enter the number"));
sum = 0;i=1;
while(i <= num):
    sum = sum + i;
    i = i+1;
else:
    print("you are out of the loop");
print(sum);
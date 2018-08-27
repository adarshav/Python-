# def printMe(str):
#     str = input("enter the string");
#     print("you have entered is", str);
#     return 

# printMe(str);

# def sum(a, b):
#     add = a + b;
#     # print("the sum of", a, "and ", b, "is", add);
#     return add;

# a = int(input("enter the number"));
# b = int(input("enter the number"));
# print(sum(a,b));

# def default(a = 10, b = 5):
#     add = a + b;
#     return add;
# a = int(input("enter the number"));
# print("the sum is", default(a));# in function while passing default parameters we have to call only one variable which is not defined, if we pass the variable which is not declared,output will be thrown as error

# def display(list1):
#     for i in list1:
#         print(i, end = " ");
#     return;
# list1 = [12, 3, 4,5];
# display(list1);

# def changeMe(myList):
#     myList.append([1, 2, 3, 4]);//append always takes one argument
#     print(myList);
# myList = [10, 20, 30];
# print(changeMe(myList));

# def oddEven(list1):
#     sum =0;
#     for i in list1:
#         if(int(i) % 2 == 0):
#             evenList.append(i);
#         else:
#             sum = sum + int(i);
#     return evenList, sum;
# # list1 = (input("enter the numbers"));
# list1 = list(list1.split(","));
# evenList = [];oddList = [];
# print(oddEven(list1));

# def printInfo(name, age):
#     print("Name:", name);
#     print("Age:", age);
#     return;
# printInfo(age = 23, name = "Isha");
# printInfo(23, "isha");
# printInfo("isha");#it prints error

# def printinfo(arg1, *varag):
#     print(arg1);
#     for v in varag:
#         print(v);
#     return None;
# printinfo(10, 20);
# printinfo(10,20,30,40);
# # printinfo();



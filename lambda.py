# double = lambda x: x*x*2

# print(double(5));

# add = lambda x, y: x+y

# print(add(3, 4));

# mul = lambda x, y, z: x*y*z;

# print(mul(2, 3, 4));

# #map 
# list1 =[1, 2,3];

# newList = list(map(lambda x: x*2, list1));

# print(newList);

# newList = [];
# def even(list1):
#     for i in list1:
#         if(i % 2 == 0):
#             newList.append(i);
#     return newList;

# print(even([12, 3, 4, 5, 8]));

# def even(list1):
#     newList = list(filter(lambda x: (x % 2 == 0), list1));
#     return newList;

# print(even([12, 3, 4 ,5 ,8]));\

# def divisible(list1):
#     newList = list(filter(lambda x: (x % 5 == 0), list1));
#     return newList;

# print(divisible([12, 2, 5, 30]));

#one method of find the vowels using filter method
# myList = ['a', 'b', 'n', 'e'];
# newList = list(filter(lambda x: x in 'aeiou', myList));
# print(newList);

from functools import reduce
# mylist = [12, 3, 4,5,6];
# newList = reduce(lambda x, newList: x+newList, mylist);
# print(newList);
# newlist = reduce(lambda x, y:x*y, mylist);
# print(newlist);

# syntax for list comprehension
# [expression for item in list if conditional]
# myList = [12, 3, 4, 5];
# squared = [l1 *l1 for l1 in myList if(l1 % 2 == 0)];
# print(squared);

# myList = [12, 3, 4, 5];
# multiply = [l1 +2 for l1 in myList if(l1 % 3 == 0)];
# print(multiply);

# create a list of lowercase characters given a list of uppercase characters
# myList = 'ADAr';
# lower = [s1.lower() for s1 in myList if(s1.isupper())];
# print(lower);

# newList = [i*i for i in range(1,9) if(5>i*i<50)];
# print(newList);

# mat = [(x, y) for x in range(5) for y in range(5)];
# print(mat);

m = [[1,2],[3,4],[5,6]]
for item in m :
    print(item)
rez = [[m[rows][cols] for rows in range(len(m))] for cols in range(len(m[0]))]
print("\n")
for item in rez:
    print(item)

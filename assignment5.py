#1.print the square root of number
# x = lambda a:a*a;
# print(x(6));

#2.solve the expression x+y*z/p
# x = lambda a, b, c, p : a+b*c/p;
# print((x(1, 2, 3, 12))); 

#3.from a given list filter out only numbers that are divisible by 3
# mylist = [12, 3, 4, 5, 7];
# divisible = list(filter(lambda x: x %3==0, mylist));
# print(divisible);

#4. remove the empty elements of a iterable
# mylist = [1, 3,"", 4];
# show = [x for x in mylist if x];
# print(show);

#5.find only names that start with 'j'
# mylist = ['adarsha', 'jarvis', 'jaari', 'shantha'];
# show = [name for name in mylist if(name[0] in 'j')];
# print(show);

#6.compute the product of list integers
from functools import reduce
# mylist = [1, 2, 3, 4];
# show = reduce(lambda x, y: x*y, mylist);
# print(show);

# 7.filter out the vowels in the list
# names = ['a', 'b', 'e', 'n'];
# show = [name for name in names if(name in 'aeiou')];
# print(show);


#1.remove vowels from sentence
# mylist = ['a', 'e', 'b', 'n'];
# show = [name for name in mylist if(name in 'aeiou')];
# print(show);
# for i in mylist:
#     result = list(filter(lambda x: del mylist[x], show));
# print(show);

#3.change to uppercase in list
# names =['adarsha', 'shantha', 'ganesha'];
# show = [name.upper() for name in names];
# print(show);
    
# 4.change to lowercase in list
# names =['ADarsha', 'Shantha', 'Ganesha'];
# show = [name.lower() for name in names];
# print(show);

#7.print the each word in a list
# words = ['asdf', 'das', 'sad'];
# result = [len(word) for word in words];
# print(result);

#8 print the first and last letter of every name in the list
# names = ['ada', 'deep'];
# result = [name[0]  name[-1] for name in names];
# print(result);

#11. create a list of squares  of the integers  from 0 to 9 where integer is greater than 5 and lesser than 50
# result = [l*l for l in range(0,9) if(5 <(l*l) <50)];
# print(result);

#9.print the reverse of each name in the list
# mylist = ['shantha', 'deepika'];
# result = [name[::-1] for name in mylist];
# print(result);

#10
# juice = ['water', 'tea', 'coffee'];
# food = ['icecream', 'chocolates', 'strawberry'];
# add = [];
# for j in juice:
#     for f in food:
#         add.append(j+' ' +'and' + ' ' +f);
    
# print(add);


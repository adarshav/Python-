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

# pass a string to a genarator and display reverse its content
def mygen(name):
    # n=len(name)
    n=1
    name[n]
    
    yield name[n]
    n+=1
    return
    

a="sathish"
for i in mygen(a):
    print(i)

# write a genarator to print fibinochi
# def fibo(n):
#     x=0;
#     y=1;
#     print(x);
#     print(y);
#     for i in range(n-2):
#         temp=x+y;
#         x=y;
#         y=temp;
#         yield temp;
#     return;

# for i in fibo(10):
#     print(i);


# write a program to search for alphanumaric values in string print its starting position
# str="1Today date is 29"
# for i in range(0,len(str)):
#     try:
#         x=int(str[i])
#         print(x,"in position of",i+1)
#         break
#     except:
#         print(str[i],"is not a number")
#         break
    
    
# regular expression


# ^
# Matches beginning of line.

# $
# Matches end of line.

# .
# Matches any single character except newline. Using m option allows it to match newline as well.

# [...]
# Matches any single character in brackets.

# [^...]
# Matches any single character not in brackets

# re*
# Matches 0 or more occurrences of preceding expression.

# re+
# Matches 1 or more occurrence of preceding expression.

# re?
# Matches 0 or 1 occurrence of preceding expression.

# re{ n}
# Matches exactly n number of occurrences of preceding expression.

# re{ n,}
# Matches n or more occurrences of preceding expression.

# re{ n, m}
# Matches at least n and at most m occurrences of preceding expression.

# a| b
# Matches either a or b.

# (re)
# Groups regular expressions and remembers matched text.

# (?imx)
# Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.

# (?-imx)
# Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.

# (?: re)
# Groups regular expressions without remembering matched text.

# (?imx: re)
# Temporarily toggles on i, m, or x options within parentheses.

# (?-imx: re)
# Temporarily toggles off i, m, or x options within parentheses.

# (?#...)
# Comment.

# (?= re)
# Specifies position using a pattern. Doesn't have a range.

# (?! re)
# Specifies position using pattern negation. Doesn't have a range.

# (?> re)
# Matches independent pattern without backtracking.

# \w
# Matches word characters.

# \W
# Matches nonword characters.

# \s
# Matches whitespace. Equivalent to [\t\n\r\f].

# \S
# Matches nonwhitespace.

# \d
# Matches digits. Equivalent to [0-9].

# \D
# Matches nondigits.

# \A
# Matches beginning of string.

# \Z
# Matches end of string. If a newline exists, it matches just before newline.

# \z
# Matches end of string.

# \G
# Matches point where last match finished.

# \b
# Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.

# \B
# Matches nonword boundaries.

# \n, \t, etc.
# Matches newlines, carriage returns, tabs, etc.

# \1...\9
# Matches nth grouped subexpression.

# \10
# Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.


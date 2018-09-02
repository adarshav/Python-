#1. Find the maximum of three numbers.
# def max(a, b, c):
#     if(a > b):
#         if(a > c):
#             return a;
#     elif(b > c):
#         return b;
#     else:
#         return c;

# print(max(3,9, 5));

# 2. Find the sum of the numbers in a list.
# def sum(list1):
#     sum = 0;
#     for i in list1:
#         sum = sum + i;
#     return sum;

# print(sum([10, 1, 3]));

#3. Reverse a string without using built-in function.
def rev(str1):
	str2=""
	for i in range(len(str1)-1,-1,-1):
		str2+=str1[i];
	print(str2)

str1=input("Enter a string")
rev(str1);

4
def fre(str1):
	di={}
	for i in str1:
		if i in di:
			di[i]+=1
		else:
			di[i]=1
	return di


string1=input("enter a string")
fli=fre(string1)
print(fli)

5
def pal(data1):
	data2=""
	for i in range(len(data1)-1,-1,-1):
		data2+=data1[i];
	return data2
data1=input("Enter a number")
data2=pal(data1)
if(data1==data2):
	print(data1,"is a palindrome")
else:
	print(data2,"is not a palindrome")

6
def occ(list1,string1):
	for i in string1:
		if i in list1:
			list1.remove(i)
	return list1


initlist=['a','b','c','d','e','f','g','h']
string1=input("enter a string")
finallist=occ(initlist,string1)
if len(finallist)==0:
	print("String contains all characters")
else:
	print("String contains all characters except",finallist)

7
def computeGCD(x, y):
	try:
	    if x > y:
	        small = y
	    else:
	        small = x
	    for i in range(1, small+1):
	        if((x % i == 0) and (y % i == 0)):
	            gcd = i             
	    return gcd
	except:
		pass
 
x=int(input("Enter a number "))
y=int(input("Enter another number"))
if(x<1 or y<1):
	print("Please enter the number")
else:
	gcd=computeGCD(x,y)
	print("GCD of",x," and ",y," is ",gcd)

8
def sum(num):
	if num==1:
		return 1
	else:
		return num+sum(num-1)

x=int(input("enter a number"))
val=sum(x)
print(val)

9
def decimalToBinary(n):
	try:
		if n > 1:
			decimalToBinary(n//2) 
		print (n%2,end=" ")			 
	except:
		pass

num=int(input("Enter a number"))
decimalToBinary(num)

10
print("Please select operation -\n 1. Add 2. Subtract 3. Multiply 4. Divide")
option= input("Select operations form 1, 2, 3, 4 :")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
 
if option == '1':
    print(num1, "+", num2, "=",num1+num2)
 
elif option == '2':
    print(num1, "-", num2, "=",num1-num2)
 
elif option == '3':
    print(num1, "*", num2, "=",num1*num2)
 
elif option == '4':
    print(num1, "/", num2, "=",num1/num2)
else:
    print("Invalid input")


11
def dev(n):
	ls=[]
	for i in range(2,n+1):
		if(n%i==0):
			ls.append(i)
	print("possible devisors are",ls)
	sum(ls)

def sum(ls):
	count=0
	sum=0
	for i in ls:
		count+=1
		sum+=i
	print("sum of all devisors are",sum,"count of all devisors are",count)

x=int(input("Enter a number"))
dev(x)



12
ls=[]
str1=" "
while str1!="":
	str1=input("Enter a string")
	if(str1!=""):
		ls.append(str1)

for i in ls:
	print("length of",i,"is",len(i))




13
def pascal(n):
    result = []
    for row in range(n):
        newrow = [1]
        for col in range(1, row+1):
            newcell = newrow[col-1] * float(row+1-col)/col
            newrow.append(int(newcell))
        result.append(newrow)
    return result
x=pascal(5)
for i in x:
	print(i)

14
def prime(lower,upper):
	for num in range(lower,upper + 1):
	   	if num > 1:
	   		flag=1;
	   		for i in range(2,num):
	   			if (num % i) == 0:
	   				flag=0
	   				break
	   		if(flag==1):
	   			print(num,end=" ")

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
prime(lower,upper)

15
def sum(list1,list2):
	sum=[]
	for i in range(1,(n*n)+1):
		sum.append(list1[i]+list2[i])
	return sum

def diff(list1,list2):
	diff=[]
	for i in range(1,(n*n)+1):
		diff.append(list1[i]-list2[i])
	return diff
list1=list2=[]
n=int(input("enter the total no of col"))
print("Enter the first matrix")
for i in range(1,(n*n)+1):
	data=int(input("Enter number"))
	list1.append(data)
print("Enter the second matrix")
for i in range(1,(n*n)+1):
	data=int(input("Enter number"))
	list2.append(data)

sum=sum(list1,list2)
diff=diff(list1,list2)
print("Sum= ")
count=0
for i in range(0,len(sum)):
	print(sum[i],end=" ")
	count+=1
	if(count>=n):
		print()
		count=0
print("Diff= ")
count=0
for i in range(0,len(sum)):
	print(diff[i],end=" ")
	count+=1
	if(count>=n):
		print()
		count=0
		
		




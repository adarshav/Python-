

#1.a
# for i in range(1, 9):
#     print(i);
#     for j in range(1, i+1):
#         print(i+1, end = "");

#b.
# row = int(input("enter the no of rows"));
# for i in range(1, row):
#     print("{0:>16s}".format("*"));
#     for j in range(1, i+1):
#         print({:20s}, format("*"));

#d.
# row = int(input("enter the number of rows"));
# for i in range(1, row, 1):
#     print(i, end = " ");

#g.
# list1 = ['A', 'B', 'C', 'D', 'E'];
# for j in range(0, len(list1)):
#     for i in range(1, j+2):
#         print(list1[j], end="");
#     print();

#k.
# row = int(input("enter the number of rows"));
# for i in range(1, row):
#     #print(i);
#     for j in range(i, 0, -1):
#         print(j, end = " ");
#     print();

#s.
# row = int(input("enter the no of rows"));
# for i in range(row, 0, -1):
#     str1 = "";
#     for j in range(i,0, -1):
#         str1 = str1 + " "+ str(j);
#     print("{:^10s}".format(str1), end = "");
#     print();

#r.
# row = int(input("enter the no of rows"));
# for i in range(row, 0, -1):
#     str1 = "";
#     for j in range(row,row-i, -1):
#         str1 = str1 + " "+ str(j);
#     print("{:^10s}".format(str1), end = "");
#     print();

#.i.
# n=int(input("Enter a total number of rows"))
# for i in range(1,n+1):
# 	for x in range(n,n-i,-1):
# 		print(x,end="")
# 	print()

#o.
# n=int(input("Enter a total number of rows"))
# for i in range(1,n+1):
# 	str1=str(i)
# 	str1=str1*i
# 	print("{:>30s}".format(str1),end="\n")
# print();

#j.
n=int(input("Enter a total number of rows"))
for i in range(n,0,-1):
	str="* "
	str=str*i;
	print(""+"{:^30s}".format(str),end="")
	print()





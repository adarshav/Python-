#In python (') singleQuotes ("")doubleQuotes and (''' or """) tripleQuotes are used to denote the string literals to span the string across the multiple lines
# variables are reserved memory locations to store values
word = "adarsha";word1 = '''triple quotes are used to denotethe string literal that it can be used
 in multiple lines'''
# In python explicit declaration of variables is not needed, the declaration happens automaticallywhen we assign the value to the variable  
print(word);
print(type(word)) # <class 'str'> this is what returned
print(word1);
#In python (#) hashtag is used for commenting lines
a, b, c = 1, 2, '3';
print('----------------------------------------');
print(a, b, type(c));# type is used to know typeOf variable;'print' is used to print the output
string = 'adarsha';number = 9663304987;# multi variables can be assigned in a single line with semicolan as statement terminator
#print(number);
del number; # 'del' keyword is used to delete the variable, multiple variables can be deleted with same method

#string datatype 
string = "iam god, god is great";
#subsets of strings can be taken using slice operator [] or [:];
print(string);
print(string[1]); # prints the second character in the string
print(string[2:7]);# prnts character starting from 3rd to 7th
print(string[-1]);# if negative number is given it starts from end
print(string[-1: -5]);# doubt to be asked
print(string[2:]); # prints the string starting from 3rd character
print(string * 2);# asterisk acts as a repetition operator
print(string + "Adarsha");# prints the concatenated string

#Lists- In python lists are the most versatile, lists are seperated by commas and enclosed in square brackets[]
listType = [1, 2, 3, 4, 5, 6];
print(type(listType));#returns <class 'list'>
list1 = ['adarsha', 123, 'qwerty'];
print(list1[1]);#slice operator can be used on any datatype
print(listType[1:4]);#[2, 3, 4]
print(list1 * 2);#(*)asterisk acts as a repetitional operator
print(list1[-1]);
list1[2] = 'python';#values in the list can be updated
print(list1);

#tuple
tuple1 = (1, 'radha', 'kaveri');
print(type(tuple1));# returns<class 'tuple'>
#slice operator can also be used on tuples
#values in the tuple cannot be updated

#Dictionary type
#Dictionary type is similar of Objects in javascript which has a key:value pair,it is enclosed in ({})flower brackets
dict1 = {"name":"Adarsha", "age":21, "education":"MCA", "college":"PESU"};
print(dict1);
print(dict1["name"]);#dictionary type is enclosed in flower brackets and it can be accessed using square brackets
print("Iam", dict1["name"], "and of", dict1["age"],"age", "completed my education from", dict1["college"]);
dict2 = {"name":"virat", "age":31, "strikeRate":154.5};
print("His name is", dict2["name"], "he is of", dict2["age"], "has a strikeRate of", dict2["strikeRate"]);
print(int(34.5));
print(float(43));
print(str(123));
print(complex(39.43));
print(tuple("234"));
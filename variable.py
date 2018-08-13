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
#


# Functions assignment

string = input("Enter the string: ")
dictionary = {}

def most_frequent():
    for keys in string:
        dictionary[keys] = dictionary.get(keys,0)+1
        
most_frequent()
print(dictionary)
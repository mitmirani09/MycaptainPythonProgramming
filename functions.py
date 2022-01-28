# Functions assignment

string = input("Enter the string: ")
dictionary = {}

def most_frequent():
    for keys in string:
        dictionary[keys] = dictionary.get(keys,0)+1
        
most_frequent()
sorted_dict = sorted(dictionary,key=dictionary.get,reverse=True)

for r in sorted_dict:
    print(r,"-",dictionary[r])
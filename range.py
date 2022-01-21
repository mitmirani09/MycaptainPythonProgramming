#assignment of loops
#To print positive numbers in range

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for number in range(start, end+1):
    if number >= 0:
        print(number)
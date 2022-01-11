# Area of circle and file extension program 

# Taking input of file name 

file_name = input("Enter the Filename: ")
f_extns = file_name.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))


#Taking input of radius of circle
import math

r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r

print("Area of the circle is :",area)
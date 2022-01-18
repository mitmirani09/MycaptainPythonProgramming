# Area of circle and file extension program 

# Taking input of file name 
#file extension program
file_name = input("Enter the Filename: ")
f_extns = file_name.split(".")
print ("The extension of the file is : ",f_extns[-1])
#----------------------------------------------------------
# Area of circle program 

#Taking input of radius of circle
import math

r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r

print("Area of the circle with radius",r, "is:",area)
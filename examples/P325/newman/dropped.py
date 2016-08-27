#Comments in Python begin with a # and extend to the length of the line
#Multiline comments are possible, delimited by triple quotes """

"""These two inputs show a key feature of Python - dynamic typing
wherein the variable type is determined at run time"""
h = float(input("Enter the height of the tower in meters: "))
t = float(input("Enter the time interval in sec.: "))

s = 9.81*t**2/2

#calculate the height.  Multiplication uses * and raising to a power **
print("At t = ",t," The height of the ball is",h-s,"meters")

#Comments in Python begin with a # and extend to the length of the line
#Multiline comments are possible, delimited by triple quotes """

"""These two inputs show a key feature of Python - dynamic typing
wherein the variable type is determined at run time"""
h0 = float(input("Enter the height of the tower in meters: "))
#t = float(input("Enter the time interval in sec.: "))
t=0.

#calculate the height.  Multiplication uses * and raising to a power **
h=h0
with open('drop.dat','w') as f:
    while h > 0: 
        curstr = str(t) + " " + str(h) + "\n"
        f.write(curstr)
        t=t+1.
        s = 9.81*t**2/2
        h=h0-s

    f.closed

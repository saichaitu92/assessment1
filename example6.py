print ("show last 10 digits of number")
x= int(input("enter number "))
p= x
while x>(p-10):
    x=x-1
    print(x)
    continue

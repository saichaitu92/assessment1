print("largest numbers among three input")

a= int(input("enter number 1: "))
b= int(input("enter number 2: "))
c= int(input("enter number 3: "))
if a > b:
        if a>c :
            print ("largest is ",+a)
else :
     if c>b :
         print ("largest is ",+c)
     else:
         print("largest is ",+b)

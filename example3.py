#print("leap year checking ")
#leap year consists of 366 day so in general every year has 365 days
#and in the leapyear the one extra day will be on second month so in feb
#we have 28 days  if it is leap year then it should contain 29days
#a=  int(input("enter the number of days in febuary  " ))
#if a == 29:
#    print ("hooray its leap year")
#elif a!= 29:
#    print("not leap year")

#doubt
y=int(input("enter year:"))
print("entered year is:",+y)
while((y%4 == 0) or (y%400 == 0)):
    print("leap year")
    break
else :
    print ("not leap year")

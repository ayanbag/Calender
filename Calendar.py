import calendar
from datetime import *
def choice():
    print("Enter 1 for Month View of Calender")
    print("Enter 2 for Todays Date with Time")
    print ("Enter 3 for to view all remainder")
def date(moth,yr):
    return calendar.month(yr,moth)
def current():
    return datetime.now()
def save_tt(rem):
    try:
       f=open("Remainder.txt","a")
       f.write(rem+"\n")
       f.close()
    except Exception:
        print ("")
def read_tt1():
    try:
        f=open("Remainder.txt","r")
        return  (f.read())
    except Exception:
        print("Process Error")

print ("Welcome to The Calender")
print("--------------------------------")
choice()
a=int(input("> "))

try:
    if a==1:
        yr1=int(input("Enter the Year: "))
        moth1=int(input("Enter the month you want to View: "))
        print(date(moth1,yr1))
        print("Do You want to enter any Remainder : ")
        yw=input("> ")
        if yw=="Y" or yw=="y" or yw=="Yes" or yw=="yes" or yw=="YES" :
            print("  ")
            print("   ")
            d1=int(input("Enter the date: "))
            print("Enter the Remainder you want: ")
            rem1=input("> ")
            rem3 = "Date: "+str(d1)+"-"+str(moth1)+"-"+str(yr1)+" |||"+" "+"Remainder: "+rem1
            print(rem3)
            save_tt(rem3)
            print(" ")
            print("Thank You ")
            print("-----------------")
            print(read_tt1())
            
    elif a==2:
        print (current())
        
    elif a==3:
        print(read_tt1())
    else : 
        print("Enter correct option")
    
except Exception:
    print("Process Error")





            

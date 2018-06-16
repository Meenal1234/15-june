#!/usr/bin/python2
def factorial(num):
    if num==1:
         return num
    else:
         return num*factorial(num-1)
num=input("enter a number")
if num<0:
   print"factorial cannot be negative"
elif num==0:
   print"factorial is 1"
else:
   print"factorial is",factorial(num)

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:38:22 2019
Program 12:Palindrome or not checking 

@author: MONU
"""
a = int(input("Enter a number : "))
n = 0
r = a
while r !=0:
    n = (n*10)+(r%10)
    r = r//10
    
if (n==a):
    print(a,"is a palindrome number")
else:
    print(a,"is not a palindrome number")
    


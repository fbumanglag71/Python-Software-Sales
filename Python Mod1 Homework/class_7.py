## Author: Francisco Bumanglag
## Project: Software Sales 
## Assignment: Module 1 Project 7
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023


#CONSTANTS 
PACKAGE_PRICE = 99

#INPUT 
quantity = int(input('Enter the number of items you would like to purchase: '))

#CALCULATIONS
totalPurchases = quantity * PACKAGE_PRICE


#IF -ELIF STATEMENT TO DETERMINE DISCOUNT -- THEN DISPLAY OUTPUT OR ERROR MESSAGE
if quantity < 10: 
    print('No discount was applied.  Your total purchase is $: ', totalPurchases)

elif quantity >= 10 and quantity <=19:
    discount = totalPurchases *.1
    discountedPrice = totalPurchases - discount     
   
elif quantity >= 20 and quantity <=49:
    discount = totalPurchases *.2
    discountedPrice = totalPurchases - discount     
 
elif quantity >= 50 and quantity <=99:
    discount = totalPurchases *.3
    discountedPrice = totalPurchases - discount     
    
elif quantity >= 100: 
    discount = totalPurchases *.4
    discountedPrice = totalPurchases - discount     
    
else: 
  print('Error.  Invalid entry.  Please reenter the quantity')

print('Your discount is 10%.  Your original total was : $' , totalPurchases, 
          ' and your discounted price is :$' , discountedPrice)

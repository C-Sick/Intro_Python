#!/usr/bin/env python3
  2 
  3 """
  4 Author: Priya 
  5 Date: Sep 3rd  
  6 Description: This customer charges fror customrs 
  7 """
  8 def total_charges_cal(charg_nv, charg_cl):
  9     return (charg_nv + charg_cl)
 10 
 11 def main():
 12         price_nv = 3.00
 13         price_cl = 2.00
 14 
 15         Qt_nv = int(input("Enter the numbr of New Videos Purchased: "))
 16         Qt_cl = int(input("Enter the numbr of Classic videos Purchased: "))
 17 
 18         charg_nv = Qt_nv * price_nv
 19         charg_cl = Qt_cl * price_cl
 20 
 21         total_charges = total_charges_cal(charg_nv, charg_cl)
 22 
 23         print("The total_charges for your purchase today is $", round(total_charges, 2))
 24 
 25 if __name__ == "__main__":
 26     main()

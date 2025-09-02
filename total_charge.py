!/usr/bin/env python3
  2 
  3 """
  4 Author: Priya 
  5 Date: Sep 3rd  
  6 Description: This customer charges fror customrs 
  7 """
  8 def total_charges_cal(charg_nv, charge_cl):
  9     return (charg_nv + charg_cl)
 10     
 11 def main():
 12         Qt_nv = int(input("Enter the numbr of New Videos Purchased"))
 13         Qt_cl = int(input("Enter the numbr of Classic videos Purchased"))
 14         charg_nv = Qt_nv * price_nv
 15         charg_cl = Qt_cl * price_cl 
 16         price_nv = 3.00
 17         price_cl = 2.00
 18         total_charges = total_charges_cal()
 19         print("The total_charges for your purchase today is", round(total_charges, 2)
 20 
 21 
 22 if __name__ == "__manin__":
 23     main()
 24     

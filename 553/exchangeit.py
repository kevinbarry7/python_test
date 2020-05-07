"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Kevin Barry
Date: April 18th 2020
"""
import currency

src = input("3-letter code for original currency: ")
dst = input("3-letter code for the new currency: ")
amt = float(input("Amount of the original currency: "))
dst_amt = currency.exchange(src, dst, amt)
# print("You can exchange " + str(amt) + " " + src + " for " + "{:.3f}".format(dst_amt) + " " + dst + ".")
print('You can exchange ' + str(amt) + ' ' + str(src) + ' for' + str(round(dst_amt, 3)) + ' ' + str(dst) + '.')


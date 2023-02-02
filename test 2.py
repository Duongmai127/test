# Name: thieu nguyen
# UNumber: u6475-2139

# A program that check whether a fraction is proper or improper, and if it can be reduced or not. Also provide the mixed 
# number if it is improper.

import math


numerator = int(input('Enter the numerator. Value must be greater than 0: '))
while numerator <= 0:
    print('The numerator cannot be negative')
    numerator = int(input('Enter the numerator: '))

denominator = int(input('Enter the denominator. Value must be greater than 0: '))
while denominator <= 0:
    print('The denominator cannot be negative')
    denominator = int(input('Enter the denominator: '))

gcd = math.gcd(numerator, denominator)

if numerator < denominator:
    print('The {numerator}/{denominator} is a proper fraction'.format(numerator=numerator, denominator=denominator))

    if gcd == 1:
        print('This proper fraction cannot be reduced further')
    else:
        print('The proper fraction can be reduced to: {}/{}'.format(numerator/gcd, denominator/gcd))
    
else:
    print(f'{numerator}/{denominator} is improper fraction')

    whole_number = numerator // denominator
    remainder = numerator % denominator
    if gcd == 1:
        print('The improper fraction cannot be reduced further')
    else:
        print('The improper fraction can be reduced to: {}/{}'.format(numerator/gcd, denominator/gcd))

    if remainder == 0:
        print('The whole number is: {}'.format(whole_number))
    else:
        gcd = math.gcd(remainder, denominator)
        if gcd == 1:
            print('The mixed number is: {} and {}/{}'.format(whole_number, remainder, denominator))
        else:
            print('The mixed number is: {} and {}/{}'.format(whole_number, remainder/gcd, denominator/gcd))

    


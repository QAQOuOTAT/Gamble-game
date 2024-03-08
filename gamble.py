# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:34:53 2024

@author: LAM Quincy
"""
import time
import random
min = 1
max = 6
coins=int(10)
print('=======================================','\nType x to exit','\n=======================================')
while True:
    print('You have : $',coins)
    input1=input("Roll the dices?(yes or no)  ")
    print('---------------------------------------')
    if input1 == 'x':
        print('Exit','Thanks for using')
        print('=======================================')
        break
    if input1 == "yes" or input1 == "y":
        b1=random.randint(min, max)
        b2=random.randint(min, max)
        t2=b1+b2
        for char in ['.', '..', '...']:
            print(f'\rRolling the dices{char}', end='')
            time.sleep(0.5)
        print('\n---------------------------------------')
        a1=random.randint(min, max)
        a2=random.randint(min, max)
        t1=a1+a2
        time.sleep(1)
        print('Your Dice')
        time.sleep(1)
        print('Dice1 : ',a1,'Dice2 :',a2,', Total = ',t1)
        print('---------------------------------------')
        time.sleep(1)
        input2=input("Gamble?(yes or no)  ")
        time.sleep(1)
        if input2 == "yes" or input2 == "y":
            input3=int(input('How much will you cost : '))
            print('\n---------------------------------------')
            time.sleep(1)
            print('You pay $',input3,',Good Luck')
            coins=coins-input3
            time.sleep(1)
            print('Now you have $',coins)
            print('\n---------------------------------------')
            time.sleep(1)
            print('His Dice')
            time.sleep(1)
            print('Dice1 : ',b1,'Dice2 :',b2,', Total = ',t2)
            print('\n---------------------------------------')
            time.sleep(1)
            if t1>t2:
                coins=coins+2*(input3)
                print('Lucky,Now you have $',coins)
            elif t1==t2:
                coins=coins+input3
                print('Now you have $',coins)
            elif t1<t2:
                print('Unlucky,Now you have $',coins)
        if input2 == "no" or input2 == "n":
            print('\n---------------------------------------')
            print('You did not play the game')
            time.sleep(1)
            print('Now you have $',coins)
        print('\n---------------------------------------')
    
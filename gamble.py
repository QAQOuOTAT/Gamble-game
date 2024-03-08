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
print('=======================================')
while True:
    print('You have : $',coins)
    time.sleep(1)
    if coins <= 0:
        print('\nIs time to stop gambling')
        time.sleep(1)
        print(' or call : 1800 858 858 \n')
    elif coins >= 100:
        print('\n High-risk , High-reward \n')
    input1=input("Roll the dices?(yes or no)  ")
    print('---------------------------------------')
    if input1 == 'no' or input1 == 'n' :
        print('                 Exit                  ')
        time.sleep(1)
        print('              Good choose              ')
        print('=======================================')
        break
    if input1 == "yes" or input1 == "y":
        print('His Turn')
        for char in ['.', '..', '...']:
            print(f'\rRolling the dices{char}', end='')
            time.sleep(0.5)
        print('\nHis Dices is ready')
        b1=random.randint(min, max)
        b2=random.randint(min, max)
        t2=b1+b2
        print('---------------------------------------')
        print('Your Turn')
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
        print('You have : $',coins)
        time.sleep(1)
        input2=input("Gamble?(yes or no)  ")
        time.sleep(1)
        if input2 == "yes" or input2 == "y":
            print('\n- High-risk High-reward -\n')
            time.sleep(1)
            input3=int(input('How much will you cost : '))
            print('---------------------------------------')
            time.sleep(1)
            print('You pay $',input3,',Good Luck')
            coins=coins-input3
            time.sleep(1)
            print('Now you have $',coins)
            print('---------------------------------------')
            time.sleep(1)
            print('His Dice')
            time.sleep(1)
            print('Dice1 : ',b1,'Dice2 :',b2,', Total = ',t2)
            print('---------------------------------------')
            time.sleep(1)
            if t1>t2:
                coins=coins+2*(input3)
                print('- (Yours)',t1,' > ',t2,'(His) -')
                print('Lucky,Now you win $',input3)
            elif t1==t2:
                coins=coins+input3
                print('- (Yours)',t1,' = ',t2,'(His) -')
                print("Now you haven't lose any coins")
            elif t1<t2:
                print('- (Yours)',t1,' < ',t2,'(His) -')
                print('Unlucky,Now you lose $',input3)
        if input2 == "no" or input2 == "n":
            print('---------------------------------------')
            print('You did not play this round')
            time.sleep(1)
            print('        Good choose        ')
            time.sleep(1)
            print("You haven't lose any coins ")
        print('---------------------------------------')
    
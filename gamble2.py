# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 22:33:31 2024

@author: LAM Quincy
"""

import time
import random
import os
min = 1
max = 6
coins=float(10)
line1='=========================================='
line2='------------------------------------------'
listA=('| 大 | 兩個骰子相同 | 小 | => | 4 | 5 | 6 |')
listB=('| 大 | 三個骰子相同 | 小 | => | 1 | 2 | 3 |')  
print(line1)
print('              Type x to Exit             ')
print(line1)
print('    買 大    : 1 賠   1  ')
print('    買 小    : 1 賠   1  ')
print(' 兩個骰子相同 : 1 賠   5  ')
print(' 三個骰子相同 : 1 賠  150  ')
time.sleep(0.5)
while True:
    print(line1)
    print(listA)
    print(listB)
    print(line1)
    time.sleep(0.5)
    print('You have : $',coins,)
    time.sleep(1)
    if coins <= 0:
        time.sleep(1)
        print('==========================================')
        print('\n        Is time to stop gambling          ')
        time.sleep(0.5)
        print('         or call : 1800 858 858           ')
        time.sleep(1)
        print('                Game over                 \n')
        print('==========================================')
        time.sleep(10)
        os.system('cls')
        break
    elif coins >= 100:
        print('- High-risk , High-reward -')
    a1=random.randint(min, max)
    a2=random.randint(min, max)
    a3=random.randint(min, max)
    t1=a1+a2+a3
    time.sleep(1)
    for char in ['','.', '..', '...']:
        print(f'\rRolling the dices{char}', end='')
        time.sleep(0.5)
    print('\n\a- Dices are ready -')
    print(line2)
    input1=input(' 買定離手 : ')
    if input1 == 'x':
        time.sleep(1)
        print('==========================================')
        time.sleep(1)
        print('        You win ',coins,' this time         ')
        time.sleep(1)
        print('                  Exit                    ')
        time.sleep(1)
        print('               Good choose                ')
        time.sleep(1)
        print('             Thx for playing              ')
        print('==========================================')
        time.sleep(10)
        os.system('cls')
        break
    input3=input(' 下注金額 : $')
    if input3 == 'x':
        time.sleep(1)
        print('==========================================')
        time.sleep(1)
        print('        You wiln ',coins,' this time         ')
        time.sleep(1)
        print('                  Exit                    ')
        time.sleep(1)
        print('               Good choose                ')
        time.sleep(1)
        print('             Thx for playing              ')
        print('==========================================')
        time.sleep(10)
        os.system('cls')
        break
    input2=float(input3)
    if input2<=0:
        print(line2)
        print('You did not join this round')
        time.sleep(1)
        print('\n- Dice -')
        time.sleep(1)
        print('Dice1 : ',a1,'Dice2 :',a2,'Dice3 :',a3,', Total = ',t1)
        time.sleep(1)
        print('\n       Good choose?        ')
        time.sleep(1)
        print("You haven't lose any coins ")
    else:
        if input1 == '1' or input1 == '4':
            time.sleep(1)
            print('- 買大 -')
            time.sleep(1)
            if input2>0: 
                if input2>coins:
                    input2=coins
                if input2==coins:
                    time.sleep(1)
                    print('- How dare You ALL IN -')
            print(line2)
            time.sleep(1)
            print('You pay $',input2,',Good Luck')
            coins=coins-input2
            time.sleep(1)
            print('Now you have $',coins)
            print(line2)
            time.sleep(1)
            print('Dice1 :',a1,',Dice2 :',a2,',Dice3 :',a3,', Total = ',t1)
            if t1>11:
                time.sleep(1)
                print('          - ',t1,' > ','11 -')
                time.sleep(1)
                coins=coins+2*(input2)
                print('Lucky,you win $',2*(input2))
            elif t1==11:
                time.sleep(1)
                print('          - ',t1,' = ','11 -')
                time.sleep(1)
                coins=coins+2*(input2)
                print('Lucky,you win $',2*(input2))
            else:
                print('          - ',t1,' < ','11 -')
                print('Unlucky,Now you lose $',input2)
        if input1 == '3' or input1 == '6':
            time.sleep(1)
            print('\n- 買小 -\n')
            time.sleep(1)
            if input2>0: 
                if input2>coins:
                    input2=coins
                if input2==coins:
                    time.sleep(1)
                    print('-How dare You ALL IN-')
                print(line2)
            time.sleep(1)
            print('You pay $',input2,',Good Luck')
            coins=coins-input2
            time.sleep(1)
            print('Now you have $',coins)
            print(line2)
            time.sleep(1)
            print('Dice1 :',a1,',Dice2 :',a2,',Dice3 :',a3,', Total = ',t1)
            if t1<10:
                time.sleep(1)
                print('          - ',t1,' < ','10 -')
                time.sleep(1)
                coins=coins+2*(input2)
                print('Lucky,you win $',2*(input2))
            elif t1==10:
                time.sleep(1)
                print('          - ',t1,' = ','10 -')
                time.sleep(1)
                coins=coins+2*(input2)
                print('Lucky,you win $',2*(input2))
            else:
                print('          - ',t1,' < ','10 -')
                print('Unlucky,Now you lose $',input2)
        if input1 == '5':
            time.sleep(1)
            print('\n- 兩個骰子相同 -\n')
            time.sleep(1)
            if input2>0: 
                if input2>coins:
                    input2=coins
                if input2==coins:
                    time.sleep(1)
                    print('-How dare You ALL IN-')
                print(line2)
            time.sleep(1)
            print('You pay $',input2,',Good Luck')
            coins=coins-input2
            time.sleep(1)
            print('Now you have $',coins)
            print(line2)
            time.sleep(1)
            print('Dice1 :',a1,',Dice2 :',a2,',Dice3 :',a3,', Total = ',t1)
            if a1==a2 or a1==a3 or a2==a3:
                time.sleep(1)
                print('    - 兩個骰子相同 -    ')
                time.sleep(1)
                coins=coins+6*(input2)
                print('Lucky,you win $',6*(input2))
            else:
                print('    - 兩個骰子不相同 -    ')
                print('Unlucky,Now you lose $',input2)
        if input1 == '2':
            time.sleep(1)
            print('\n- 三個骰子相同 -\n')
            time.sleep(1)
            if input2>0: 
                if input2>coins:
                    input2=coins
                if input2==coins:
                    time.sleep(1)
                    print('-How dare You ALL IN-')
                print(line2)
            time.sleep(1)
            print('You pay $',input2,',Good Luck')
            coins=coins-input2
            time.sleep(1)
            print('Now you have $',coins)
            print(line2)
            time.sleep(1)
            print('Dice1 :',a1,',Dice2 :',a2,',Dice3 :',a3,', Total = ',t1)
            if a1==a2==a3:
                time.sleep(1)
                print('    - 三個骰子相同 -    ')
                time.sleep(1)
                coins=coins+151*(input2)
                print('Lucky,you win $',151*(input2))
            else:
                print('    - 三個骰子不相同-    ')
                print('Unlucky,Now you lose $',input2)
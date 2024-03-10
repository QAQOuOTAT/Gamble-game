# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:13:52 2024

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
numlist=['4','5','6','2']
listA=('| 大 | 兩個骰子相同 | 小 | => | 4 | 5 | 6 |')
listB=('| 大 | 三個骰子相同 | 小 | => | 4 | 2 | 6 |') 
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
    print('\n')
    print(line2)
    print('\a- Dices are ready -')
    print(line2)
    print( '- 0 => Yes 1 => NO -\n')
    playlist=dict()
    j=input('Join the game? ')
    if j == 'x':
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
        time.sleep(5)
        os.system('cls')
        break
    if j== '1':
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
    if j == '0':
        time.sleep(1)
        print('- Type x to finish -')
        while True:
            print(line2)
            input1=input(' 買定離手 :  ')
            if input1 =='x':
                print(line2)
                break
            if input1 in numlist:
                input3=input(' 下注金額 : $')
                if input3 =='x':
                    print(line2)
                    break
                input2=float(input3)
                if input2>coins:
                    input2=coins
                playlist[input1]=input2
                coins=coins-input2
                print('You have $',coins)
                if coins<=0:
                    print(line2)
                    time.sleep(1)
                    print("You don't have enough money")
                    time.sleep(1)
                    print(line2)
                    break
            if input1 in playlist:
                playlist[input1]=playlist[input1]+input2
            if input1 not in numlist:
                print('Please input correctly')
    time.sleep(1)
    for char in ['','.', '..', '...']:
        print(f'\rLoading{char}', end='')
        time.sleep(0.5)
    print('\n')
    print('Dice1 :',a1,',Dice2 :',a2,',Dice3 :',a3,', Total = ',t1)
    print(line2)
    if '4' in playlist:
        time.sleep(1)
        print('\n- 買大 -\n')
        print(line2)
        if t1>11:
            time.sleep(1)
            print('          - ',t1,' > ','11 -')
            time.sleep(1)
            print('Lucky,you win $',(playlist['4']))
            coins=coins+(playlist['4'])
        elif t1==11:
            time.sleep(1)
            print('          - ',t1,' = ','11 -')
            time.sleep(1)
            print('Lucky,you win $',(playlist['4']))
            coins=coins+(playlist['4'])
        else:
            print('          - ',t1,' < ','11 -')
            print('Unlucky,Now you lose $',playlist['4']/2)
        print(line2)
    if '6' in playlist:
        time.sleep(1)
        print('\n- 買小 -\n')
        print(line2)
        if t1<10:
            time.sleep(1)
            print('          - ',t1,' < ','10 -')
            time.sleep(1)
            coins=coins+(playlist['6'])
            print('Lucky,you win $',(playlist['6']))
        elif t1==10:
            time.sleep(1)
            print('          - ',t1,' = ','10 -')
            time.sleep(1)
            coins=coins+2*(playlist['6'])
            print('Lucky,you win $',(playlist['6']))
        else:
            print('          - ',t1,' > ','10 -')
            print('Unlucky,Now you lose $',playlist['6']/2)
        print(line2)
    if '5' in playlist:
        time.sleep(1)
        print('\n- 兩個骰子相同 -\n')
        print(line2)
        if a1==a2 or a1==a3 or a2==a3:
            time.sleep(1)
            print('    - 兩個骰子相同 -    ')
            time.sleep(1)
            coins=coins+5*(playlist['5'])
            print('Lucky,you win $',(playlist['5']))
        else:
            print('    - 兩個骰子不相同 -    ')
            print('Unlucky,Now you lose $',playlist['5']/2)
        print(line2)
    if '2' in playlist:
        time.sleep(1)
        print('\n- 三個骰子相同 -\n')
        print(line2)
        if a1==a2==a3:
            time.sleep(1)
            print('    - 三個骰子相同 -    ')
            time.sleep(1)
            coins=coins+150*(playlist['2'])
            print('Lucky,you win $',150*(playlist['2']))
        else:
            print('    - 三個骰子不相同-    ')
            print('Unlucky,Now you lose $',playlist['2']/2)
        print(line2)
    time.sleep(1)
    print(f'\rLoading{char}', end='')
    time.sleep(1)
    print('Next Round is Ready')
    time.sleep(0.5)
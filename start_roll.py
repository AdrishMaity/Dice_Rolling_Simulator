#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 06:56:21 2018

Application Name: //__ROLL__DICE__ROLLER__\\
Description: Dice roller app using ASCII art

Instruction to run: 
    1> Open terminal or command promt
    2> run python strat_roll.py
        (i)  enter 'r' without quotes to start roll
        (ii) enter 'q' without quotes to exit program

@author: adrish | email: adrish.maity@outlook.com

"""
import time
import subprocess as sp
import random
from sys import platform


################### Clear Screen Function Based On System OS ########################
def clearScreen():
    if platform == "linux" or platform == "linux2":
        sp.call('clear',shell=True)
        print("\n\n")
    else:
        sp.call('cls',shell=True)
        print("\n\n")


################### Main Function ###################################################
def main():
    ############ Read dice1 ascii codes used in animation ################
    dice1 = open(r'dice_face1.txt','r')
    dice1_content = dice1.read()
    dice1.close()
    
    ############ Read dice1 ascii codes used in animation ################
    dice2 = open(r'dice_face2.txt','r')
    dice2_content = dice2.read()
    dice2.close()
    
    ############ Read all dice ascii codes used in result display ################
    all_dices = open(r'dices.txt','r')
    all_dices_content = all_dices.read()
    all_dices.close()
    
    ############ Dictonary to strore dice ascii codes ###################
    diceDictionary = {}
    
    ############ one dice art takes 297 ascii characters #################
    for i in range(6):
        diceDictionary[i+1] = all_dices_content[i*297:(298*(i+1)+1)]
    
    
    ############## Application Loop ####################
    while(True):
        clearScreen()
        print("\t\t\t______________WELCOME TO //__ROLL__DICE__ROLLER__\\\______________\n\n")
        userInput = input("\t\t\tenter 'r' to roll dice or 'q' to exit: ")
        
        if userInput == 'r':
            
            ############## Roll Animation 6 times ####################
            for i in range(6):
                clearScreen()
                print('%s\r'%dice1_content)
                time.sleep(0.3)
                clearScreen()
                print('%s\r'%dice2_content)
                time.sleep(0.3)
                clearScreen()
            
            ############## Print Result ##########################
            clearScreen()
            rolled = random.randint(1,6)
            print('%s\r\n\n'%diceDictionary[rolled])
            print('\t\tYou rolled: %d\n'%rolled)
            
            input('\t\tPress enter to continue..')
            
        elif userInput == 'q':
            clearScreen()
            print("\r\t\tThank you for using //__ROLL__DICE__ROLLER__\\\\n\n\n")
            exit()
        


if __name__ == '__main__':
    main()
    

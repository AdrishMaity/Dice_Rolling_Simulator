#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 06:56:21 2018

@author: adrish
"""
import time
import subprocess as sp
import random
from sys import platform


################### Clear Screen Function Based On System OS ########################
def clearScreen():
    if platform == "linux" or platform == "linux2":
        sp.call('clear',shell=True)
    else:
        sp.call('cls',shell=True)


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
    
    diceDictionary = {}
    
    for i in range(6):
        diceDictionary[i+1] = all_dices_content[i*72+i:(i*72+12*6+i)]
    
    while(True):
        clearScreen()
        print(" ______________WELCOME TO ROLL DICE ROLLER ______________")
        userInput = input("enter 'r' to roll dice or 'q' to exit: ")
        if userInput == 'r':
            for i in range(6):
                clearScreen()
                print('%s\r'%dice1_content)
                time.sleep(0.3)
                clearScreen()
                print('%s\r'%dice2_content)
                time.sleep(0.3)
                clearScreen()
            
            clearScreen()
            rolled = random.randint(1,6)
            print('%s\r\n\n'%diceDictionary[rolled])
            print('You rolled: %d\n'%rolled)
            
            input('Press enter to continue..')
        elif userInput == 'q':
            clearScreen()
            print("\rThank you for using __ROLL__DICE__ROLLER__\n\n\n")
            exit()
        


if __name__ == '__main__':
    main()
    

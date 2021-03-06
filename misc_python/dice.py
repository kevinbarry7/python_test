"""
A module providing a simple dice game.

The purpose of this module is to show off a slightly longer function that 
could benefit from being broken up into smaller functions.

Author: Kevin Barry
Date: March 28, 2020
"""
import random

def roll_off(handicap1,handicap2):
    """
    Returns true if player 1 wins the roll-off contest with player 2; otherwise returns false
    
    Each player rolls two dice and adds their handicap to the result.  Player 1 wins
    if his/her result is higher. This function will print out the player scores before
    it returns the result.
    
    Parameter handicap1: The handicap of player 1
    Precondition: handicap1 is a number
    
    Parameter handicap2: The handicap of player 2
    Precondition: handicap2 is a number
    """
    # Player 1 computes score
    # die1 = random.randint(1,6)
    # die2 = random.randint(1,6)
    sum1 = rollem(1, 6)
    sum1 += handicap1
    
    # Player 2 computes score
    sum2 = rollem(1, 6)
    sum2 += handicap2
    
    # Determine result
    print('Player 1 got '+str(sum1)+'; Player 2 got '+str(sum2)+'.')
    return sum1 > sum2

def rollem(first, last):
    
    num1 = random.randint(first,last)
    num2 = random.randint(first,last)
    thesum = num1+num2
    return thesum
"""
Script to play a text-based version of Quasar from Mass Effect

The rules are explained in the specifications below.  For the optimal strategy to
maximize your winnings, see

    https://masseffect.fandom.com/wiki/Quasar

Author: Kevin Barry
Date: May 23, 2020
"""
import random
import introcs


# Do not touch these first two functions. They are finished for you.
def prompt(prompt, valid):
    """
    Returns the choice from a given prompt.

    This function asks the user a question, and waits for a response.  It checks
    if the response is valid against a list of acceptable answers.  If it is not
    valid, it asks the question again. Otherwise, it returns the player's answer.

    Parameter prompt: The question prompt to display to the player
    Precondition: prompt is a string

    Parameter valid: The valid reponses
    Precondition: valid is a tuple of strings
    """
    # Ask the question for the first time.
    response = input(prompt)

    # Continue to ask while the response is not valid.
    while not (response in valid):
        print('Invalid option. Choose one of ' + str(valid))
        print()
        response = input(prompt)

    return response


def payout(bet, score):
    """
    Returns the winnings for a game of quasar.

    Winnings are payout-bet.  So winning your bet (on a score of 17) has a net of 0.

    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0

    Parameter score: the quasar score
    Precondition: score is an int >= 0
    """
    if score == 20:
        return bet
    elif score == 19:
        return round(0.5 * bet)
    elif score == 18:
        return round(0.25 * bet)
    elif score == 17:
        return 0
    elif score == 16:
        return round(-0.5 * bet)
    elif score == 15:
        return round(-0.75 * bet)

    # Everything else is a total loss
    return -bet


# Complete these functions
def get_bet(credits):
    """
    Returns the number of credits bet by the user.

    This function asks the user to make a bet

        Make a bet:

    If bet is not an integer, it responds with the error message

        The bet must be an integer.

    If bet is 0 or less, it responds with the error message

        The bet must be a positive integer.

    Finally, if bet is more than credits, it responds with the error message

        You do not have enough credits for that bet.

    It continues to ask for a bet until the user gives a valid answer.

    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    assert type(credits) == int, 'credits must be of type integer'
    assert credits > 0, 'not enough credits to bet'

    loop_control = True
    bet = 0

    while loop_control:

        bet = int(input('Make a bet: '))
        if type(bet) != int:
            print('The bet must be an integer')
        elif bet < 0:
            print('The bet must be a positive integer')
        elif bet >= credits:
            print('You do not have enough credits for that bet')
        else:
            loop_control = False
    return bet


def session(bet):
    """
    Returns the payout after playing a single session of quasar.

    The game starts by randomly choosing a number 1-8 and then displaying

        Your score is X.

    (where X is the number chosen). It then prompts the user with the following options:

        Choose (a) 4-7, (b) 1-8, or (s)top:

    If the user chooses 'a' or 'b', it picks a random number, adds it to the score,
    and then displays the score again.  If the user chooses 's' OR the new score is
    20 or more, the session is over.

    Once the session ends, if the user goes over 20, the function prints out

        You busted.

    However, if the user hits 20 exactly, the function prints out

        Quasar!

    Nothing extra is printed if the user is below 20.

    It then prints out

        You won X credits.

    or
        You lost X credits.

    as appropriate, where X is the payout (if X is 0, this is considered a win). When
    the session is done, the function returns the payout.

    Parameter bet: the number of credits bet
    Precondition: bet is an int > 0
    """

    assert type(bet) == int and bet > 0, 'bet is not type int or greater than zero'
    # assert bet > 0, 'The bet must be greater than zero'

    num = random.randint(1, 8)
    print('Your score is ' + str(num) + '.')
    loop_control = True
    while loop_control:
        response = prompt('Choose (a) 4-7, (b) 1-8, or (s)top: ', ('a', 'b', 's'))
        if response == 'a':
            num = num + random.randint(4, 7)
            if num < 20:
                print('Your score is ' + str(num) + '.')
            else:
                loop_control = False

        elif response == 'b':
            num = num + random.randint(1, 8)
            if num < 20:
                print('Your score is ' + str(num) + '.')
            else:
                loop_control = False
        elif response == 's':
            loop_control = False
        elif num > 20:
            print('You busted')
            loop_control = False
        elif num == 20:
            print('Quasar!')
            loop_control = False

    print('before payout')
    print('bet = ' + str(bet) + ' num = ' + str(num))
    pay = payout(bet, num)
    if pay >= 0:
        print('You won ' + str(pay) + ' credits.')
    else:
        print('You lost ' + str(pay) + ' credits.')
    return pay


def play(credits):
    """
    Plays Quasar until the player quits or is broke.

    The game starts by announcing

        You have X credits.

    where X is the number of credits.  It gets a bet from the user and plays a session
    of Quasar.  When done, it adds the payout to the score and repeats the message above.

    If the user reaches 0 credits, the game is over.  Otherwise, it asks

        Do you want to (c)ontinue or (p)ayout?

    If the user chooses 'c', the process repeats (get a bet, play a session, etc.)

    When done, the game prints

        You leave with X credits.

    assuming X > 0. However, if X is 0 it instead prints

        You went broke.

    Parameter credits: the number of credits available to bet
    Precondition: credits is an int > 0
    """
    assert type(credits) == int, 'credits are not of type int'
    assert credits > 0, 'credits are not greater than zero'

    print('You have ' + str(credits) + ' credits.')

    bet = get_bet(credits)
    payout = session(bet)
    credits_remaining = credits + payout
    print('You have ' + str(credits_remaining) + ' credits.')
    if credits > 0:
        game_on = True
        while game_on:
            response = prompt('Do you want to (c)ontinue or (p)ayout?', ('c', 'p'))
            if response == 'c':
                bet = get_bet(credits)
                payout = session(bet)
                credits_remaining = credits + payout
                print('You have ' + str(credits_remaining) + ' credits.')
            elif response == 'p':
                if credits > 0:
                    print('You leave with ' + str(credits) + ' credits.')
                    game_on = False
                else:
                    print('You went broke')
                    game_on = False
                


# Script Code
# DO NOT MODIFY BELOW THIS LINE
# if __name__ == '__main__':
#     play(1000)


get_bet(120.5)
# session(500)
#play(500)



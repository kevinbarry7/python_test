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
    print(bet)
    
    
get_bet(50)

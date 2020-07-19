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
    assert bet > 0, 'The bet must be greater than zero'
    print(bet)  # remove this line

    num = random.randint(1, 8)
    print('Your score is ' + str(num) + '.')
    loop_control = True
    while loop_control:
        response = prompt('Choose (a) 4-7, (b) 1-8, or (s)top:', ('a', 'b', 's'))
        if response == 'a':
            num = num + random.randint(4, 7)
            if num >= 20:
                loop_control = False
            else:
                print('Your score is ' + str(num) + '.')

        elif response == 'b':
            num = num + random.randint(1, 8)
            if num >= 20:
                loop_control = False
            else:
                print('Your score is ' + str(num) + '.')
        elif response == 's' or num > 20:
            print('You busted')
            loop_control = False
        elif num == 20:
            print('Quasar!')

        pay = payout(bet, num)
        if pay > 0:
            print('You won ' + str(pay) + ' credits.')
        else:
            print('You lost ' + str(pay) + ' credits.')
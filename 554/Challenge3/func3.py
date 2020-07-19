"""
Module for scoring blackjack hands.

In blackjack, face cards are worth 10, number cards are worth their value, and Aces
are worth either 1 or 11, whichever is more advantageous. The latter is what makes
scoring blackjack so tricky.

In this module, we assume that a card hand is represented by a tuple of strings, where
each string is two characters representing a card.  The first character is the rank of
the card: '2'-'9' for numerical cards, 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for
King and 'A' for Ace.  The second character is the suit: 'H' for hearts, 'D' for diamonds,
'C' for clubs, and 'S' for spades.

For example ('KS','AD') is a blackjack hand with the King of Spades and Ace of Diamonds.

Author: Kevin Barry
Date: May 25, 2020
"""
import introcs


def bjack(hand):
    """
    Returns the score of the blackjack hand.

    When scoring the hand, number cards are always worth their value and face cards
    (Jack, Queen, King) are always worth 10.  However, Aces are either worth 1 or 11,
    which ever is more advantageous.

    When determining how to value a hand, the score should be as high as possible without
    going over 21.  If the hand is worth more than 21 points, then all Aces should be
    worth 1 point.

    Examples:
        bjack(('KS','AD')) returns 21
        bjack(('KS','9C','AD')) returns 20
        bjack(('AS','AC','KH')) returns 12
        bjack(('AS','AC','KH','TD')) returns 22
        bjack(()) returns 0

    Parameter hand: the blackjack hand to score
    Precondition: hand is a (possibly empty) tuple of 2-character strings representing
    cards. The first character of each string is '2'-'9', 'T', 'J', 'Q', 'K', or 'A'.
    The second character of each string is 'H', 'D', 'C', or 'S'.
    """
    # Hint: Keep track of whether you have seen any aces in the hand that are worth 11
    # If so, subtract 10 from the accumulator if you go over.

    # assert

    i = 0
    ace = 0
    result = 0
    total = 0
    while i < len(hand):
        user_hand = hand[i]
        char = user_hand[0]

        if char == '2':
            result = 2
        elif char == 'A':
            result = 11
            ace = ace + 1
        elif char == '3':
            result = 3
        elif char == '4':
            result = 4
        elif char == '5':
            result = 5
        elif char == '6':
            result = 6
        elif char == '7':
            result = 7
        elif char == '8':
            result = 8
        elif char == '9':
            result = 9
        elif char == 'T' or 'J' or 'Q' or 'K':
            result = 10

        i = i + 1
        total = total + result
    if total > 21 and ace == 1:
        total = total - 10

        # print(ace)
    print('The blackjack hand total is ' + str(total) + '.')


bjack(('AH',))

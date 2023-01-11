"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if(card == "A"):
        return 1
    elif card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_1 = card_one
    card_2 = card_two
    faceCards = {'A': 1, 'J' : 10, 'Q' : 10, 'K' : 10}
    if card_one in faceCards.keys():
        card_one = faceCards[card_one]
    else:
        card_one = int(card_one)

    if card_two in faceCards.keys():
        card_two = faceCards[card_two]
    else:
        card_two = int(card_two)

    if card_one > card_two:
        return card_1
    elif card_one < card_two:
        return card_2
    else:
        return card_1, card_2


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    MAX = 21
    if(card_one == 'A' or card_two == 'A'):
      return 1

    if(value_of_card(card_one) + value_of_card(card_two) <= 10):
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if(card_one == 'A'):
        if(card_two == '10'):
            return True
        elif card_two == 'J':
            return True
        elif card_two == 'Q':
            return True
        elif card_two == 'K':
            return True
        else:
            return False
    elif (card_two == 'A'):
        if(card_one == '10'):
            return True
        elif card_one == 'J':
            return True
        elif card_one == 'Q':
            return True
        elif card_one == 'K':
            return True
        else:
            return False

    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass

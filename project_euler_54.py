"""
    Project Euler 54: Poker hands

        In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following
        way:

            High Card: Highest value card.
            One Pair: Two cards of the same value.
            Two Pairs: Two different pairs.
            Three of a Kind: Three cards of the same value.
            Straight: All cards are consecutive values.
            Flush: All cards of the same suit.
            Full House: Three of a kind and a pair.
            Four of a Kind: Four cards of the same value.
            Straight Flush: All cards are consecutive values of same suit.
            Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

        The cards are valued in the order:
        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

        If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair
        of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a
        pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie
        then the next highest cards are compared, and so on.

        Consider the following five hands dealt to two players:
        Hand	 	Player 1    	 	Player 2	 	        Winner
        1   	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD          Player 2
                    Pair of Fives       Pair of Eights
        2   	 	5D 8C 9S JS AC      2C 5C 7D 8S QH          Player 1
                    Highest card Ace    Highest card Queen
        3   	 	2D 9C AS AH AC      3D 6D 7D TD QD          Player 2
                    Three Aces          Flush with Diamonds
        4   	 	4D 6S 9H QH QC      3D 6D 7H QD QS          Player 1
                    Pair of Queens      Pair of Queens
                    Highest card Nine   Highest card Seven
        5   	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D          Player 1
                    Full House          Full House
                    With Three Fours    with Three Threes

        The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains
        ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's
        cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand
        is in no specific order, and in each hand there is a clear winner.

        How many hands does Player 1 win?
"""
import time

# Cards
# T stands for 10, so we only use one letter to represent each card.
cards = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
# Suits
suits = ("C", "D", "H", "S")


def read_data_from_file(file_name):
    """
    Read input data from file, and return a list, each item contains a pair of hands, one for each player.

    :param file_name: input data file
    :return: a list of dealt hands
    """
    dealt_hands = []

    with open(file_name, "r") as f:
        # Split each line into two hands, one for each player
        for line in f:
            temp_list = line.strip().split(" ")
            first_hand = tuple(temp_list[:5])
            second_hand = tuple(temp_list[5:])
            dealt_hands.append((first_hand, second_hand))

    return dealt_hands


def get_suit(card):
    """
    Get the suit of a card

    :param card:
    :return: Return the suit e.g. H, C, S, or D
    """
    return card[1]


def get_value(card):
    """
    Get the value of a card

    :param card:
    :return: return the value e.g. 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
    """
    return card[0]


def breakdown_hand(hand):
    """
    Split cards in a hand into two groups, one contains values, and the other contains suits

    :param hand:
    :return: two lists, one represents the values in the hand, the other represents suits
    """
    # The list index + 2 represents the card value i.e. index 0 represents card value 2
    # index 12 represents card value A
    # The list value shows how many cards with the same value are in a hand.
    value_list = [0] * 13

    # The suit_list index corresponding to the suit 
    # 0 corresponds to C, 1 to D, 2 to H, and 3 to S
    suit_list = [0] * 4

    for card in hand:
        value_list[cards.index(get_value(card))] += 1
        suit_list[suits.index(get_suit(card))] += 1

    return value_list, suit_list


def get_high_single_card(breakdown_cards):
    """
    Find the single card with highest value, which is not part of a pair, three of a kind etc.,

    :param breakdown_cards:
    :return: the highest value of a single card in the hand
    """
    card_values = breakdown_cards[0]

    for index, value in reversed(list(enumerate(card_values))):
        if value == 1 and value != check_straight(breakdown_cards) \
                and value != check_flush(breakdown_cards) and check_straight_flush(breakdown_cards):
            return index + 2

    # This means the highest card value is 2.
    return 2


def check_pairs(breakdown_cards):
    """
    Check if a hand contains pairs, and if so, return the values of the pairs

    :param breakdown_cards:
    :return: a list in the form [value1, value2] for where value1 and value2 are values 
    for each pair. If there is no pair, then value1 and value2 = -1
    """
    card_values = breakdown_cards[0]
    pair_values = []

    for index, value in list(enumerate(card_values)):
        # There is a pair
        if value == 2:
            # Get the value of the pair
            pair_values.append(index + 2)

    # If pair_values does not contain enough pair, write -1 to indicate that there is 
    # no other pair.
    # A hand should contain at most two pairs
    for i in range(2 - len(pair_values)):
        pair_values.append(-1)

    return pair_values


def check_three_of_a_kind(breakdown_cards):
    """
    Decide if a hand contains three cards of the same value

    :param breakdown_cards:
    :return: value of the three cards
    """
    card_values = breakdown_cards[0]

    for index, value in list(enumerate(card_values)):
        # There is three of a kind
        if value == 3:
            return index + 2

    # There is no three of a kind
    return -1


def check_straight(breakdown_cards):
    """
    Check if a hand contains all cards in consecutive values

    :param breakdown_cards:
    :return: the highest value of the five cards if they are straight, -1 otherwise
    """
    card_values = breakdown_cards[0]

    for index, value in list(enumerate(card_values)):
        # There are two cards of same value, no way to get straight
        if value > 1:
            return -1

        # First card in a possible straight
        if value == 1:
            # Check for all 4 subsequent cards
            if card_values[index + 1] != 1 or card_values[index + 2] != 1 or \
                    card_values[index + 3] != 1 or card_values[index + 4] != 1:
                return -1
            else:
                return index + 4 + 2


def check_flush(breakdown_cards):
    """
    Check if a hand contain a flush

    :param breakdown_cards:
    :return: the highest value of the five cards if there is a flush, -1 otherwise
    """
    card_values = breakdown_cards[0]
    card_suits = breakdown_cards[1]
    is_flush = False

    # Check for a flush
    for suit in card_suits:
        # There is a flush
        if suit == 5:
            is_flush = True

    # Get the highest card in the flush
    if is_flush is True:
        for index, value in reversed(list(enumerate(card_values))):
            # If we reach this point, value should be 0 or 1
            if value == 1:
                return index + 2
    else:
        return -1


def check_full_house(breakdown_cards):
    """
    Check to see if there is a full house

    :param breakdown_cards:
    :return: a pair of card values, one for three of a kind and the other for the pair if there is a 
    full house, return [-1, -1] otherwise.
    """
    card_values = breakdown_cards[0]
    pair_values = [-1, -1]

    for index, value in list(enumerate(card_values)):
        if value == 1 or value == 4 or value == 5:
            pair_values[0] = -1
            pair_values[1] = -1
            break
        elif value == 2:
            pair_values[1] = index + 2
        elif value == 3:
            pair_values[0] = index + 2

    return pair_values


def check_four_of_a_kind(breakdown_cards):
    """
    Check if a hand contains four cards of the same value

    :param breakdown_cards:
    :return: the value of the cards, if the hand contains four cards of the same value, 
    return -1 otherwise
    """
    card_values = breakdown_cards[0]

    for index, value in list(enumerate(card_values)):
        if value == 4:
            return index + 2

    return -1


def check_straight_flush(breakdown_cards):
    """
    Check if a hand contains all consecutive cards of same suit

    :param breakdown_cards:
    :return: the highest value of the cards if it is straight flush, return -1 otherwise
    """
    straight_value = check_straight(breakdown_cards)
    flush_value = check_flush(breakdown_cards)

    if straight_value != -1 and flush_value != -1:
        return straight_value
    else:
        return -1


def is_royal_flush(breakdown_cards):
    """
    Check if a hand contains a royal flush

    :param breakdown_cards:
    :return: True if the hand contains a royal flush, False otherwise
    """
    is_same_suit = check_flush(breakdown_cards)
    card_values = breakdown_cards[0]

    # Only need to check if there is a flush
    if is_same_suit == -1:
        return False
    else:
        # Check the last five cards
        for value in card_values[8:]:
            if value != 1:
                return False

    return True


def get_player_score(breakdown_cards):
    """
    Depending on the cards in hand, assign a player a score with the following maps:
        High Card: 1
        One Pair: 2
        Two Pairs: 3
        Three of a Kind: 4
        Straight: 5
        Flush: 6
        Full House: 7
        Four of a Kind: 8
        Straight Flush: 9
        Royal Flush: 10

    :param breakdown_cards:
    :return: corresponding score, corresponding card value of each group if there is a pair, two pairs, 
    three of a kind etc., and a single high card
    """
    single_high_card = get_high_single_card(breakdown_cards)
    group_card_value = -1

    if is_royal_flush(breakdown_cards) is True:
        score = 10
    elif check_straight_flush(breakdown_cards) != -1:
        score = 9
        group_card_value = check_straight_flush(breakdown_cards)
    elif check_four_of_a_kind(breakdown_cards) != -1:
        score = 8
        group_card_value = check_four_of_a_kind(breakdown_cards)
    elif check_full_house(breakdown_cards)[0] != -1:
        score = 7
        group_card_value = check_full_house(breakdown_cards)
    elif check_flush(breakdown_cards) != -1:
        score = 6
        group_card_value = check_flush(breakdown_cards)
    elif check_straight(breakdown_cards) != -1:
        score = 5
        group_card_value = check_straight(breakdown_cards)
    elif check_three_of_a_kind(breakdown_cards) != -1:
        score = 4
        group_card_value = check_three_of_a_kind(breakdown_cards)
    else:
        group_card_value = check_pairs(breakdown_cards)
        if group_card_value[1] != -1:
            # There should be two pairs
            score = 3
        elif group_card_value[0] != -1:
            # There is only one pair
            score = 2
        # No pair, just go with the high card only
        else:
            score = 1
            group_card_value = single_high_card

    return score, group_card_value, single_high_card


def does_player1_win(dealt_hand):
    """
    Decide if Player1 wins based on the input dealt hand

    :param dealt_hand: a tuple containing dealt hand for each player
    :return: True if Player1 wins, False if he does not
    """
    player1_score = get_player_score(breakdown_hand(dealt_hand[0]))
    player2_score = get_player_score(breakdown_hand(dealt_hand[1]))

    # Two players have different group e.g one has one pair, the other has a flush
    # Player 1 wins
    if player1_score[0] > player2_score[0]:
        return True
    # Player 2 wins
    if player1_score[0] < player2_score[0]:
        return False

    # Two players has the same rank (same type of group), they are just probably differed in the 
    # high cards in the pairs
    # Player 1 has higher high card, and wins
    if player1_score[1] > player2_score[1]:
        return True
    # Player 2 wins
    if player1_score[1] < player2_score[1]:
        return False

    # Last option, use the single high card to decide who wins because all previous conditions
    # do not match, or they simply ends up a tie
    # Player 1 wins
    if player1_score[2] > player2_score[2]:
        return True
    # Player2 wins or there is a tie
    else:
        return False


def calculate_number_of_wins_for_player1(dealt_hands):
    """
    Calculate the number of wins for Player 1 based on a set of dealt hands

    :param dealt_hands: list of dealt hands
    :return: The number of wins for Player 1
    """
    number_of_wins = 0

    for dealt_hand in dealt_hands:
        if does_player1_win(dealt_hand) is True:
            number_of_wins += 1

    return number_of_wins


def main():
    start_time = time.time()
    deals = read_data_from_file("project_euler_54.txt")
    result = calculate_number_of_wins_for_player1(deals)
    print("The result is {0}, found in {1} seconds.".format(result, time.time() - start_time))


if __name__ == "__main__":
    main()

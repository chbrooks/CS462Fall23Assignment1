from random import randint

# Blackjack.py
# This program extends the Monte Carlo strategy from the previous Approach problem to a
# somewhat more difficult domain - Blackjack.

# If you don't know the game Blackjack, you can read the description here:
# https://en.wikipedia.org/wiki/Blackjack
# This page from gymnasium might also help - we'll see this again later in the semester.
# https://gymnasium.farama.org/environments/toy_text/blackjack/#blackjack

# Our state space, or win table, is much larger now. Rather than just having a single
# value to consider, we have three values: our total, the dealer's visible total, and a boolean
# indicating whether we have an ace:

# e.g. (16, 5, 0) would indicate that we have a total of 16 in our hand, the dealer has a 5 visible
# (we don't know what's hidden), and we do not have an ace.

# We'll stick to the situation where the dealer follows a strict rule - they 'hit'
# (or take another card) at 16 or lower, and 'stick' (or stop taking cards) at 17 or above.

# as in the gymnasium implementation, we will keep things simple by assuming that the
# deck is infinitely large, with replacement, so we don't need to keep track of the cards
# that have already been played. (in probability terms, our observations are independent.)

# you implement this. Assume that the input is of the form:
# get_total([1,2,5,6,2]) as in test_Blackjack.py
def get_total(list_of_cards) :
  pass

def draw_card() :
    return randint(1,11)

def has_ace(hand) :
    return 1 if 11 in hand else 0


def blackjack() :
    win_table = {}
    for i in range(4,22) :
        for j in range (1,12) :
            for k in range (0,2) :
                win_table[(i,j,k)] = 0

    for item in win_table : ## for each item, let's see how many times we win if we hold there.

        for i in range(10000) :
        ## play a game.
            # what are the players truly holding
            player_hand = (randint(1,11), randint(1,11))
            dealer_hand = (randint(1,11), randint(1,11))
            # what is our current state?
            observation = (get_total(player_hand),
                            dealer_hand[0],
                            1 if player_hand[0] == 11 or player_hand[1] == 11 else 0)
        stick_val = item[0]
        # You do the rest. Player 1 draws until their total exceeds stick_val
        # if they don't bust, the dealer goes.
        # if you win, increment win_table

    # print out the percentage of times we won holding in this state.
    for item in win_table.keys() :
        print("%s: %f" % (item, win_table[item]/10000))

blackjack()
# https://adventofcode.com/2023/day/7


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

# strength of cards from top to bottom
# if two types of hands are the same the one with the higher cards wins

# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
# The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

# e.g.  five hands -> strongest hands = 5 points, weakest = 1 point

# To make things a little more interesting, the Elf introduces one additional rule.
# Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

# To balance this, J cards are now the weakest individual cards, weaker even than 2.
# The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

from enum import IntEnum


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    ONE_PAIR = 2
    HIGH_CARD = 1


card_strenghts_ordered = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_type_of_hand(hand: dict) -> HandType:
    # type of card e.g. A : found_instances
    found_pair: bool = False
    found_triplet: bool = False

    # get jokers in hand
    jokers_used: bool = False
    jokers: int = hand.get("J", 0)
    print("JOKERS: ", jokers)

    # remove jokers from checked cards
    hand.pop("J", -1)

    if jokers > 0:
        print("HAND WITH JOKERS:", hand)

    if jokers == 5:
        # removed from map therefore not checked
        return HandType.FIVE_OF_A_KIND

    if jokers == 0:
        # look, I had code working for with jokers and code working for without jokers
        # this was the fastest way without losing my mind
        for card in hand:
            if hand[card] >= 4:
                # number of cards over 3 equal to the type of hand -> 5 = FIVE_OF_A_KIND
                match hand[card]:
                    case 4:
                        return HandType.FOUR_OF_A_KIND
                    case 5:
                        return HandType.FIVE_OF_A_KIND
            elif hand[card] == 3:
                if found_pair:
                    return HandType.FULL_HOUSE
                else:
                    found_triplet = True
            elif hand[card] == 2 and found_pair:
                return HandType.TWO_PAIRS

            # next pair found -> two pairs
            if hand[card] == 2:
                found_pair = True

        if found_triplet and found_pair:
            return HandType.FULL_HOUSE
        elif found_triplet:
            return HandType.THREE_OF_A_KIND
        elif found_pair:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD
    else:
        for card in hand:
            if hand[card] + jokers >= 4:
                # number of cards over 3 equal to the type of hand -> 5 = FIVE_OF_A_KIND
                match hand[card] + jokers:
                    case 4:
                        return HandType.FOUR_OF_A_KIND
                    case 5:
                        return HandType.FIVE_OF_A_KIND
            elif hand[card] + jokers == 3 and (not jokers_used):
                if found_pair:
                    return HandType.FULL_HOUSE
                else:
                    found_triplet = True
            elif hand[card] == 2 and found_pair:
                return HandType.TWO_PAIRS

            # next pair found -> two pairs
            if hand[card] == 2 and (not jokers_used and found_triplet):
                found_pair = True
            elif hand[card] + jokers == 2:
                jokers_used = True
                found_pair = True

        if found_triplet and found_pair and ():
            return HandType.FULL_HOUSE
        elif found_triplet:
            return HandType.THREE_OF_A_KIND
        elif found_pair:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD


def compare_hands(hands: list[str]) -> list[str]:
    # return the sorted list -> starting with higher hand
    # higher hand = the hand with the higher card at the start / from the left
    for i in range(len(hands) - 1):
        # bubble sort -> lower hands at the start
        for j in range(0, len(hands) - i - 1):
            for card_index in range(5):
                diff: int = (
                    card_strenghts_ordered[hands[j][card_index]]
                    - card_strenghts_ordered[hands[j + 1][card_index]]
                )
                if diff == 0:
                    # equal -> compare next
                    continue
                elif diff > 0:
                    # next hand higher -> switch hands
                    hands[j], hands[j + 1] = hands[j + 1], hands[j]

                # swapped or correct order -> compare next hands
                break

    return hands


def rank_hands(unordered_hands: map) -> map:
    # rank  cards
    duplicates_in_hand: {str: int} = {
        # type of card e.g. A : found_instances
    }

    cards = list(unordered_hands.keys())

    hand_scores: {HandType: list[str]} = {
        # type of hands -> 1 duplicate : [hand1, hand3,...]
    }

    for i in range(len(cards)):
        duplicates_in_hand.clear()

        # find duplicates
        for card in cards[i]:
            if duplicates_in_hand.get(card, 0) + 1 == 4:
                print(cards[i])
            duplicates_in_hand[card] = duplicates_in_hand.get(card, 0) + 1

        # get type of card
        duplicates_in_hand = dict(
            # sort duplicates -> to compare with jokers in mind
            sorted(duplicates_in_hand.items(), key=lambda x: x[1], reverse=True)
        )
        type: HandType = get_type_of_hand(duplicates_in_hand)
        print(cards[i], type)
        print("------------------------------\n")
        if hand_scores.get(type) == None:
            hand_scores[type] = [cards[i]]
        else:
            hand_scores[type].append(cards[i])

    # sort where multiple hands
    for key in hand_scores:
        hand_scores[key] = compare_hands(hand_scores[key])

    return hand_scores


# input
file = open("input.txt")
input = file.readlines()
file.close()

hands: {str, int} = {
    # cards : bid
}

for line in input:
    temp = line.split(" ")
    hands[temp[0]] = int(temp[1])

ranked_hands = rank_hands(hands)

# sort by keys -> lowest = high_card, highest = five_of_a_kind
ranked_hands = dict(sorted(ranked_hands.items()))

# print(ranked_hands)

sum = 0
current_rank = 0

# add up sums
for key in ranked_hands:
    print(key)
    for hand in ranked_hands[key]:
        print(hand)
        current_rank += 1
        sum += current_rank * hands[hand]
    print("---------------------------------")


print("SUM OF (BIDS * RANK):", sum)

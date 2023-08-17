import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)
    
def deal(number):
    cards_dealt = []
    for item in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt = deal(2)
card = cards_dealt[0]
rank = card[1]
print(card, rank)

rank_dict = {}
for item in ranks:
    if item == "A":
        value = 11
    elif item == "J" or item == "K" or item == "Q":
        value = 10
    else:
        value = item
    rank_dict.update({str(item): value})
print(rank_dict)
print(rank, value)


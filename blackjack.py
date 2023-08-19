import random

class Deck:
  def __init__(self):
    self.cards = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    
    n = len(ranks)
    for i in range(n):
      if ranks[i] == 'A':
        ranks[i] = dict(rank = "A", value = 11)
      elif ranks[i] == "J" or ranks[i] == "Q" or ranks[i] == "K":
        ranks[i] = dict(rank = ranks[i], valule = 10)
      else:
        ranks[i] = dict(rank = str(ranks[i]), value = int(ranks[i]))
        
    for suit in suits:
        for rank in ranks:
            self.cards.append([suit, rank])
    
  def shuffle(self):
      random.shuffle(self.cards)
      
  def deal(self, number):
      cards_dealt = []
      for item in range(number):
          card = self.cards.pop()
          cards_dealt.append(card)
      return cards_dealt

deck_1 = Deck()
deck_1.shuffle()
print(deck_1.cards)

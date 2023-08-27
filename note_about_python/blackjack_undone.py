import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

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
            self.cards.append(Card(suit, rank))
    
  def shuffle(self):
      if len(self.cards) > 1:
        random.shuffle(self.cards)
      
  def deal(self, number):
      cards_dealt = []
      for item in range(number):
          if len(self.cards) > 0:
            card = self.cards.pop()
            cards_dealt.append(card)
      return cards_dealt

class Hand:
  def  __init__(self, dealer = False):
    self.cards = []
    self.value = 0
    self.dealer = dealer

  def  add_card(self, card_list):
    return self.cards.extend(card_list)

  def  calculate_value(self):
    self.value = 0
    has_Ace = False
    
    for card in self.cards:
      value = int(card.rank['value'])
      self.value += value
      if card.rank['rank'] == 'A':
        has_Ace = True

    if has_Ace and self.value > 21:
      self.value -= 10

  def get_value(self):
    self.calculate_value()
    return self.value

  def  is_blackjack(self):
    return self.get_value() == 21

  def  display(self):
    print(f'''{"Dealer's:" if self.dealer else "Your"} hand:''')
    for card in self.cards:
      print(card)

    if not self.dealer:
      print("Value", self.get_value())
    print()
deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
print(hand.cards[0], hand.cards[1])

    

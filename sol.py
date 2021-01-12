class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def get_value(self, suit_val):
      return self.val+suit_val

suits = ['spades', 'diamonds', 'clubs', 'hearts', 'jokers']
deck = [Card(value, suit) for suit in suits for value in range(1, 14)]

deck.append(Card(0, 'jokers'))
deck.append(Card(1, 'jokers'))

#Exercise 18-2.
#Write a Deck method named sort that uses the list method sort to sort the cards in a
#Deck . sort uses the __cmp__ method we defined to determine sort order.

class Card(object):
  def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
  
  def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
  
  def __cmp__(self, other):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return cmp(t1,t2)

class Deck(object):
  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)


  def __str__(self):
    res = []
    for card in self.cards:
      res.append(str(card))
    return '\n'.join(res)


  def pop_card(self):
    return self.cards.pop()
  
  def add_card(self, card):
    self.cards.append(card) 

  def shuffle(self):
    random.shuffle(self.cards)
  
  def sort(self):
    self.cards.sort()

c1=Card(1,13)
c2=Card(2,3)
print(c1)
print(c2)

d1=Deck()
print(d1)
d1.add_card(c1)
print(d1)
d1.sort()
print(d1)

#Exercise 18-3.
#Write a Deck method called deal_hands that takes two parameters, the number of hands
#and the number of cards per hand, and that creates new Hand objects, deals the appro
#priate number of cards per hand, and returns a list of Hand objects.

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


  def deal_hands(self,no_of_hands,no_of_cards_per_hand):
      hands=[]
      for i in range(no_of_hands):
        hand=Hand("hand : %d"%(i))
        for j  in range(no_of_cards_per_hand):
            card=self.pop_card()
            hand.cards.append(card)
        hands.append(hand)
      return(hands)




class Hand(Deck):
  def __init__(self, label=''):
    self.cards = []
    self.label = label
  
  def __str__(self):
    print(self.label)
    for card in self.cards:
        print(card)

  def move_cards(self, hand, num):
    for i in range(num):
      hand.add_card(self.pop_card())


def find_defining_class(obj, meth_name):
  for ty in type(obj).mro():
    if meth_name in ty.__dict__:
      return ty



d1=Deck()
l=d1.deal_hands(3,10)
print(l)

for h in l:
    print(find_defining_class(h,'move_cards'))

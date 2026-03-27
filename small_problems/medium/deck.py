"""
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    
The Deck class should provide a draw method to deal one card. 
The Deck should be shuffled when it is initialized. If no more cards 
remain when draw is called, the method should generate a new set of 
52 shuffled cards, then deal one card from the new cards.


"""
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._deck = self._create_deck()

    def _create_deck(self):
        deck = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        random.shuffle(deck)
        return deck
        
    def draw(self):
        if not self._deck:
            self._deck = self._create_deck()
        return self._deck.pop()

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
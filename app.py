import random

# REQUIREMENTS:
# 4 classes, at least 2 attributes each...? and 2 methods that modify attributes
# at least one shows composition, being composed of other objects.
# design diagram that shows an overview of all classes that make up the system, show relationships between classes
# at least one class inherits from another class and overrides at least one superclass method.

# card class:
# attributes suit, value
# methods show()
# challenge color attribute
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

    # def color()
    # calculate color based on suit
    # may not need this since suit stays one of 2 colors, can put color in suit


# drawnCard = Card("Hearts", 8, "red")
# drawnCard.show()

# deck class:
# attributes cards(list)
# methods create_deck()
# challenges? deal() shuffle()

class Deck(Card):
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for suit in suits:
            for value in values:
                new_card = Card(suit, value)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        hand = random.sample(self.cards, 8)
        # instead of 8 use draw parameter then when u call draw enter amount?
        for card in hand:
            card.show()


# this prints all the objects DONT USE
# print(card_deck.cards)


# card_deck.shuffle()
# this shows all the cards in order


# Player class and its the one holding the hand, can play game.
# game class? need 4 classes
class Player(Deck):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        self.hand.append(deck.drawCard())
        return self
    # def drawCard(self):
    #     return self.cards.pop()

    def showHand(self):
        for card in self.hand:
            card.show()

card_deck = Deck()
# for card in card_deck.cards:
#     card.show()
print("Please take your hand:")
card_deck.shuffle()
card_deck.deal()

print("Jay")

jay = Player("Jay")
jay.showHand()
jay.drawCard()
jay.showHand()
import random

# card class:
# attributes suit, value
# methods show()
# challenge color attribute
class Card:
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

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

        for suit in suits:
            for value in range(1,14):
                new_card = Card(suit, value)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        hand = random.sample(self.cards, 8)
        # instead of 8 use draw parameter then when u call draw enter amount?
        for card in hand:
            card.show()
print("begin")
card_deck = Deck()
# this prints all the objects DONT USE
# print(card_deck.cards)


# card_deck.shuffle()
print("next")

for card in card_deck.cards:
    card.show()
print("your hand")
card_deck.deal()

# Player class and its the one holding the hand, can play game.
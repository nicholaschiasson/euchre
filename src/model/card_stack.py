import random
class CardStack:
    def __init__(self, cards):
        self.cards = cards
    def shuffle(self):
        random.shuffle(self.cards)
    def take_card(self):
        if len(self.cards) < 1:
            return None
        card = self.cards[-1]
        self.cards = self.cards[:-1]
        return card
    def place_card(self, card):
        self.cards.append(card)

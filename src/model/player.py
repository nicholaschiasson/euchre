from model.card_stack import CardStack

class Player:
    def __init__(self):
        self.hand = CardStack([])
        self.is_dealer = False

    def deal_card(self, card):
        self.hand.place_card(card)

    def empty_hand(self):
        self.hand = CardStack([])

    def set_dealer(self, is_dealer):
        self.is_dealer = is_dealer

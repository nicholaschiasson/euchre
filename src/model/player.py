from ai.search.game_playing import *
from model.card import Card
from model.card_stack import CardStack

class Player:
    def __init__(self):
        self.hand = CardStack([])
        self.hand_priorities = []
        self.is_dealer = False
        self.points = 0
        self.search_alg = alphabeta
        self.valid_cards = []

    def choose_card(self):
        return self.take_card(len(self.hand.cards) - 1)

    def deal_card(self, card):
        self.hand.place_card(card)

    def empty_hand(self):
        self.hand = CardStack([])

    def order_up(self, trump):
        self.prioritize_hand(trump.suit)
        self.take_card(self.hand_priorities.index(min(self.hand_priorities)))
        self.deal_card(trump)

    def prioritize_hand(self, trump):
        self.hand_priorities = []
        for i, c in enumerate(self.hand.cards):
            self.hand_priorities.append(Card.get_card_value(c, trump))

    def set_dealer(self, is_dealer):
        self.is_dealer = is_dealer

    def take_card(self, card_index):
        card = self.hand.cards[card_index]
        del self.hand.cards[card_index]
        return card

    def update_valid_cards(self, round_suit):
        self.valid_cards = []
        for c in self.hand.cards:
            self.valid_cards.append(c.suit == round_suit)
        if not all(self.valid_cards):
            for i in range(len(self.valid_cards)):
                self.valid_cards[i] = True

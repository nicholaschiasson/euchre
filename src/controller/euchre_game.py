import random

from model.card import Card
from model.card_stack import CardStack
from model.player import Player
from view.euchre_app import EuchreApp

class Euchre:
    def __init__(self, user_player = False):
        self.view = EuchreApp("Euchre", self, user_player)
        self.players = []
        for i in range(4):
            self.players.append(Player())
        self.dealer = random.randrange(4)
        self.restart_trick()

    def restart_trick(self):
        self.dealer += 1
        for i, p in enumerate(self.players):
            p.set_dealer(i == self.dealer % len(self.players))
        self.deck = CardStack([])
        self.deck.place_card(Card.NineOfClubs)
        self.deck.place_card(Card.NineOfDiamonds)
        self.deck.place_card(Card.NineOfHearts)
        self.deck.place_card(Card.NineOfSpades)
        self.deck.place_card(Card.TenOfClubs)
        self.deck.place_card(Card.TenOfDiamonds)
        self.deck.place_card(Card.TenOfHearts)
        self.deck.place_card(Card.TenOfSpades)
        self.deck.place_card(Card.JackOfClubs)
        self.deck.place_card(Card.JackOfDiamonds)
        self.deck.place_card(Card.JackOfHearts)
        self.deck.place_card(Card.JackOfSpades)
        self.deck.place_card(Card.QueenOfClubs)
        self.deck.place_card(Card.QueenOfDiamonds)
        self.deck.place_card(Card.QueenOfHearts)
        self.deck.place_card(Card.QueenOfSpades)
        self.deck.place_card(Card.KingOfClubs)
        self.deck.place_card(Card.KingOfDiamonds)
        self.deck.place_card(Card.KingOfHearts)
        self.deck.place_card(Card.KingOfSpades)
        self.deck.place_card(Card.AceOfClubs)
        self.deck.place_card(Card.AceOfDiamonds)
        self.deck.place_card(Card.AceOfHearts)
        self.deck.place_card(Card.AceOfSpades)
        self.deck.shuffle()
        self.view.restart_trick()

    def deal(self):
        for i in range(4):
            self.players[(self.dealer + i + 1) % len(self.players)].empty_hand()
        for i in range(4):
            for j in range(random.randrange(2, 4)):
                self.players[(self.dealer + i + 1) % len(self.players)].deal_card(self.deck.take_card())
        for i in range(4):
            for j in range(5 - len(self.players[(self.dealer + i + 1) % len(self.players)].hand.cards)):
                self.players[(self.dealer + i + 1) % len(self.players)].deal_card(self.deck.take_card())

    def player_choose_card(self, player, card):
        pass

    def run(self):
        self.view.mainloop()

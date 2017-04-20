import time
import random

from model.card import Card
from model.card_stack import CardStack
from model.player import Player
from view.euchre_app import EuchreApp

class Euchre:
    class State:
        Dealing = 0

    def __init__(self, user_player = False):
        self.user_player = user_player
        self.view = EuchreApp("Euchre", self, user_player)
        self.players = []
        for i in range(4):
            self.players.append(Player())
        self.dealer = random.randrange(4)
        self.trump = ""
        self.round_suit = ""
        self.used_cards = []
        self.current_turn = self.dealer
        self.turns_left_in_round = 0
        self.cards_in_play = [0, 0, 0, 0]
        self.restart_trick()

    def restart_trick(self):
        self.dealer += 1
        self.current_turn = self.dealer
        for i, p in enumerate(self.players):
            p.empty_hand()
            p.points = 0
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
        self.view.restart_trick(self.dealer)

    def deal(self):
        self.turns_left_in_round = 0
        for p in self.players:
            p.empty_hand()
            p.points = 0
        for i in range(4):
            for j in range(random.randrange(2, 4)):
                self.players[(self.dealer + i + 1) % len(self.players)].deal_card(self.deck.take_card())
        for i in range(4):
            for j in range(5 - len(self.players[(self.dealer + i + 1) % len(self.players)].hand.cards)):
                self.players[(self.dealer + i + 1) % len(self.players)].deal_card(self.deck.take_card())
        trump_card = self.deck.take_card()
        self.trump = trump_card.suit
        self.used_cards = []
        self.players[self.dealer % len(self.players)].order_up(trump_card)
        self.view.deal(self.trump)
        for i, p in enumerate(self.players):
            p.prioritize_hand(self.trump)
            self.view.update_player_hand(p, i)
        self.view.after(1000, self.next_turn)

    def player_choose_card(self, player, card):
        self.view.deactivate_player_turn(self.players[self.current_turn], self.current_turn)
        chosen_card = self.players[self.current_turn].take_card(card)
        value = Card.get_card_value(chosen_card, self.trump, self.round_suit)
        self.end_turn(self.players[self.current_turn], self.current_turn, chosen_card, value)

    def next_turn(self):
        if self.turns_left_in_round < 1:
            self.cards_in_play = [0, 0, 0, 0]
            self.view.new_round()
            self.round_suit = ""
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.turns_left_in_round = (self.turns_left_in_round - 1) % len(self.players)
        self.view.update_current_player(str(self.current_turn + 1))
        for p in self.players:
            p.update_valid_cards(self.round_suit)
        if self.user_player and (self.current_turn == 0):
            self.view.activate_player_turn(self.players[0], 0)
        else:
            card = self.players[self.current_turn].choose_card(self.trump, self.round_suit, self.cards_in_play, self.players, self.current_turn)
            value = Card.get_card_value(card, self.trump, self.round_suit)
            self.end_turn(self.players[self.current_turn], self.current_turn, card, value)

    def end_turn(self, player, player_num, card, card_value):
        self.cards_in_play[player_num] = card_value
        self.used_cards.append(card)
        if self.round_suit == "":
            self.round_suit = card.suit
        self.view.player_play_card(player, player_num, card)
        if self.turns_left_in_round < 1 and all(self.cards_in_play):
            winner_ind = self.cards_in_play.index(max(self.cards_in_play))
            self.current_turn = winner_ind - 1
            self.players[winner_ind].points += 1
            self.view.update_player_points(self.players[winner_ind], winner_ind)
        if self.turns_left_in_round < 1 and len(player.hand.cards) < 1:
            self.view.game_over()
        else:
            self.view.after(1000, self.next_turn)

    def run(self):
        self.view.mainloop()

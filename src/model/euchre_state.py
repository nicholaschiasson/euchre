from model.card import Card

class EuchreState:
    def __init__(self, current_player, player_hands, player_valid_cards, player_points, cards_in_play, trump_suit, round_suit):
        self.current_player = current_player
        self.player_hands = player_hands
        self.player_valid_cards = player_valid_cards
        self.player_points = player_points
        self.cards_in_play = cards_in_play
        self.trump_suit = trump_suit
        self.round_suit = round_suit

    def get_adjacent_states(self):
        adj_states = []
        for i in range(len(self.player_hands[self.current_player]))[::-1]:
            if len(self.player_valid_cards) < 1 or self.player_valid_cards[self.current_player][i]:
                new_state = EuchreState(self.current_player, [h[:] for h in self.player_hands], [v[:] for v in self.player_valid_cards], self.player_points[:], self.cards_in_play[:], self.trump_suit, self.round_suit)
                card_taken = new_state.player_hands[new_state.current_player][i]
                if all(new_state.cards_in_play):
                    new_state.cards_in_play = [0, 0, 0, 0]
                    new_state.round_suit = card_taken.suit
                    for j, h in enumerate(new_state.player_hands):
                        new_state.player_valid_cards[j] = []
                        for c in h:
                            new_state.player_valid_cards[j].append(c.suit == new_state.round_suit)
                        if all(v == False for v in new_state.player_valid_cards[j]):
                            for k in range(len(new_state.player_valid_cards[j])):
                                new_state.player_valid_cards[j][k] = True
                new_state.cards_in_play[new_state.current_player] = Card.get_card_value(card_taken, new_state.trump_suit, new_state.round_suit)
                del new_state.player_hands[new_state.current_player][i]
                del new_state.player_valid_cards[new_state.current_player][i]
                new_state.current_player = (new_state.current_player + 1) % len(new_state.player_hands)
                if all(new_state.cards_in_play):
                    winner_ind = new_state.cards_in_play.index(max(new_state.cards_in_play))
                    new_state.current_player = winner_ind - 1
                    new_state.player_points[winner_ind] += 1
                adj_states.append(new_state)
        return adj_states

    @staticmethod
    def team_heuristic(state):
        state_ind = (state.current_player - 1) % len(state.player_hands)
        score = 0
        score += state.player_points[state_ind]
        score += state.player_points[(state_ind + 2) % len(state.player_hands)]
        score -= state.player_points[(state_ind + 1) % len(state.player_hands)]
        score -= state.player_points[(state_ind + 3) % len(state.player_hands)]
        return score

    @staticmethod
    def paranoid_heuristic(state):
        state_ind = (state.current_player - 1) % len(state.player_hands)
        score = 0
        score += state.player_points[state_ind]
        score -= state.player_points[(state_ind + 2) % len(state.player_hands)]
        score -= state.player_points[(state_ind + 1) % len(state.player_hands)]
        score -= state.player_points[(state_ind + 3) % len(state.player_hands)]
        return score

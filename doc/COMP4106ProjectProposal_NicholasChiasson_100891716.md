# COMP4106A Project Proposal
Nicholas Chiasson - 100891716

***

## Euchre

### Problem Domain
Euchre is a trick taking paired team based card game. To **very** briefly summarize my understanding of the game, each player is dealt 5 cards from a 24 card deck (regular 52 card deck with 2 through 8 rank cards omitted). A suit is then selected as the *trump* suit by a sequence of asking each player in clockwise order. Once *trump* is chosen, the round starts. A round consists of a number of *tricks* equating to the number of cards players were dealt. During a *trick*, each player puts down a card in clockwise order. Each player must play a card of the same suit as the card that the first player put down. If the player does not have a card of that suit, they can play any card in their hand. The player who played the highest card at the end wins the trick for their team. The highest card played in a trick can be overridden by the highest card played in the *trump* suit. Finally, the two highest value cards are the Right bower (jack of the *trump* suit) and the left bower (jack of the matching color as the right bower).

### Motivation For Problem
I think this game makes for a great learning experience in AI because it is very probability based and it is a team game. It is a very fun game to play, but rather complicated, so I figured it would be a great exercise to create an artificially intelligent opponent to practice against.

### AI Techniques
-   Intelligent game playing
    -   Min-max search
    -   Maximize payoff for team, minimize payoff for opponent team
-   Machine learning
    -   Part of the game involves knowing when it's best to make certain actions such as ordering up trump or playing a trick alone
    -   Must recognize when it's best to use better cards or worse cards based on what cards have been played so far

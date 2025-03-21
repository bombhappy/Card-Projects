from collections import deque

from Cards import Deck, Card, Player
from Poker import Poker, PokerPlayer

player_count = int(input("Let's play Poker! How many players will be playing? 2 - 9 players are allowed: "))

while player_count <= 1 or player_count >= 10:
    player_count = int(input("Error! Please enter the number of players between 2 to 9: "))
else:
    print(f"There are {player_count} players this game")

participating_players = []

for i in range(0, player_count):
    participating_players.append(PokerPlayer(i+1))

#Start of first hand
deck = Deck()
deck.shuffle()
game = Poker(deck, 2, 2, 1)
hands_at_table = deck.deal_cards(player_count, 2)

for j in range(0, player_count):
    participating_players[j].held_cards(hands_at_table[str(j)])

#Shifting list two over since the Small Blind gets dealt cards first, but left of Big Blind starts the round of betting
temp = deque(participating_players)
temp.rotate(-2)
participating_players = [*temp]

game.update_pot(participating_players[-1].bet(game.get_big_blind())) #Big Blind bet
game.update_pot(participating_players[-2].bet(game.get_small_blind())) #Small Blind bet

#Preflop starts with the person left of Big Blind
game.betting_round(participating_players)
#Evaluate if everyone is all in, otherwise continue to next street
game.deal_flop()

#Post flop, the person who starts the bet is the Small Blind
temp = deque(participating_players)
temp.rotate(2)
participating_players = [*temp]
game.betting_round(participating_players)
#Evaluate again
game.deal_turn()
game.betting_round(participating_players)
#Evaluate again
game.deal_river()
game.betting_round(participating_players)
#Players show card and evaluate strength of their hands












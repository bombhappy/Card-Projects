from Cards import SUITS, Card, Deck, Player
import random


class Poker:

    def __init__(self, deck, min_raise, big_blind, small_blind):
        self.deck = deck
        self.board = {}
        self.pot = [0]
        self.min_raise = min_raise
        self.big_blind = big_blind
        self.small_blind = small_blind
        self.highest_bet = big_blind
        self.no_skip_betting_round = True
        self.all_in_players = 0

    def update_pot(self, betting_amount): #how to handle side pots??????
        self.pot += betting_amount


    def betting_round(self, players):
        k = 0
        while k != len(players) or self.no_skip_betting_round:
            for player in players:
                action = player.act
                if action == 'check' or 'pass': #pass is when player already has gone all-in and forced to skip their turn
                    k += 1
                elif action == 'call':
                    k += 1
                    player_call = self.highest_bet - player.bet_in_pot
                    self.update_pot(player.bet(player_call))
                elif action == 'bet':
                    k = 0
                    bet_amount = 0
                    player_min_raise = self.highest_bet - player.bet_in_pot() + self.min_raise
                    while player_min_raise >= bet_amount > player.chip_count():
                        bet_amount = input(f'Please enter a bet from {player_min_raise} to {player.chip_count()}: ')
                    self.update_pot(player.bet(bet_amount))
                    self.highest_bet = player.bet_in_pot
                elif action == 'all-in':
                    k+= 1
                    self.update_pot(player.bet(player.chip_count))
                    self.all_in_players += 1
                elif action == 'fold':
                    del player
                else:
                    pass
                if k == len(players):  #if count has gone through all players, then proceed to next street
                    break
            if self.all_in_players == len(players)-1: #skip all betting rounds and show all player's cards
                self.no_skip_betting_round = False


    def distribute_pot(self, players):
        current_pot = self.pot
        lowest_bet = min(players.bet_in_pot) #Ask about this?
        #for player in players: #Find player with the lowest bet that has not folded
            #if player.get_bet_in_pot < current_pot:
                #current_pot = player.get_bet_in_pot
        strongest_hand = max(players.hand_strength)
        winners = 0
        winning_players = []
        for player in players: #check if pot needs to be split
            if player.get_hand_strength == strongest_hand: #and nothing in list
                winning_players.append(player)
                winners += 1
            elif player.get_hand_strength == strongest_hand:
                #winning_players[0] = player
                pass

    def deal_flop(self):
        del self.deck[0] #burn card
        for i in range(0,3): #deal 3 cards
            self.board[i] = self.deck.pop(0)

    def deal_turn(self):
        del self.deck[0] #burn card
        self.board[3] = self.deck.pop(0)

    def deal_river(self):
        del self.deck[0] #burn card
        self.board[4] = self.deck.pop(0)

    def check_hand(self, hand):
        temp_board = self.board.copy()
        temp_board.extend(hand)
        sorted_cards = sorted(temp_board)
        #is_royal_flush = [10, 11, 12, 13, 14]
        #is_straight_flush
        #is_quads
        #is_full_house
        #is_flush = len(set(sorted_cards.suits for card in sorted_cards)) == 1
        #is_straight
        #is_wheel_straight = [14, 2, 3, 4, 5] #5 high straight
        #is_triple
        #is_two_pair
        #is_pair
        #is_high_card

    def get_big_blind(self):
        return self.big_blind

    def get_small_blind(self):
        return self.small_blind

class PokerPlayer(Player):

    def __init__(self, player_num):
        super().__init__(player_num)
        self.chips = (input('How many chips would you like to start with? 20-50 BB are allowed: '))
        while int(self.chips) < 20 or int(self.chips) > 50:
            self.chips = int(input('Error! Please enter a number between 20 and 50: '))
        self.bet_in_pot = 0
        self.hand_strength = 0
        self.result = 0
        self.live = True #check if player has folded or not

    def bet(self, bet_amount):
        self.chips = self.chips - bet_amount
        self.bet_in_pot += bet_amount
        return bet_amount

    def act(self, highest_bet, min_raise):
        total_player_chips = self.chips + self.bet_in_pot
        if self.bet_in_pot == highest_bet and self.chips >= min_raise:
            action = input('Would you like to check, bet, or fold? ') #could also warn player not to fold if they can check
            while action != 'check' or 'bet' or 'fold': #Can use a function that does not need action to be case sensitive
                action = input('Sorry, wrong input. Would you like to check, bet or fold? ')
            return action
        elif self.bet_in_pot < highest_bet and total_player_chips > (highest_bet + min_raise):
            action = input('Would you like to call, bet, or fold? ')
            while action != 'call' or 'bet' or 'fold':
                action = input('Sorry, wrong input. Would you like to call, bet or fold? ')
            return action
        elif total_player_chips < highest_bet:
            action = input('Would you like to go all-in, or fold?')
            while action != 'all-in' or 'fold':
                action = input('Sorry, wrong input. Would you like to go all-in, fold? ')
            return action
        elif self.chips == 0: #Player has already gone all-in and is still covered by other players
            return 'pass'

    def set_hand_strength(self, hand_strength):
        self.hand_strength = hand_strength

    def add_winnings(self, winnings):
        self.chips += winnings

















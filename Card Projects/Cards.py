import random


RANKS = {"Ace": 14, "Deuce": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13}
SUITS = ["Spades", "Clubs", "Diamonds", "Hearts"]

class Card:

    def __init__(self, rank, suit):
        self.rank = rank #ace, two, three, etc
        self.suit = suit #clubs, spades, diamonds, hearts

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __lt__(self, other):
        return RANKS[self.rank] < RANKS[other.rank]

    def __gt__(self, other):
        return RANKS[self.rank] > RANKS[other.rank]

    def rank(self):
        return self.rank

    def suit(self):
        return self.suit

class Deck:

    def __init__(self):
        self.deck_of_cards = []

        for rank in RANKS:
            for suit in SUITS:
                self.deck_of_cards.append(Card(rank,suit))

    def __str__(self):
        self.deck = ', '.join([str(card) for card in self.deck_of_cards])
        return self.deck

    def shuffle(self):
        return random.shuffle(self.deck_of_cards)

    def deal_cards(self, num_players, hand_size):
        hands = {}

        for i in range(0, hand_size):

            for player_num in range(0, num_players): #Gives cards to players around the table
                if str(player_num) in hands.keys():
                    hands[str(player_num)].append(self.deck_of_cards.pop(0))

                else:
                    hands[str(player_num)] = [self.deck_of_cards.pop(0)]


        return hands


class Player:

    def __init__(self, player_num):
        self.hand = {}
        self.player_number = player_num
        self.name = input(f"Name of Player {player_num}: ")

    def __str__(self):
        str_hand = ', '.join([str(card) for card in self.hand])
        return f'{self.name} has {str_hand}'
    def __repr__(self):
        str_hand = ', '.join([str(card) for card in self.hand])
        return f'{self.name} has {str_hand}'

    def held_cards(self, dealt_cards): #list of cards
        self.hand = dealt_cards







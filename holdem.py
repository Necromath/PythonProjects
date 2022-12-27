// write me a program that plays a game of no limit texas holdem poker
// against a computer opponent
// the program should take a command line argument for the number of players
// and the number of chips each player starts with
// the program should then play a game of texas holdem poker
// and print out the results of the game
// the program should also print out the cards in each players hand
// and the cards on the board
// the program should also print out the final chip counts for each player
// the program should also print out the winner of the game


import sys
import random
import itertools

# Path: holdem.py
# Class: Card
# Description: A class that represents a playing card
class Card:
    # Path: holdem.py
    # Function: __init__
    # Description: The constructor for the Card class
    # Parameters: self, the card's rank, the card's suit
    # Returns: nothing
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Path: holdem.py
    # Function: __str__
    # Description: The string representation of a card
    # Parameters: self
    # Returns: the string representation of the card
    def __str__(self):
        return self.rank + self.suit

    # Path: holdem.py
    # Function: __eq__
    # Description: The equality operator for a card
    # Parameters: self, the other card
    # Returns: true if the cards are equal, false otherwise
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    # Path: holdem.py
    # Function: __ne__
    # Description: The inequality operator for a card
    # Parameters: self, the other card
    # Returns: true if the cards are not equal, false otherwise
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Path: holdem.py
    # Function: __lt__
    # Description: The less than operator for a card
    # Parameters: self, the other card
    # Returns: true if self is less than other, false otherwise
    def __lt__(self, other):
        return self.rank < other.rank

    # Path: holdem.py
    # Function: __gt__
    # Description: The greater than operator for a card
    # Parameters: self, the other card
    # Returns: true if self is greater than other, false otherwise
    def __gt__(self, other):
        return self.rank > other.rank

    # Path: holdem.py
    # Function: __le__
    # Description: The less than or equal to operator for a card
    # Parameters: self, the other card
    # Returns: true if self is less than or equal to other, false otherwise
    def __le__(self, other):
        return self.rank <= other.rank

    # Path: holdem.py
    # Function: __ge__
    # Description: The greater than or equal to operator for a card
    # Parameters: self, the other card
    # Returns: true if self is greater than or equal to other, false otherwise
    def __ge__(self, other):
        return self.rank >= other.rank

    # Path: holdem.py
    # Function: get_rank
    # Description: Gets the rank of the card
    # Parameters: self
    # Returns: the rank of the card
    def get_rank(self):
        return self.rank

    # Path: holdem.py
    # Function: get_suit
    # Description: Gets the suit of the card
    # Parameters: self
    # Returns: the suit of the card
    def get_suit(self):
        return self.suit

# Path: holdem.py
# Class: Deck
# Description: A class that represents a deck of playing cards
class Deck:

    # Path: holdem.py
    # Function: __init__
    # Description: The constructor for the Deck class
    # Parameters: self
    # Returns: nothing
    def __init__(self):
        self.cards = []
        self.build()

    # Path: holdem.py
    # Function: build
    # Description: Builds the deck of cards
    # Parameters: self
    # Returns: nothing
    def build(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suits = ["C", "D", "H", "S"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    # Path: holdem.py
    # Function: shuffle
    # Description: Shuffles the deck of cards
    # Parameters: self
    # Returns: nothing
    def shuffle(self):
        random.shuffle(self.cards)

    # Path: holdem.py
    # Function: draw
    # Description: Draws a card from the deck
    # Parameters: self
    # Returns: the card that was drawn
    def draw(self):
        return self.cards.pop()

    # Path: holdem.py
    # Function: __str__
    # Description: The string representation of the deck
    # Parameters: self
    # Returns: the string representation of the deck
    def __str__(self):
        return str(self.cards)

# Path: holdem.py
# Class: Hand
# Description: A class that represents a hand of playing cards
class Hand:

    # Path: holdem.py
    # Function: __init__
    # Description: The constructor for the Hand class
    # Parameters: self
    # Returns: nothing
    def __init__(self):
        self.cards = []

    # Path: holdem.py
    # Function: add_card
    # Description: Adds a card to the hand
    # Parameters: self, the card to add
    # Returns: nothing
    def add_card(self, card):
        self.cards.append(card)

    # Path: holdem.py
    # Function: get_cards
    # Description: Gets the cards in the hand
    # Parameters: self
    # Returns: the cards in the hand
    def get_cards(self):
        return self.cards

    # Path: holdem.py
    # Function: __str__
    # Description: The string representation of the hand
    # Parameters: self
    # Returns: the string representation of the hand
    def __str__(self):
        return str(self.cards)

# Path: holdem.py
# Class: Player
# Description: A class that represents a player in a game of poker
class Player:

    # Path: holdem.py
    # Function: __init__
    # Description: The constructor for the Player class
    # Parameters: self, the player's name
    # Returns: nothing
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    # Path: holdem.py
    # Function: get_name
    # Description: Gets the name of the player
    # Parameters: self
    # Returns: the name of the player
    def get_name(self):
        return self.name

    # Path: holdem.py
    # Function: get_hand
    # Description: Gets the hand of the player
    # Parameters: self
    # Returns: the hand of the player
    def get_hand(self):
        return self.hand

    # Path: holdem.py
    # Function: __str__
    # Description: The string representation of the player
    # Parameters: self
    # Returns: the string representation of the player
    def __str__(self):
        return self.name + ": " + str(self.hand)

# Path: holdem.py
# Class: Game
# Description: A class that represents a game of poker
class Game:

    # Path: holdem.py
    # Function: __init__
    # Description: The constructor for the Game class
    # Parameters: self, the number of players in the game
    # Returns: nothing
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = Hand()
        self.pot = 0
        self.bet = 0
        self.bets = []
        self.folded = []
        self.winner = None
        self.winning_hand = None
        self.winning_hand_type = None
        self.winning_hand_rank = None
        self.winning_hand_kickers = None
        self.winning_hand_kicker_ranks = None
        self.winning_hand_kicker_suits = None
        self.winning_hand_kicker_ranks_str = None
        self.winning_hand_kicker_suits_str = None
        self.winning_hand_kicker_ranks_str_sorted = None
        self.winning_hand_kicker_suits_str_sorted = None

    def get_num_players(self):
        return self.num_players

    def get_players(self):
        return self.players

    def get_deck(self):
        return self.deck

    def get_community_cards(self):
        return self.community_cards

    def get_pot(self):
        return self.pot

    def get_bet(self):
        return self.bet

    def get_bets(self):
        return self.bets

    def get_folded(self):
        return self.folded

    def get_winner(self):
        return self.winner

    def get_winning_hand(self):
        return self.winning_hand

    def get_winning_hand_type(self):
        return self.winning_hand_type

    def get_winning_hand_rank(self):
        return self.winning_hand_rank

    def get_winning_hand_kickers(self):
        return self.winning_hand_kickers

    def get_winning_hand_kicker_ranks(self):
        return self.winning_hand_kicker_ranks

    def get_winning_hand_kicker_suits(self):
        return self.winning_hand_kicker_suits

    def get_winning_hand_kicker_ranks_str(self):
        return self.winning_hand_kicker_ranks_str

    def get_winning_hand_kicker_suits_str(self):
        return self.winning_hand_kicker_suits_str

    def get_winning_hand_kicker_ranks_str_sorted(self):
        return self.winning_hand_kicker_ranks_str_sorted

    def get_winning_hand_kicker_suits_str_sorted(self):
        return self.winning_hand_kicker_suits_str_sorted

    def set_num_players(self, num_players):
        self.num_players = num_players

    def set_players(self, players):
        self.players = players

    def set_deck(self, deck):
        self.deck = deck

    def set_community_cards(self, community_cards):
        self.community_cards = community_cards

    def set_pot(self, pot):
        self.pot = pot

    def set_bet(self, bet):
        self.bet = bet

    def set_bets(self, bets):
        self.bets = bets

    def set_folded(self, folded):
        self.folded = folded

    def set_winner(self, winner):
        self.winner = winner

    def set_winning_hand(self, winning_hand):
        self.winning_hand = winning_hand

    def set_winning_hand_type(self, winning_hand_type):
        self.winning_hand_type = winning_hand_type

    def set_winning_hand_rank(self, winning_hand_rank):
        self.winning_hand_rank = winning_hand_rank

    def set_winning_hand_kickers(self, winning_hand_kickers):
        self.winning_hand_kickers = winning_hand_kickers

    def set_winning_hand_kicker_ranks(self, winning_hand_kicker_ranks):
        self.winning_hand_kicker_ranks = winning_hand_kicker_ranks

    def set_winning_hand_kicker_suits(self, winning_hand_kicker_suits):
        self.winning_hand_kicker_suits = winning_hand_kicker_suits

    def set_winning_hand_kicker_ranks_str(self, winning_hand_kicker_ranks_str):
        self.winning_hand_kicker_ranks_str = winning_hand_kicker_ranks_str

    def set_winning_hand_kicker_suits_str(self, winning_hand_kicker_suits_str):
        self.winning_hand_kicker_suits_str = winning_hand_kicker_suits_str

    def set_winning_hand_kicker_ranks_str_sorted(self, winning_hand_kicker_ranks_str_sorted):
        self.winning_hand_kicker_ranks_str_sorted = winning_hand_kicker_ranks_str_sorted

    def set_winning_hand_kicker_suits_str_sorted(self, winning_hand_kicker_suits_str_sorted):
        self.winning_hand_kicker_suits_str_sorted = winning_hand_kicker_suits_str_sorted

    # Path: holdem.py
    # Function: add_player
    # Description: Adds a player to the game
    # Parameters: self, the player to add
    # Returns: nothing
    def add_player(self, player):
        self.players.append(player)

    # Path: holdem.py
    # Function: deal
    # Description: Deals the cards to the players
    # Parameters: self
    # Returns: nothing
    def deal(self):
        for i in range(2):
            for player in self.players:
                player.add_card(self.deck.deal())

    # Path: holdem.py
    # Function: deal_flop
    # Description: Deals the flop to the community cards
    # Parameters: self
    # Returns: nothing
    def deal_flop(self):
        for i in range(3):
            self.community_cards.add_card(self.deck.deal())

    # Path: holdem.py
    # Function: deal_turn
    # Description: Deals the turn to the community cards
    # Parameters: self
    # Returns: nothing
    def deal_turn(self):
        self.community_cards.add_card(self.deck.deal())

    # Path: holdem.py
    # Function: deal_river
    # Description: Deals the river to the community cards
    # Parameters: self
    # Returns: nothing
    def deal_river(self):
        self.community_cards.add_card(self.deck.deal())

    # Path: holdem.py
    # Function: deal_community_cards
    # Description: Deals the community cards
    # Parameters: self
    # Returns: nothing
    def deal_community_cards(self):
        self.deal_flop()
        self.deal_turn()
        self.deal_river()

    # Path: holdem.py
    # Function: get_player
    # Description: Gets a player from the list of players
    # Parameters: self, the player to get
    # Returns: the player
    def get_player(self, player):
        return self.players[player]

    # Path: holdem.py
    # Function: get_player_by_name
    # Description: Gets a player from the list of players by name
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_name(self, player_name):
        for player in self.players:
            if player.get_name() == player_name:
                return player

    # Path: holdem.py
    # Function: get_player_by_id
    # Description: Gets a player from the list of players by id
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_id(self, player_id):
        for player in self.players:
            if player.get_id() == player_id:
                return player

    # Path: holdem.py
    # Function: get_player_by_seat
    # Description: Gets a player from the list of players by seat
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_seat(self, seat):
        for player in self.players:
            if player.get_seat() == seat:
                return player

    # Path: holdem.py
    # Function: get_player_by_card
    # Description: Gets a player from the list of players by card
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_card(self, card):
        for player in self.players:
            if player.has_card(card):
                return player

    # Path: holdem.py
    # Function: get_player_by_hand
    # Description: Gets a player from the list of players by hand
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand(self, hand):
        for player in self.players:
            if player.has_hand(hand):
                return player

    # Path: holdem.py
    # Function: get_player_by_cards
    # Description: Gets a player from the list of players by cards
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_cards(self, cards):
        for player in self.players:
            if player.has_cards(cards):
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_type
    # Description: Gets a player from the list of players by hand type
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_type(self, hand_type):
        for player in self.players:
            if player.get_hand_type() == hand_type:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_type_str
    # Description: Gets a player from the list of players by hand type string
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_type_str(self, hand_type_str):
        for player in self.players:
            if player.get_hand_type_str() == hand_type_str:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_type_str_sorted
    # Description: Gets a player from the list of players by hand type string sorted
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_type_str_sorted(self, hand_type_str_sorted):
        for player in self.players:
            if player.get_hand_type_str_sorted() == hand_type_str_sorted:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_rank
    # Description: Gets a player from the list of players by hand rank
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_rank(self, hand_rank):
        for player in self.players:
            if player.get_hand_rank() == hand_rank:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_rank_sorted
    # Description: Gets a player from the list of players by hand rank sorted
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_rank_sorted(self, hand_rank_sorted):
        for player in self.players:
            if player.get_hand_rank_sorted() == hand_rank_sorted:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_rank_str
    # Description: Gets a player from the list of players by hand rank string
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_rank_str(self, hand_rank_str):
        for player in self.players:
            if player.get_hand_rank_str() == hand_rank_str:
                return player

    # Path: holdem.py
    # Function: get_player_by_hand_rank_str_sorted
    # Description: Gets a player from the list of players by hand rank string sorted
    # Parameters: self, the player to get
    # Returns: the player
    def get_player_by_hand_rank_str_sorted(self, hand_rank_str_sorted):
        for player in self.players:
            if player.get_hand_rank_str_sorted() == hand_rank_str_sorted:
                return player
   

    # Path: holdem.py
    # Function: hand_rank
    # Description: Sets the rank of each possible hand in Poker
    # Parameters: 

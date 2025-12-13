from card_mapper import CardMapper
import random


SUITS = ["♣", "♦", "♥", "♠"]

class Referee:
    def __init__(self):
        self.players = {"player1":[True,True,True,True],
                        "player2":[True,True,True,True],
                        "player3":[True,True,True,True],
                        "player4":[True,True,True,True]
                        }
        self.trump=None
        self.trump_suit=None
        self.trump_was_played = False
                
    def receive_card(self):
        card = input("card:")
        return card

    def round(self, first_player):
        for _ in range(10):
            if _==0:
                self.get_trump()
            for i in range(4):
                card_number = self.receive_card()
                if card_number == self.trump:
                    self.trump_was_played = True
                card_suit = CardMapper.get_card_suit(card_number)
                this_player = i + first_player
                if this_player > 4:
                    this_player = this_player%4
                player = str("player"+str(this_player))
                card_suit_index = SUITS.index(card_suit)
                if self.players.get(player)[card_suit_index]== False:
                    return False
                if i == 0:
                    round_suit = card_suit
                    print(player, card_suit, round_suit, "\n")
                    round_suit_index = SUITS.index(round_suit)
                elif 0<i<3: 
                    print(player, card_suit, round_suit, "\n")
                    if card_suit != round_suit:
                        print("Já não tenho\n")
                        self.players[player][round_suit_index]=False
                else:
                    print(player, card_suit, round_suit, "\n")
                    if card_suit != round_suit:
                        if round_suit == self.trump_suit:
                            if self.trump_was_played == False:
                                return False
                        print("Já não tenho\n")
                        self.players[player][round_suit_index]=False
                    
        return True
    
    def game(self):
        while True:
            for i in range(4):
                first_player = i+1
                self.reset_players()
                if self.round(first_player) == False:
                    print("RENUNCIA")
                    continue

    def reset_players(self):
        self.players = {"player1":[True,True,True,True],
                        "player2":[True,True,True,True],
                        "player3":[True,True,True,True],
                        "player4":[True,True,True,True]
                        }
        self.trump_was_played = False
        self.trump=None
        self.trump_suit=None
        
    def get_trump(self):
        self.trump = self.receive_card()
        self.trump_suit = CardMapper.get_card_suit(self.trump)



r = Referee()
r.game()
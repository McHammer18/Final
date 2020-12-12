"""
Morgan Christensen

Black Jack: this program is black jack emulator that uses a gui to interact with
the player and allow them to place bets

11/28/20
"""
from tkinter import *
from BlackJack.design import *
from BlackJack.Card import *
from BlackJack.Dealer import *
MAX = 21

class Game(Card, DealerAI):
    def __init__(self, name, suit, value, is_displayed, dealer_score, player_score, deck, master, player_button_frame,player_cards_frame,
                 player_card1_label, player_card2_label, dealer_card1_label, dealer_card2_label,player_score_label,
                 dealer_score_label, dealer_cards_frame, player_busted_message, dealer_busted_message, deal_results_frame):
        super().__init__(name, suit, value, is_displayed)
        super().__init__(dealer_score, player_score)
        self.deck = deck  # Card Instances
        self.master = master  # The main windows
        self.player_game_options_frame = player_button_frame
        self.player_cards_frame = player_cards_frame  # Player frame that cards are in
        self.player_card1_label = player_card1_label  # Players first card label
        self.player_card2_label = player_card2_label  # Players second card label
        self.dealer_card1_label = dealer_card1_label  # Dealer first card label
        self.dealer_card2_label = dealer_card2_label  # Dealer second card label , this is going to be hidden in the first stage
        self.player_score_label = player_score_label  # Player Score
        self.dealer_score_label = dealer_score_label  # Dealer Score
        self.dealer_cards_frame = dealer_cards_frame  # Dealer cards Frame
        self.player_busted_message = player_busted_message  # Busted case for player
        self.dealer_busted_message = dealer_busted_message  # Busted case for dealer
        self.deal_results_frame = deal_results_frame  # results of the gameplay

        ########
        # New indexed Parameters to be indexed throughout the deal:
        ########
        self.player_cards = []
        self.dealer_cards = []

        ########
        # Methods to Execute after Initialize
        ########
        self.enable_buttons(
            buttons=['stand', 'hit', 'double'])  # referring to the buttons that ALWAYS have to be enabled

    #####
    # This function will enable the buttons that are required on order to play
    ######
    def enable_buttons(self, buttons):
        for button in self.player_game_options_frame.winfo_children():
            if button.winfo_name() in buttons:
                button.configure(state='normal')  # set the state from disabled to normal

    ######
    # Dynamic Method that changes from card to card
    # Made in order to get a new card for player and dealer
    # This Function responsible also to update the score of the player or dealer after the card
    # By default it is for the player
    ######
    def get_card(self, card_label, display=True, is_player=True):
        card = Card.shuffle_deck(self.deck)
        card_image = Card.get_card_image(card)

        if is_player:
            self.player_cards.append(card)

        if not is_player:
            self.dealer_cards.append(card)

        print(card.name)
        print(card.value)

        if display:
            self.display_card(card_label=card_label, card_image=card_image)
        else:
            # Change the is_displayed value from automatic True to False
            card.is_displayed = False
            hidden_card = Card.hidden_card()
            card_label.configure(image=hidden_card)
            card_label.image = hidden_card

        # Remove from the deck the selected card:
        self.deck.remove(card)
        print(f"You got {len(self.deck)} cards in deck, because now {card.name} is taken!")

        return card

    def display_card(self, card_label, card_image):
        card_label.configure(image=card_image)
        card_label.image = card_image

    def deal_player(self):
        card1 = self.get_card(self.player_card1_label)
        card2 = self.get_card(self.player_card2_label)

    #########
    # This function would triggered when player hits the hit button
    # This will give him another card
    # And will check if the player is busted by the end of the hit
    #########
    def hit(self, dealer_card_2=None, is_player=True):
        # Bring with hidden card by default (Maybe its the dealer ? )
        hidden_card = Card.hidden_card()

        if is_player:
            # Create new label with image right there
            new_card = Label(self.player_cards_frame, image=hidden_card, bg=background_color)
            new_card.pack(side=RIGHT)

            # Call the get_card function with setting up the image of the card:
            card = self.get_card(card_label=new_card)
            self.update_player_score_after_hit()

            # Handle busted:
            if self.player_is_busted():
                self.player_busted_message.pack(side=TOP, anchor='nw')
                self.finish_player_turn(dealer_card_2=dealer_card_2)

            return card

        # If its the dealer and not the player:
        else:
            new_card = Label(self.dealer_cards_frame, image=hidden_card, bg=background_color)
            new_card.pack(side=LEFT)

            card = self.get_card(card_label=new_card, is_player=False)
            self.update_dealer_score_after_hit()

            return card

    #########
    # Get players current score:
    #########
    def get_player_score(self):
        value = 0
        for card in self.player_cards:
            value += card.value
        return str(value)

    #########
    # Get dealers current score:
    #########
    def get_dealer_score(self):
        value = 0
        for card in self.dealer_cards:
            if card.is_displayed:
                value += card.value
        return str(value)

    ##########
    # This will set the score board when the user clicks deal:
    ##########

    def set_scoreboard(self):
        self.player_score_label.configure(text=f'Player Score: {self.get_player_score()}')
        self.dealer_score_label.configure(text=f'Dealer Score: {self.get_dealer_score()}')

    #######
    # Update player score after the hit
    #######
    def update_player_score_after_hit(self):
        self.player_score_label.configure(text=f'Player Score: {self.get_player_score()}')

    #######
    # Update dealer score after the hit
    #######
    def update_dealer_score_after_hit(self):
        self.dealer_score_label.configure(text=f'Dealer Score: {self.get_dealer_score()}')

    #######
    # Clean table in given frames children
    #######
    @staticmethod
    def clean_table(frames):
        for frame in frames:
            # get all frames children:
            delete_from = frame.winfo_children()

            for widget in delete_from:
                if not str(widget.winfo_name()).startswith('dealcard'):
                    widget.forget()

    ########
    # Check if Player is busted
    # This check will run on each hit, so we know if to continue or not
    ########
    def player_is_busted(self):
        if int(self.get_player_score()) > 21:
            return True
        else:
            return False

    ########
    # Check if Dealer is busted
    # This check will run on each hit, so we know if to continue or not
    ########
    def dealer_is_busted(self):
        if int(self.get_dealer_score()) > 21:
            return True
        else:
            return False

    #########
    # This will handle situations after player finished
    # Important first of all to display the hidden card of dealer
    #########
    def stand_or_busted(self, dealer_card_2):
        # Get its images
        card_image = Card.get_card_image(dealer_card_2)
        # Display the Card
        self.display_card(self.dealer_card2_label, card_image)
        # Change the property of is_displayed
        dealer_card_2.is_displayed = True

        # update the score of dealer:
        self.update_dealer_score_after_hit()


    #########
    # Handles what happens after player clicked stand or Busted
    #########
    def finish_player_turn(self, dealer_card_2):
        for button in self.player_game_options_frame.winfo_children():
            button.configure(state='disabled')
            button.unbind('<Button-1>')

        # Display the dealers second card and update its score
        self.stand_or_busted(dealer_card_2)

        # Start dealer Automatic Play
        dealer = DealerAI(dealer_score=self.get_dealer_score())
        while dealer.is_hit():
            self.hit(is_player=False)
            # Update the DealerAI about the new dealer score after each hit
            dealer.dealer_score = self.get_dealer_score()
            if self.dealer_is_busted():
                self.dealer_busted_message.pack(side=LEFT)

        # Decide who won the deal
        self.decider()

    #######
    # This Method is going to decide who is the winner
    #######
    def decider(self):
        player_score = int(self.get_player_score())
        dealer_score = int(self.get_dealer_score())

        result = Label(self.deal_results_frame, text='', font=font_large, bg=background_color)
        result.pack(fill=BOTH, side=TOP)

        player_won_text = 'YOU WON!'
        dealer_won_text = 'DEALER WINS!'
        tied_text = 'Tie!'
        both_busted = 'BOTH BUSTED!'

        if self.player_is_busted() and self.dealer_is_busted():
            result.configure(fg='#FFFFFF', text=both_busted)

        if self.player_is_busted() and not self.dealer_is_busted():
            result.configure(fg="#FF0000", text=dealer_won_text)

        if not self.player_is_busted() and self.dealer_is_busted():
            result.configure(fg="#00FF00", text=player_won_text)

        if not self.player_is_busted() and not self.dealer_is_busted():
            if player_score > dealer_score:
                result.configure(fg="#00FF00", text=player_won_text)
            elif player_score < dealer_score:
                result.configure(fg="#FF0000", text=dealer_won_text)
            else:
                result.configure(fg='#FFFFFF', text=tied_text)

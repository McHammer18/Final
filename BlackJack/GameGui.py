"""
Morgan Christensen

Black Jack GUI: This is the Gui file that handles creating the interface to interact with the
player

12/07/20
"""
from tkinter import *
from BlackJack.design import *
from BlackJack.Card import *
from BlackJack.Game import *

from PIL import ImageTk, Image

game = Tk()
game.title("Black Jack")
game.configure(bg=background_color)

# Frames#
# Players frame that hold the card frame and the options frame
pf = Frame(game, bg = background_color, ** hightlight_frame_with_white)
pf.grid(row=2, column=0, columnspan=3)

# cards
pcf = Frame(pf, bg=background_color)
pcf.grid(row=0, column=0)
l = Label(pf, text="Hello")
l.grid()
# Sets the image of the first card face down
p_card1 = Card.hidden_card()
p_card1_label = Label(pcf, image=p_card1, bg=background_color, name='dealcard1_player')
p_card1.pack(side=RIGHT)
p_card2 = Card.hidden_card()
p_card2_label = Label(pcf, image = p_card2, bg = background_color,name = 'dealcard2_player')
p_card2_label.pack(side=RIGHT)

# buttons
pbf = Frame(pf, bg=background_color)
pbf.grid(row=1, column=0)
hit = Button(pbf, text="Hit", **button_args, state=DISABLED, name='hit')
stand = Button(pbf, text="Stand", **button_args, state=DISABLED, name='stand')
deal = Button(pbf, text = 'DEAL', **button_args, bg = "green")

deal.grid(row=0, column=0)
hit.grid(row=0, column=1)
stand.grid(row=0, column=2)

# Dealers frame that hold the card frame
df = Frame(game, bg=background_color, ** hightlight_frame_with_white)
df.grid(row=0, column=0, columnspan=3)
dl = Label(df, text="Hello")
dl.grid()
# cards
dcf = Frame(df, bg=background_color)
dcf.grid(row=0, column=0)

d_card1 = Card.hidden_card()
d_card1_label = Label(dcf, image = d_card1, bg = background_color,name = 'dealcard1_dealer')
d_card1.pack(side=LEFT)

d_card2 = Card.hidden_card()
d_card2_label = Label(dcf, image = d_card2, bg = background_color,name = 'dealcard2_dealer')
d_card2_label.pack(side=LEFT)
# Score/status frame
sf = Frame(game, bg=background_color, **hightlight_frame_with_white)
sf.grid(row=1, column=0, columnspan=2)

# Dealers status
ds = Frame(sf, bg=background_color)
ds.grid(row=0, column=0)
dsl = Label(ds, bg=background_color, text="Dealer Balance: $", **button_args)
dsl.grid()

# Player status
ps = Frame(sf, bg=background_color)
ps.grid(row=1, column=0)
psl = Label(ps, bg=background_color, text="Player Balance: $", **button_args)
psl.grid()

#Table Frame for displaying result of the deal (WON OR LOST)
deal_results_frame = Frame(game, bg=background_color)
deal_results_frame.grid(row=1, column=1)
#Busted Text:
player_busted_message = Label(pf, text='BUSTED', font=font_medium, fg='#FF0000', bg=background_color)
dealer_busted_message = Label(df, text='BUSTED', font=font_medium, fg='#FF0000', bg=background_color)

#Deal a game:
def deal_init():
    ########
    #Clean player frame from the hit cards:
    Game.clean_table(frames = [pcf,dcf,deal_results_frame])
    ########

    ########
    #Initialize Card Instances so this way i will have a new deck each time deal is pressed
    cards_instances = []
    for card in collect_cards():
        cards_instances.append(Card(name=card)) # (Card instance)
        print(f'{card} added to deck')
    ########


    #Initialize Game:
    game = Game(
        deck = cards_instances,
        master = game,
        player_button_frame = pbf,
        player_cards_frame = pcf,
        player_card1_label = p_card1_label,
        player_card2_label = p_card2_label,
        dealer_card1_label = d_card1_label,
        dealer_card2_label = d_card2_label,
        player_score_label = psl,
        dealer_score_label = dsl,
        dealer_cards_frame = dcf,
        deal_results_frame = deal_results_frame,
        player_busted_message = player_busted_message,
        dealer_busted_message = dealer_busted_message,
    )

    # Starting operations in real game:

    #deal player:
    game.deal_player()


    #deal for dealer:
    #handle all dealt cards for dealer for here so we can keep one undisplayed
    dealer_1 = game.get_card(d_card1_label, is_player = False)
    dealer_2 = game.get_card(d_card2_label, is_player = False, display=False)

    #fill the score board:
    game.set_scoreboard()

    # Set the Buttons click function <Button-1> Stand for left click
    hit.bind('<Button-1>', lambda event: game.hit(dealer_2))
    stand.bind('<Button-1>', lambda event: game.finish_player_turn(dealer_2))


deal.bind('<Button-1>', lambda event: deal_init())
game.mainloop()
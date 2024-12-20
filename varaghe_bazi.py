SUITS=['CLUBS','DIAMONDS','HEARTS','SPADES']
RANKS=['2','3','4','5','6','7','8','9','10','jack','queen','KING','ace']

deck=[]
for rank in RANKS:
    for suit in SUITS:
        card=rank+'of'+suit
        deck+=[card]



print(deck)

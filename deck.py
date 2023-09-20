#!python3

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

deck = [rank + suit for rank in ranks for suit in suits]
print(f"All 52 cards in the deck: {deck}")
print("First 5 cards in the deck: ")
print(deck[:5])

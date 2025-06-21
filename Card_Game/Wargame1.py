
#Simple War Game

# let's walk through together on using OOP for a more robust and complex application, such as a game. 
# We will use Python OOP to simulate a simplified version of the game war. 
# Two players will each start off with half the deck, then they each remove a card, compare which card has the highest value, 
# and the player with the higher card wins both cards.


# Step 1: Card Class बनाउने
# प्रत्येक कार्डसँग दुई कुरा हुन्छ:
# Suit → जस्तै "Hearts", "Spades", "Diamonds", "Clubs"
# Rank → "2" देखि "10", "J", "Q", "K", "A"

import random   # कार्डहरू मिलाउनको लागि random प्रयोग

# --------------------------
# Step 1: Card class बनाउने
# --------------------------
class card:
    # Rank अनुसार value दिने dictionary
    values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 11, "Q": 12, "K": 13, "A": 14
    }

    def __init__(self, suit, rank):
        self.suit = suit               # कार्ड कुन सूटको हो
        self.rank = rank               # कार्डको रैंक
        self.value = card.values[rank]  # रैंक अनुसार value निकाल्ने

    def __str__(self):
        return f"{self.rank} of {self.suit}"  # कार्डलाई string जस्तो देखाउने


# Step 2: Deck class बनाउने

class Deck:
    # सबै सूट र रैंकको list
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        # ५२ वटा कार्ड बनाउने: suit र rank मिलाएर
        self.all_cards = [card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.all_cards)  # कार्ड मिलाउने

    def deal_half(self):
        # कार्डलाई दुई जनामा बाँड्ने — २६–२६ गरेर
        return self.all_cards[:26], self.all_cards[26:]

# --------------------------
# Step 3: Player class बनाउने
# --------------------------
class player:
    def __init__(self, name, cards):
        self.name = name        # खेलाडीको नाम
        self.cards = cards      # खेलाडीको कार्डहरूको सूची

    def play_card(self):
        return self.cards.pop(0)   # अगाडिको कार्ड play गर्ने

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)  # जितेको कार्डहरू थप्ने

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards."  # कार्डको संख्या देखाउने

# --------------------------
# Step 4: मुख्य Game function
# --------------------------
def play_war():
    print("Welcome to the war Game!!!")

    deck = Deck()  # नयाँ ५२ वटा कार्ड भएको deck बनाउने
    half1, half2 = deck.deal_half()  # कार्ड बाँड्ने

    player1 = player("Player 1", half1)
    player2 = player("Player 2", half2)

    round_num = 1  # सुरुवाती राउन्ड

    while player1.cards and player2.cards and round_num <= 10:  # अधिकतम १० राउन्ड
        print(f"\n-- Round {round_num} --")

        card1 = player1.play_card()
        card2 = player2.play_card()

        print(f"{player1.name} played: {card1}")
        print(f"{player2.name} played: {card2}")

        if card1.value > card2.value:
            print(f"{player1.name} wins the round!")
            player1.add_cards([card1, card2])
        elif card2.value > card1.value:
            print(f"{player2.name} wins the round!")
            player2.add_cards([card1, card2])
        else:
            print("It's a tie! Both cards are discarded.")

        print(player1)
        print(player2)

        round_num += 1  # अर्को राउन्ड

    # अन्तिम नतिजा
    if len(player1.cards) > len(player2.cards):
        print(f"\n{player1.name} wins the game!")
    elif len(player2.cards) > len(player1.cards):
        print(f"\n{player2.name} wins the game!")
    else:
        print("\nIt's a draw!")

# --------------------------
# Step 5: Start to play the game.
# --------------------------
play_war()

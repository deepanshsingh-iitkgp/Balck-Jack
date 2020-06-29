Values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
Ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
Suits = ['Hearts','Spades','Clubs','Diamonds']

class card():
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = Values[self.rank]
    
    def __str__(self):
        return (f'{self.rank} of {self.suit}({self.value})')
    
    
class deck():
    
    def __init__(self):
        
        self.all_cards = []
        for suit in Suits:
            for rank in Ranks:
                card_new = card(rank,suit)
                self.all_cards.append(card_new)
    
    def shuffle_deck(self):
        from random import shuffle
        shuffle(self.all_cards)
        
class player():
    
    def __init__(self,name,cards_in_hand = []):
        self.name = name
        self.cards_in_hand = cards_in_hand
    
    def __str__(self):
        return f'{self.name} has {len(cards)}'

def introduce(player_name):
    print(f'\nHey {player_name}, welcome to BLACK-JACK!')
    print('Its a classic two player game\ncompete against the bot!\nBEST OF LUCK!')
    print("NOTE: we've creddited 200 chips to your account!\n")
    
def read_player_name():
    name = input("What's your name? \n")
    return name

def game_start():
    while True:
        reply = input('shall we start the game?:(Y/N)\n ')
        if reply == 'Y' or reply == 'N' or reply == 'y' or reply == 'n':
            break
        else:
            print('\nplease enter a valid response:(Y/N)\n')
    return reply

def display_status_player1(player1,player2):
    sum = 0
    print("\nYour hand:")
    for card in player1.cards_in_hand:
        sum += card.value
        print(f'{card}')
    print(f"your current total: {sum}")
    print("\nComputer's hand:")
    print("first card hidden")
    for card in player2.cards_in_hand[1:]:
        print(f'{card}')

def display_status_computer(player1,player2):
    sum = 0
    print("\nYour hand:")
    for card in player1.cards_in_hand:
        sum += card.value
        print(f'{card}')
    print(f"your current total: {sum}")
    print("\nComputer's hand:")
    sum = 0
    for card in player2.cards_in_hand:
        print(f'{card}')
        sum += card.value
    print(f"computer's current total: {sum}")

def draw(deck,player):
    card_drawn = deck.all_cards.pop(0)
    player.cards_in_hand.append(card_drawn)

def result_check_computer(player_1, computer):
    value1 = 0
    value2 = 0
    for card in player_1.cards_in_hand:
        value1 += card.value
    for card in computer.cards_in_hand:
        value2 += card.value
    if value2 > 28:
        return True
    elif value2 > value1 and value2 <= 28:
        return False
def result_check_player1(player_1):
    value1 = 0
    value2 = 0
    for card in player_1.cards_in_hand:
        value1 += card.value
    if value1 > 28:
        print(f"\nOops! you've already lost, better luck next time {player_1.name}!")
        return False
    else:
        return True

class bank_account():
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deduct(self,amount):
        self.balance -= amount
        print(f"{amount} chips have been debitted from your account\n")
        
    def credit(self,amount):
        self.balance += amount
        print(f"{amount} chips have been creddited to your account\n")

def place_bet(player_account,player):
    while True:
        while True:
            try:
                bet = int(input(f"How many chips would you like to bet,{player.name}? \n"))
                break
            except:
                print('\nKindly enter an amount:')
        if bet <= player_account.balance:
            player_account.deduct(bet)
            break
        else:
            print(f'insufficient funds!')
    return bet

def black_jack():
    player_name = read_player_name()
    account = bank_account(player_name,200)

    
    introduce(player_name)
    response = game_start()
    
    while response == 'Y' or response == 'y':
        player1_cards = []
        computer_cards = []
        player1 = player(player_name,player1_cards)
        computer = player('computer',computer_cards)
        bet = place_bet(account,player1)
        
        new_deck = deck()
        new_deck.shuffle_deck()
        draw(new_deck,player1)
        draw(new_deck,player1)
        draw(new_deck,computer)
        draw(new_deck,computer)
        
        interest = 'D'
        sum1 = 0
        round = 0
        while interest in ['D','d'] and sum1 <=28 :
            display_status_player1(player1,computer)
            interest = input("Enter 'D' to draw further or 'P' to pass:(D/P)\n")
            if interest in ['d', 'D']:
                draw(new_deck,player1)
            sum1 = 0
            for card in player1_cards:
                sum1 += card.value
                if sum1 > 28:
                    display_status_player1(player1,computer)
                    break
                else:
                    pass
        result = result_check_player1(player1)
            
        if result:
            print("\nCOMPUTER'S TURN\n")            
            sum1 = 0
            sum2 = 0
            for card in player1_cards:
                sum1 += card.value
            
            for card in computer_cards:
                sum2 = card.value
                
            while sum2 <= sum1:
                draw(new_deck,computer)
                display_status_computer(player1,computer)
                sum2 = 0
                for card in computer_cards:
                    sum2 += card.value
            result = result_check_computer(player1,computer)
            if result == True:
                print(f"\nCongratulations {player1.name}, you WIN!")
                account.credit(2*bet)
                print(f"CURRENT BALANCE = {account.balance}")
            elif result == False:
                print(f"\noops! sorry {player1.name}, you've lost the round!")
                print(f"CURRENT BALANCE = {account.balance}")
        
        response = input(print("would you like to give it another shot?(Y/N):\n "))
        if response == 'n' or response == 'N' or response == 'no' or response == 'NO':
            print("thanks for playing!")
        
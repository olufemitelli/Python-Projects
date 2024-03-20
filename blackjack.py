
"""
File:    blackjack.py
Author:  Olufemi Telli
Date:    6:13
Section: 21
E-mail:  otelli1@umbc.edu
Description:
  This is a game of black jack with a twist if someone has what we call a retiever card then they automatically have 21 and there are also seeds.
        """

import random

def create_deck(num_decks):
    suits = ['\u2660', '\u2663', '\u2661', '\u2662']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank + suit) for suit in suits for rank in ranks] * num_decks
    random.shuffle(deck)
    return deck


def get_card_value(card, hand_value):
    value_map = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'R':21}
    rank = card[:-1]
    return value_map[rank]

def get_hand_value(hand):
    hand_value = 0
    num_aces = 0
    for card in hand:
        if card == 'Ace':
            num_aces += 1
        hand_value += get_card_value(card, hand_value)
    while hand_value > 21 and num_aces:
        hand_value -= 10
        num_aces -= 1
    return hand_value


def deal_cards(num_decks, retriver_cards):
    deck = create_deck(num_decks)
    random.shuffle(deck)
    player_hand = [deck.pop(0), deck.pop(0)]
    dealer_hand = [deck.pop(0), deck.pop(0)]
    return deck, player_hand, dealer_hand

def hit(deck, hand):
    hand.append(deck.pop(0))


def player_turn(deck, player_hand):
    while True:
        print(f"Your hand: {player_hand} (value {get_hand_value(player_hand)})")
        action = input("Do you want to hit or stay? ")
        if action.lower() == 'hit':
            hit(deck, player_hand)
            if get_hand_value(player_hand) > 21:
                print(f"Busted! Your hand: {player_hand} (value {get_hand_value(player_hand)})")
                return 'BUST'
        elif action.lower() == 'stay':
            print(f"Stayed with hand: {player_hand} (value {get_hand_value(player_hand)})")
            return 'STAY'
        else:
            print("Invalid input. Please try again.")

def dealer_turn(deck, dealer_hand):
    while get_hand_value(dealer_hand) < 17:
        hit(deck, dealer_hand)
        print(f"Dealer hits. Dealer's hand: {dealer_hand} (value {get_hand_value(dealer_hand)})")
    if get_hand_value(dealer_hand) > 21:
        print(f"Dealer busted with hand: {dealer_hand} (value {get_hand_value(dealer_hand)})")
        return 'BUST'
    else:
        print(f"Dealer stays with hand: {dealer_hand} (value {get_hand_value(dealer_hand)})")
        return 'STAY'


def determine_winner(player_hand, dealer_hand, bet_amount):
    player_hand_value = get_hand_value(player_hand)
    dealer_hand_value = get_hand_value(dealer_hand)
    if player_hand_value == 21 and len(player_hand) == 2:
        print(f"Blackjack! You win {bet_amount} quatloos.")
        return bet_amount
    elif dealer_hand_value == 21 and len(dealer_hand) == 2:
        print(f"Dealer has blackjack. You lose {bet_amount} quatloos.")
        return -bet_amount
    elif player_hand_value == dealer_hand_value:
        print(f"Tie game. You keep your bet of {bet_amount} quatloos.")
        return 0
    elif player_hand_value > 21:
        print(f"Busted! You lose {bet_amount} quatloos.")


def main():
    print("Welcome to Blackjack!")
    num_decks = int(input("How many decks of cards would you like to use? "))
    random_seed = input("What seed would you like to use? ")
    random.seed(random_seed)
    retriever_cards = int(input("How many Retriever cards would you like to add? "))
    deck = create_deck(num_decks)
    deck.extend(["R*"] * retriever_cards)
    player_money = 100

    while True:
        print(f"You have {player_money} quatloos, how many would you like to bet?")
        bet_amount = int(input())
        deck, player_hand, dealer_hand = deal_cards(num_decks, retriever_cards)
        print("The dealer's hand is: ", " ".join(['\u2588\u2588'] + [card for card in dealer_hand[1:]]))
        print("Your hand is: ", " ".join(player_hand), f"and has value {get_hand_value(player_hand)}")
        while True:
            action = input("What would you like to do? [hit, stay]")
            if action == "hit":
                player_hand.append(deck.pop())
                print("Your hand is: ", " ".join(player_hand), f"and has value {get_hand_value(player_hand)}")
                if get_hand_value(player_hand) > 21:
                    print("You have busted, sorry.")
                    player_money -= bet_amount
                    break
            elif action == "stay":
                dealer_result = dealer_turn(deck, dealer_hand)
                print(f"Dealer's hand is now: ", " ".join(dealer_hand), f"and has value {get_hand_value(dealer_hand)}")
                if dealer_result == "BUST":
                    print(f"You win {bet_amount} quatloos.")
                    player_money += bet_amount
                elif get_hand_value(dealer_hand) > get_hand_value(player_hand):
                    print("Dealer wins.")
                    player_money -= bet_amount
            elif get_hand_value(dealer_hand) == get_hand_value(player_hand):
                print(f"Tie game. You keep your bet of {bet_amount} quatloos.")
            else:
                print(f"You win {bet_amount} quatloos.")
                player_money += bet_amount
            break
            if player_money == 0:
                print("You are out of money. Thanks for playing!")
                break
            play_again = input("Would you like to play again? [y/yes, n/no]")
            if play_again.lower() not in ["y", "yes"]:
                print("Thanks for playing!")
                break
main()


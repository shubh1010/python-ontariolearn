import random


def draw_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"])


def calculate_score(cards):
    total = 0
    aces = 0
    for card in cards:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            aces += 1
            total += 11
        else:
            total += card
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def display_cards(cards, is_dealer=False):
    if is_dealer:
        return f"Dealer has {cards[0]} and a hidden card."
    if len(cards) == 2:
        return f"{cards[0]} and {cards[1]}"
    return f"{', '.join(map(str, cards[:-1]))}, and {cards[-1]}"


def player_turn():
    player_cards = [draw_card(), draw_card()]
    while True:
        total = calculate_score(player_cards)
        print(f"Your cards are: {display_cards(player_cards)}. Your total is {total}.")

        if total > 21:
            print("You bust! Dealer wins!")
            return None
        if total == 21:
            print("You got Blackjack! You win!")
            return total

        move = input("Hit or stand? (h/s): ").strip().lower()
        if move == "h":
            player_cards.append(draw_card())
        elif move == "s":
            return total
        else:
            print("Invalid input. Please enter 'h' for hit or 's' for stand.")


def dealer_turn(hidden_card, visible_card):
    dealer_cards = [visible_card, hidden_card]
    print(f"The dealer reveals the hidden card:{hidden_card}. Dealer's total is {calculate_score(dealer_cards)}.")
    while True:
        total = calculate_score(dealer_cards)
        if total > 21:
            print(f"The dealer busts with a total of {total}! You win!")
            return None
        if total >= 17:
            print(f"The dealer stands with a total of {total}.")
            return total
        print("The dealer hits.")
        dealer_cards.append(draw_card())
        print(f"The dealer draws {dealer_cards[-1]}. Dealer's total is {calculate_score(dealer_cards)}.")


def determine_winner(player_total, dealer_total):
    if player_total > dealer_total:
        print(f"You win! Your total is {player_total} and dealer's total is {dealer_total}.")
    else:
        print(f"You lose! Your total is {player_total} and dealer's total is {dealer_total}.")


def play_game():
    print("Welcome to Blackjack!")
    while True:
        player_response = input("Do you want to play a new game? (y/n)").strip().lower()
        if player_response == "n":
            print("Thanks for playing! Have a nice day!")
            break
        elif player_response == "y":
            print("\nStarting a new game...\n")

            visible_card = draw_card()
            hidden_card = draw_card()
            print(f"The dealer draws the hidden card: {visible_card} and a hidden card.")

            player_total = player_turn()
            if player_total is None:
                continue

            dealer_total = dealer_turn(hidden_card, visible_card)
            if dealer_total is None:
                continue

            determine_winner(player_total, dealer_total)
        else:
            print("Invalid input. Please enter y (for yes) or n (for no).")


if __name__ == "__main__":
    play_game()

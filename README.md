Blackjack Game

Description

This is a simple command-line Blackjack game written in Python. The game follows standard Blackjack rules where the player competes against the dealer to get as close to 21 as possible without going over.

How to Play
	1.	Run the script in a Python environment:

python blackjack.py


	2.	The game will ask if you want to start a new round. Type y for yes or n for no.
	3.	You and the dealer will each receive two cards:
	•	You can see both of your cards.
	•	The dealer’s second card is hidden.
	4.	You can choose to:
	•	Hit (h) → Draw an extra card.
	•	Stand (s) → Keep your current cards.
	5.	The dealer reveals their hidden card and follows standard rules:
	•	Hits until they reach at least 17.
	•	If the dealer exceeds 21, you win automatically.
	6.	The winner is determined based on the highest total ≤ 21.

Game Rules
	•	Number cards (2-10) are worth their face value.
	•	Face cards (J, Q, K) are worth 10 points.
	•	Aces (A) are worth 11 points but turn into 1 point if the total exceeds 21.

Example Gameplay

Welcome to Blackjack!  
Do you want to play a new game? (y/n) y  

Starting a new game...  

The dealer draws the hidden card: 10 and a hidden card.  
Your cards are: 7 and K. Your total is 17.  
Hit or stand? (h/s): s  

The dealer reveals the hidden card: 6. Dealer's total is 16.  
The dealer hits.  
The dealer draws 8. Dealer's total is 24.  
The dealer busts with a total of 24! You win!  

Requirements
	•	Python 3.x
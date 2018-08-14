# The-Blackjack-Game
One approach to strengthen your programming skills is the game development. In this problem,
therefore, you are asked to develop a Blackjack (二十一點) game, which allows a user to play against
a computer dealer (莊家). First of all, let me remind you the rules of Blackjack as follows:

(1)First, both player and dealer receive two cards from a shuffled deck of 52 cards (一副洗好的牌).

(2)After the first two cards are delivered to dealer and player, the player is asked if they want
another card (called "hitting" (再抽)), or if he/she are happy with the cards they have already
(called "staying" (停止)). The goal is to make the sum of the player’s card values as close to 21 as
possible, without going over. If the player makes 21 exactly, he/she has Blackjack, which cannot
be beat. If the player goes over 21, he/she "busts" (爆掉) and lose the game. The player is allowed
to stop hitting at any time point.

(3)The number cards (2 through 10) are worth the number displayed, face cards (JACK, QUEEN, and
KING) are worth 10, and an ACE can be worth either 1 or 11. For example, if the first two cards in
the player’s hand are a JACK and an ACE, you needs to count the ACE as 11 because 10 + 11 = 21
and have Blackjack. But if the player has already had the cards worth 18, and decides to hit and
gets an ACE, you should count such ACE as 1, because counting it as 11 would put the player at
29 and get busted.
(4)Once the player’s hand is finished, the dealer will try to do the same things. The dealer must keep
hitting until he/she gets to 17. If the dealer gets above 17 without busting, then they can stay.
Finally, the game is settling by simple rules: 1. if the player has blackjack, he/she wins the game,
unless the dealer also has Blackjack, in which case the game is a tie. 2. If the dealer busts and the
player does not, the player wins. 3. If the player busts, the dealer wins. 4. If the player and the dealer
both do not bust, whoever is closest to 21 wins.

To help you implement the Blackjack game, we divide the Blackjack game into six of the division of
labor in terms of the program logic, as described in the following. The program logic forms the game
engine, enforcing the rules of the game.

(a) Preprocessing. Create the deck of cards by combing the 13 ranks (ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10,
JACK, QUEEN, and KING) with 4 suits (SPADE, HEART, DIAMOND, and CLUB). There are 52 cards.
Then before the game starts, you need to shuffle the cards.

(b) Settle the Stage. Send the player’s and dealer’s first two cards by random. In other words, four
cards that will be owned by the player and the dealer respectively are taken from the 52 cards.

(c) Compute the Total Value. Your program has to reason the total value of cards in the hand. Two
things must be done here. First, your program needs to reason the value of a card. For example,
ACE = 1 or 11, JACK/QUEEN/KING = 10. Second, by default you program considers ACE as 11.
Then your program needs to count up the number of ACEs in the hand, then checks to see that
the total value in the hand is higher than 21. If it is, and there is an ACE in the hand, your
program needs to consider the ACE as 1, and re‐computes the total value. If not, your program
obtains the current total value of the player. Otherwise, if there is a second ACE in the hand,
your program again considers the second ACE as 1 and checks again. We continue to do this
until we have exhausted all the ACEs in the player’s hand. Finally, your program obtains the total
value in the player’s hand.

(d) Game Logic. The next thing we code is the logic of gameplay. Your program has to ask the player
whether he/she would like to hit or stay, and continue to ask them until they bust, or they
decide to stay. One piece of information that’s crucial to the player’s decision is their current
cards in the hands. Therefore, we need to print the player’s cards in the hand and current total
value each time before asking for their response and input. As long as the player’s hand isn’t a
bust, we ask for the player’s input: hit (再抽) = 1, stay (停止) = 0. If the player wants to hit, we
again deliver him/her a new card by randomly drawn a card from the remaining cards in the
deck, and immediately print the newly drawn card. If they ask to stay, the action of the player
will be terminated, and your program moves on to the dealer. In the meanwhile, your program
needs to calculate the player’s value, and the dealer’s current value (on his/her first two cards).
If the player’s hand isn’t a bust, we print the dealer’s total value and current cards. Then, while
the dealer’s hand is worth less than 17, the dealer is made to hit. Each time each dealer hits,
you need to print the new drawn card. By design, this loop halts when the dealer exceeds 17.

(e) Determine the Winner. At this point, the game is nearly finished. All that remains is to check
the player’s total value and the dealer’s total value against the list of scoring rules we outlined
above. To start, we obtain the label, and number for the score of the dealer's hand. Next, we
simply enumerate the possible end states, and ask which of them our game satisfies. Based on
the outcome, we print to the screen declaring the winner.

(f) Ask the Player to play or not. If the player does not want to play again, quit the Blackjack game.
If the player wants to play again, your program needs to rearrange the deck of cards to let the
player play one more time.

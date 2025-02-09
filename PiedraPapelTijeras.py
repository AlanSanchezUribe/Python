print('Welcome to the game of Rock, Paper, Scissors')
print('Please choose one of the following options:')
print('1. Rock')
print('2. Paper')
print('3. Scissors')
player1 = input('Player 1, please enter your choice: ')
player2 = input('player 2, please enter your choice: ')
player1 = player1.lower()
player2 = player2.lower()
if player1 == player2:
    print('It is a tie')
elif player1 == 'rock' and player2 == 'scissors':
    print('Player 1 wins')
elif player1 == 'rock' and player2 == 'paper':
    print('Player 2 wins')
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 wins')
elif player1 == 'paper' and player2 == 'scissors':
    print('Player 2 wins')
elif player1 == 'scissors' and player2 == 'paper':
    print('Player 1 wins')
elif player1 == 'scissors' and player2 == 'rock':
    print('Player 2 wins')
else:
    print('Invalid input try again')
print('Game over')
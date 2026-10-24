# TIC-TAC-TOE

## 1. Project Overview
This is a simple, console based  tic-tac-toe game developed using Python. Simply it is a two player game where the players can place their selected symbol in a 3x3 game board in each turns.
The objective of this game is to place three identical symbol in a horizontal row or vertical column or in the diagonal before the opponent does.

## 2. Project Features

- **Two player mode:** this allows the players to play against each other.

- **Player Name:** Playeers can manually give their name before the game starts.

- **Symbol Selection:** Players can select the symbol. The first player chooses the symbol X or O and the second player receives the opposite symbol.

- **3×3 Game Board:** Displays the game board using a simple text-based interface.

- **Input Validation:** Checks whether the entered position is between 1 and 9.

- **Occupied Position Check:** Prevents players from selecting positions that are already occupied.

- **Win Detection:** Checks rows, columns, and diagonals to determine the winner.

- **Replay Option:** Allows players to start another game without restarting the program.

- **Error Handling:** Handles invalid inputs using Python's try and except statements.

## 3. Game Instructions

The game board contains nine positions numbered from 1 to 9.

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Players select a position by entering its corresponding number.

For example, if Player 1 enters 5, their symbol will be placed in the center of the board.

| 1 | 2 | 3 |
|---|---|---|
| 4 | X | 6 |
| 7 | 8 | 9 |

Rules:

- Two players participate in the game.
- Each player uses a different symbol: X or O.
- Players take turns selecting positions.
- A position cannot be selected if it is already occupied.
- A player wins by placing three identical symbols in a row, column, or diagonal.
- If all nine positions are occupied and neither player wins, the game is a draw.
- After the game ends, players can choose to play again.
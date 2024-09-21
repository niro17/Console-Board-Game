# Console-Board-Game
20 x 2 - Console Board Game Description

**20 x 2** is a two-player board game played between a human player and a computer. The game board consists of 20 blocks, numbered from 1 to 20 for both players. The goal is to move a pawn, represented by an "X", from block 1 to block 20. The game introduces a few twists with black holes and movement rules that create unique challenges for players.

### Gameplay
The game begins when a player rolls a 6 on the dice, which allows their pawn to enter the board. Until then, players keep rolling the dice, waiting for the starting roll. Once the game starts, players move forward based on the dice value divided by two (e.g., rolling a 6 means moving 3 blocks, a 4 means 2 blocks, and a 1 means no movement).

Black holes are placed on blocks 7 and 14 for both players. Landing on a black hole forces the player to return to block 1, although passing over them without landing is safe. The game alternates turns between the human player and the computer, with the first to reach or pass block 20 declared the winner.

### Game Board
The game board is displayed on the console, showing two rows—one for the human and one for the computer. The board updates in real time as the players move, showing pawns "X" and black holes "O" on the corresponding blocks.

### Game End and Session Logging
Once the game ends, whether the human or computer wins, the game session is saved in a text file with a timestamp in the format `YYYY_M_D_H_M.txt`. The session file contains a log of all moves made, including details of any black hole hits and the final game result.

This game is designed to be played on the console, offering a fun and strategic experience without requiring advanced external libraries like NumPy.

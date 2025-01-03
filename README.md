﻿# snake_game_using_pygame 
 
# Snake Game in Python with Pygame

This is a classic **Snake Game** developed using **Pygame**. In this game, the player controls a snake that eats food, growing longer as it advances. The game ends when the snake hits the screen boundaries or collides with its own body.

## Features

- **Classic Snake Game mechanics**: Snake grows longer when it eats food.
- **Increasing difficulty**: Game speed increases with each level.
- **Music and sound effects**: Background music and game over sound.
- **Game over screen**: Option to retry or quit.

## Requirements

To run this game, you'll need:

- Python 3.x installed.
- Pygame installed. You can install Pygame using pip:

  ```bash
  pip install pygame
  ```

- The following sound files should be placed on your system for the game:
  1. **Background music**: `squid-game-music-tone.mp3`
  2. **Game Over sound**: `game-over-160612.mp3`

Make sure to provide the correct paths for these audio files in the code where required.

## Game Controls

- **Arrow keys** (Up, Down, Left, Right): Control the snake's movement.
- **Enter**: Restart the game after a game over.
- **Esc**: Quit the game after a game over.

## How to Play

1. Run the game by executing `snake_game.py`.
2. The game will show a start screen with a **Press Enter to Start** prompt.
3. Use the arrow keys to control the snake and eat the food that appears on the screen.
4. The game speed will increase after every 5 points scored.
5. If the snake collides with the boundaries or itself, the game will display a "Game Over" screen with an option to **try again** or **quit**.

## Game Mechanics

- **Snake Movement**: The snake moves based on arrow key input, and the head moves in the direction chosen while the body follows.
- **Collisions**:
  - If the snake hits the boundaries of the game window, or its body, the game is over.
- **Score**: The score increases by 1 for every piece of food the snake eats.
- **Levels**: The level increases with the score and makes the snake move faster.

## Code Breakdown

### Main Game Loop
The main game loop controls the logic for the snake's movement, eating food, collision detection, and screen updates. It keeps running until the player decides to quit or restarts after a game over.

### Game Over Screen
A game over screen displays the player's score and lets them choose to restart the game or quit.

### Music and Sound
Background music and sound effects are used for a more engaging experience.

## Possible Enhancements

1. **High Scores**: Save the highest score across game sessions.
2. **Add Obstacles**: Add random obstacles for the snake to avoid.
3. **Game Modes**: Implement different difficulty modes.

## License

This game is free for personal use. Redistribution and modification of the code are allowed under the terms of your chosen license.

![Screenshot 2025-01-02 203618](https://github.com/user-attachments/assets/d65d2af3-8ab5-41af-ada9-9e196a7d5364)

![Screenshot 2025-01-02 203708](https://github.com/user-attachments/assets/aa6e5999-c340-4a9d-a123-a61cc3919c25)

![Screenshot 2025-01-02 203715](https://github.com/user-attachments/assets/c1349461-8a19-43f9-b985-432214e7433c)






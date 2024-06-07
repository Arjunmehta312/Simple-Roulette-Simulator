# Roulette Game

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Code Overview](#code-overview)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Roulette Game project is a desktop application that simulates a classic casino roulette game. Built using Python's Tkinter library, this interactive application allows users to place various types of bets, spin the roulette wheel, and win or lose virtual currency based on the outcome.

## Features
- **User Interface**: Intuitive GUI built with Tkinter.
- **Multiple Betting Options**: Bet on single numbers, red/black, even/odd, low/high, columns, and dozens.
- **Balance Management**: Start with ₹1000 and update balance based on game outcomes.
- **Random Roulette Spin**: Simulates a real roulette wheel with random results.
- **Result Display**: Shows spin result, win/loss status, and balance updates.
- **Play Again Option**: Allows users to play multiple rounds or exit the game.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/roulette-game.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd roulette-game
   ```
3. **Install Dependencies**:
   - Ensure you have Python installed. This project requires Python 3.x.
   - Install Tkinter if it is not already installed. Tkinter is usually included with Python installations, but you can install it using your package manager if needed.
   
## Usage
1. **Run the Application**:
   ```bash
   python roulette_game.py
   ```
2. **Place Your Bet**:
   - Click on the "Place Bet" button.
   - Select your bet type and enter the bet amount.
   - Confirm the bet.
3. **Spin the Roulette**:
   - The application will randomly generate a result and display it.
4. **Check Results**:
   - The outcome will be displayed, and your balance will be updated accordingly.
5. **Play Again**:
   - Choose to play another round or exit the game.

## Game Rules
- **Starting Balance**: Each player starts with ₹1000.
- **Betting Options**:
  - **Red/Black**: Bet on the ball landing on a red or black tile.
  - **Even/Odd**: Bet on an even or odd number.
  - **Single Number**: Bet on a specific number (0-36).
  - **Low/High**: Bet on low (1-18) or high (19-36) numbers.
  - **Column**: Bet on one of the three columns.
  - **Dozen**: Bet on one of the three dozens (1-12, 13-24, 25-36).
- **Winning and Losing**:
  - If your bet matches the spin result, you win and your balance increases based on the payout rate.
  - If your bet does not match the result, you lose and your balance decreases by the bet amount.
- **Payout Rates**:
  - Red/Black, Even/Odd, Low/High: 1:1
  - Column, Dozen: 2:1
  - Single Number: 35:1

## Code Overview
### Initialization
- **Starting Balance**: Set to ₹1000.
- **Roulette Numbers**: List of numbers from 0 to 36.

### Functions
- **display_balance()**: Updates and displays the current balance.
- **place_bet()**: Opens a new window to place bets and handles bet confirmation.
- **spin_roulette(bet, bet_amount, bet_type)**: Simulates the roulette spin, determines the outcome, updates the balance, and displays the result.
- **red_numbers()**: Returns a list of red numbers on the roulette wheel.
- **black_numbers()**: Returns a list of black numbers on the roulette wheel.
- **column_numbers(column)**: Returns the numbers in the specified column.
- **dozen_numbers(dozen)**: Returns the numbers in the specified dozen.
- **play_again()**: Prompts the user to play again or exit the game.

### GUI Components
- **Main Window**: Initializes the main Tkinter window.
- **Labels and Buttons**: Includes labels for displaying balance and results, and buttons for placing bets and playing again.

### Running the Game
- The game starts with the initial balance displayed.
- Users can place bets, spin the roulette, and see the results.
- The balance is updated, and users can choose to play another round or exit.

## Future Enhancements
- **Enhanced Betting Options**: Add more betting options such as street bets, corner bets, etc.
- **Improved UI**: Enhance the user interface with better graphics and animations.
- **Statistics**: Display statistics such as the number of games played, total wins, and losses.
- **Save Progress**: Implement a feature to save and load game progress.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

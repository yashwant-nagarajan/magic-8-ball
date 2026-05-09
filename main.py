# Magic 8 Ball Simulator 🎱

A simple, interactive command-line Python application that mimics the classic Magic 8 Ball toy. 

## Features
* **Interactive CLI:** Prompts users to type any yes-no question.
* **Classic Responses:** Contains the original 20 traditional Magic 8 Ball answers.
* **Randomized Output:** Uses Python's pseudo-random number generation for unbiased answers.
* **Input Validation:** Prevents empty submissions and ensures continuous play loops.

## Installation
Clone the repository to your local machine:
```bash
git clone github.com
cd magic-8-ball
```

## Usage
Run the script using Python 3:
```bash
python magic-8-ball.py
```

## How It Works
1. The program initializes a list of 20 classic responses (positive, hesitant, and negative).
2. The user is prompted to enter a question.
3. The script utilizes `random.choice()` to select a random response.
4. The user is asked if they want to ask another question or exit.

  

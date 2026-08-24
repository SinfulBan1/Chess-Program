# Chess Program

This program is meant for use in the terminal, which allows users to create and manage tournaments.

## Setup

Clone or download this repo and open a terminal in the project directory (or alternatively, find it with cd command)

It is recommended that you create a virtual environment as well.

### Virtual environment creation

```
python -m venv .venv
.venv/Scripts/activate
```

### Install the requirements
```
python -m pip install -r requirements.txt
```

## Running

From the root directory, run:
```
python chess_program.py
```

The list of tournaments is the main menu of the program, although it is worth noting that if there is only one active tournament (current date is between start and end dates), that will be the page loaded initially.

Users can navigate through the menus by typing letters/numbers into the console.

When creating a tournament, the user will be able to give tournament information before being brought to the tournament view screen.
From there, the user can add players and filter through them.

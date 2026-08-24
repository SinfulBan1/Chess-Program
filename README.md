# Chess Program

This program is meant for use in the terminal, which allows users to create and manage tournaments.

## Setup

Clone or download this repo and open a terminal in the project directory (or alternatively, find it with cd command)

It is recommended that you create a virtual environment as well.

### Virtual environment creation

```
python -m venv .venv
.venv\Scripts\activate
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
A tournament is only able to be started when there are an even number of 2+ players.

The Create First Round option can be used to start the tournament, and from then on whenever the user wants to start the next round, they must enter the winners of the previous round's matches.

At any point a report can be generated for a tournament which shows all relevant information to it.

## Persistence

Data is saved and loaded to/from the data folder. This means data is persistent even through restarts.

## Flake8

Flake8 was used to check code quality.
The report is visible in the flake8_report folder, inside index.html.

To run it yourself, run this command in the project root directory's terminal:
```
python -m flake8 . --max-line-length=119 --format=html --htmldir=flake8_report --exclude=.git,__pycache__,.venv,venv,flake8_report
```
It is important to note that I had to use some ignoring tags for the report, as the project relies on exposing classes to init files, which flake8 marks as unused, even when they end up getting used elsewhere. Importantly, this was only ever used on those init files.
Along with the import ignores, part of the starter code that was given to me contained a line of code that is much longer than the 119 limit. This code was for the email regex, and since it was provided with the starter code, I commented an ignore on that one as well.

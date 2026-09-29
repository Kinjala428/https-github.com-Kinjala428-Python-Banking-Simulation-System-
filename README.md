# Python Banking Simulation System

## Overview
A console-based Banking Simulation System built in Python that replicates core ATM/banking operations — balance inquiry, deposit, withdrawal, and statement generation — using only fundamental Python constructs (variables, functions, conditionals, loops, dictionaries, and lists). The project was built  to demonstrate practical application of algorithmic thinking, function design, and data structure usage.

## Features
- **Account Management** — create an account with name, initial balance, and a 4-digit PIN; PIN-based authentication before any transaction
- **Transaction Processing** — deposit and withdraw funds, with validation to reject invalid/negative input and prevent overdrafts
- **Reporting** — mini statement (last 5 transactions), full transaction history, and a session summary (total deposited, total withdrawn, net change)
- Input validation and graceful error handling throughout
- Modular file structure — each functional area lives in its own file

## Technologies / Tools Used
- **Language:** Python 3 (standard library only — no external packages)
- **Design tools:** Graphviz (for UML/architecture diagrams)
- **Version control:** Git / GitHub

## Project Structure
```
BankingSimulationProject/
├── README.md
├── statement.md
└── docs/
    └── Project Report.word
## Steps to Install & Run
1. Ensure Python 3 is installed (`python3 --version`).
2. Clone or download this repository.
   cd pythonBankingSimulationsystem/
   ```
4. Run the application:
   ```
   python3 main.py
   ```
5. Follow the on-screen prompts to create an account, authenticate, and use the menu.

## Instructions for Testing
- **Valid flow:** Create an account → enter correct PIN → try each menu option (1–7) → confirm balance updates correctly after deposit/withdrawal.
- **Invalid input test:** At any amount prompt, enter a negative number, zero, or text (e.g., `abc`) — the system should reject it with an error message and return to the menu.
- **Overdraft test:** Attempt to withdraw more than the current balance — the system should deny the transaction with an "Insufficient funds" message.
- **PIN test:** At authentication, enter an incorrect PIN up to 3 times — the system should lock the session after 3 failed attempts.
- **Reporting test:** After a few transactions, check that Mini Statement, Full Statement, and Session Summary all reflect the correct values.


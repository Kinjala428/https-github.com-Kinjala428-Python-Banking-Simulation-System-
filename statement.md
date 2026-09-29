# Project Statement

## Problem Statement
Manual tracking of bank account transactions is error-prone and offers no structured way to validate operations like withdrawals against available balance. This project addresses that by simulating a simplified banking system in software, where account operations are handled programmatically with built-in validation, ensuring accurate and reliable transaction processing.

## Scope of the Project
This project is limited to a single-user, console-based banking simulation running entirely in memory (no persistent database or network connectivity). It supports account creation, PIN authentication, balance inquiry, deposits, withdrawals, and transaction reporting within a single program session. Advanced banking features such as fund transfers between accounts, interest calculation, or loan management are outside the scope of this version.

## Target Users
- Students and instructors evaluating the application of core programming concepts (control flow, functions, data structures) in a realistic scenario.
- Anyone wanting a simple, extendable starting point for a console-based financial application.

## High-Level Features
- Create an account with name, starting balance, and a 4-digit PIN
- Authenticate via PIN before accessing account operations
- Check current balance
- Deposit funds (with input validation)
- Withdraw funds (with input validation and overdraft prevention)
- View a mini statement (last 5 transactions)
- View the full transaction history
- View a session summary (total deposited, total withdrawn, net change, closing balance)

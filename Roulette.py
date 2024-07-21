#!/usr/bin/env python
# coding: utf-8

# # Roulette

# Disclaimer:
# This Python Roulette Game is intended solely for entertainment purposes and does not involve real money or actual gambling. No financial transactions are associated with this game. The outcome of each spin is determined by random chance, and while players may choose different betting strategies, there is no guarantee of winning. Please play responsibly and within your means. If you experience any negative emotions related to gambling, consider seeking professional help.

# In[43]:


# Import libraries

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# tkinter: This is the standard Python interface to the Tk GUI toolkit. tkinter is used to create graphical user interfaces.
# messagebox: This module in tkinter provides a simple way to create message boxes (e.g., for showing error or information messages).
# random: This module provides functions to generate random numbers and to make random choices. It will be used to deal cards randomly from the deck.


# In[44]:


# Starting balance
balance=1000


# In[45]:


# LIST: Roulette wheel with 37 numbers (0-36)
roulette_numbers=list(range(37))


# In[46]:


# DICTIONARY KEY-VALUE PAIR: Betting modes and payouts
bet_options={
    "red":1,      # betting on a red tile
    "black":1,    # betting on a black tile
    "even":1,     # betting on an even number
    "odd":1,      # betting on an odd number
    "single":35,  # betting on a single number
    "low":1,      # low means the number is 1-18 
    "high":1,     # high means the number is 19-36
    "column":2,   # payout for column bet
    "dozen":2,    # payout for dozen bet where 1st dozen is 1-12, 2nd dozen is 13-24 and 3rd dozen is 25-36
}


# In[47]:


# Function to display balance
def display_balance():
    balance_label.config(text=f"Current balance: ₹{balance}")


# In[48]:


def place_bet():
    bet_window = tk.Toplevel(root)
    bet_window.title("Place Your Bet")

    tk.Label(bet_window, text="Available betting options:").pack()

    bet_options = [
        ("Red", 1),
        ("Black", 2),
        ("Even", 3),
        ("Odd", 4),
        ("Single number (0-36)", 5),
        ("Low (1-18)", 6),
        ("High (19-36)", 7),
        ("Column", 8),
        ("Dozen", 9),
    ]

    bet_type_var = tk.IntVar()
    bet_type_var.set(1)

    for text, value in bet_options:
        tk.Radiobutton(bet_window, text=text, variable=bet_type_var, value=value).pack(anchor=tk.W)

    tk.Label(bet_window, text="Enter your bet amount:").pack()
    bet_amount_entry = tk.Entry(bet_window)
    bet_amount_entry.pack()

    def confirm_bet():
        bet_type = bet_type_var.get()
        bet_amount = int(bet_amount_entry.get())

        if bet_amount > balance:
            messagebox.showerror("Error", "Insufficient funds! Place a smaller bet.")
            return

        if bet_type == 5:
            chosen_number = tk.simpledialog.askinteger("Input", "Enter the number you want to bet on (0-36):", minvalue=0, maxvalue=36)
            if chosen_number not in roulette_numbers:
                messagebox.showerror("Error", "Choose a valid number!")
                return
            spin_roulette(chosen_number, bet_amount, bet_type)
        elif bet_type == 8:  # Column bet
            column_choice = tk.simpledialog.askinteger("Input", "Enter the column you want to bet on (1, 2, or 3):", minvalue=1, maxvalue=3)
            if column_choice not in [1, 2, 3]:
                messagebox.showerror("Error", "Invalid choice. Please select a valid column (1, 2, or 3).")
                return
            spin_roulette(str(column_choice), bet_amount, bet_type)
        elif bet_type == 9:  # Dozen bet
            dozen_choice = tk.simpledialog.askinteger("Input", "Enter the dozen you want to bet on (1, 2, or 3):", minvalue=1, maxvalue=3)
            if dozen_choice not in [1, 2, 3]:
                messagebox.showerror("Error", "Invalid choice. Please select a valid dozen (1, 2, or 3).")
                return
            spin_roulette(str(dozen_choice), bet_amount, bet_type)
        else:
            spin_roulette(bet_type, bet_amount, bet_type)

        bet_window.destroy()

    tk.Button(bet_window, text="Place Bet", command=confirm_bet).pack()


# In[49]:


def spin_roulette(bet, bet_amount, bet_type):
    global balance
    result = random.choice(roulette_numbers)
    result_label.config(text=f"Roulette result: {result}")
    win = False
    reason = ""

    if bet_type == 5:  # Single number bet
        if result == bet:
            win = True
            payout = bet_options['single'] * bet_amount
            reason = f"you bet on number {bet}."
        else:
            reason = f"you bet on number {bet}."
    else:
        if bet_type == 1 and result in red_numbers():
            win = True
            payout = bet_options['red'] * bet_amount
            reason = "you bet on red."
        elif bet_type == 2 and result in black_numbers():
            win = True
            payout = bet_options['black'] * bet_amount
            reason = "you bet on black."
        elif bet_type == 3 and result % 2 == 0 and result != 0:
            win = True
            payout = bet_options['even'] * bet_amount
            reason = "you bet on even."
        elif bet_type == 4 and result % 2 != 0:
            win = True
            payout = bet_options['odd'] * bet_amount
            reason = "you bet on odd."
        elif bet_type == 6 and 1 <= result <= 18:
            win = True
            payout = bet_options['low'] * bet_amount
            reason = "you bet on low."
        elif bet_type == 7 and 19 <= result <= 36:
            win = True
            payout = bet_options['high'] * bet_amount
            reason = "you bet on high."
        elif bet_type == 8 and result in column_numbers(bet):
            win = True
            payout = bet_options['column'] * bet_amount
            reason = f"you bet on column {bet}."
        elif bet_type == 9 and result in dozen_numbers(bet):
            win = True
            payout = bet_options['dozen'] * bet_amount
            reason = f"you bet on dozen {bet}."
        else:
            reason = f"the result didn't match your bet."

    if win:
        messagebox.showinfo("Result", f"You won! Payout: ₹{payout} because {reason}")
        balance += payout
    else:
        messagebox.showinfo("Result", f"You lost ₹{bet_amount} because {reason}")
        balance -= bet_amount

    display_balance()


# In[50]:


def red_numbers():
    return [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]


# In[51]:


def black_numbers():
    return [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]


# In[52]:


def column_numbers(column):
    if column=="1":
        return [1,4,7,10,13,16,19,22,25,28,31,34]
    elif column=="2":
        return [2,5,8,11,14,17,20,23,26,29,32,35]
    elif column=="3":
        return [3,6,9,12,15,18,21,24,27,30,33,36]


# In[53]:


def dozen_numbers(dozen):
    if dozen=="1":
        return list(range(1,13))
    elif dozen=="2":
        return list(range(13,25))
    elif dozen=="3":
        return list(range(25,37))


# In[54]:


def play_again():
    play_more=messagebox.askyesno("Play Again","Do you want to play again?")
    if play_more:        
        place_bet()
    else:
        messagebox.showinfo("Roulette","Roulette finished!")
        root.quit()


# In[55]:


# Initialize Tkinter root window
root=tk.Tk()
root.title("Roulette Game")

balance_label=tk.Label(root,text=f"Current balance: ₹{balance}",font=("Helvetica",14))
balance_label.pack(pady=10)

result_label=tk.Label(root,text="",font=("Helvetica",14))
result_label.pack(pady=10)

bet_button=tk.Button(root,text="Place Bet",command=place_bet,font=("Helvetica",14))
bet_button.pack(pady=20)

play_again_button=tk.Button(root,text="Play Again",command=play_again,font=("Helvetica",14))
play_again_button.pack(pady=20)

# Display initial balance
display_balance()

# Run the Tkinter event loop
root.mainloop()


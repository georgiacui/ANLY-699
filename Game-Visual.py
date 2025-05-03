#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import random

# Create main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

# Choices and result variables
choices = ["Rock", "Paper", "Scissors"]
result_text = tk.StringVar()
user_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()

# Game logic function
def play(user_choice):
    computer_choice = random.choice(choices)
    user_choice_text.set(f"You chose: {user_choice}")
    computer_choice_text.set(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or          (user_choice == "Paper" and computer_choice == "Rock") or          (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    result_text.set(result)

# Create widgets
tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, textvariable=user_choice_text, font=("Helvetica", 12)).pack()
tk.Label(root, textvariable=computer_choice_text, font=("Helvetica", 12)).pack()
tk.Label(root, textvariable=result_text, font=("Helvetica", 14, "bold")).pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=20)

for choice in choices:
    btn = tk.Button(frame, text=choice, width=10, command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)

# Run the GUI
root.mainloop()


import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pyttsx3
import pandas as pd
import numpy as np
import threading
import logging

# Setup logging
logging.basicConfig(filename="headline_generator.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Headline storage using Pandas
headline_df = pd.DataFrame(columns=["Timestamp", "Category", "Headline"])

# Categories
subjects = {
    "sports": ["Virat Kohli", "Rohit Sharma", "A confused umpire", "A retired cricketer"],
    "politics": ["Prime Minister Modi", "Nirmala Sitharaman", "Rahul Gandhi", "A political analyst"],
    "dance": ["Shahrukh Khan", "A Bollywood choreographer", "A dancing peacock", "A flash mob dancer"],
    "random": ["A Mumbai cat", "A group of monkeys", "Auto rickshaw driver from Delhi", "A tea stall vendor"]
}

actions = {
    "sports": ["scores century against", "gets bowled over by", "celebrates with", "challenges"],
    "politics": ["declares war on", "debates fiercely with", "tweets angrily about", "orders"],
    "dance": ["performs bhangra with", "joins flash mob at", "dances with", "choreographs"],
    "random": ["eats", "launches", "cancels", "celebrates"]
}

places_or_things = {
    "sports": ["during IPL match", "in cricket stadium", "at India Gate", "on national television"],
    "politics": ["inside Parliament", "at election rally", "on Twitter", "in front of media"],
    "dance": ["on dance reality show", "at Ganga Ghat", "in Mumbai local train", "at Red Fort"],
    "random": ["a plate of samosa", "at tea stall", "at Ganga Ghat", "in Mumbai local train"]
}

emojis = ["😂", "🤣", "😳", "🤯", "😎", "🙈"]
emoji_weights = [0.2, 0.2, 0.15, 0.15, 0.2, 0.1]  # NumPy will use these for weighted selection

# Text-to-speech in a separate thread
def speak_text(text):
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()

# Generate headline
def generate_headline():
    category = category_var.get()
    if category not in subjects:
        messagebox.showerror("Error", "Please select a valid category.")
        logging.error("Invalid category selected.")
        return

    subject = random.choice(subjects[category])
    action = random.choice(actions[category])
    place_or_thing = random.choice(places_or_things[category])
    emoji = np.random.choice(emojis, p=emoji_weights)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    headline = f"{emoji} [{timestamp}] BREAKING NEWS: {subject} {action} {place_or_thing}"
    headline_label.config(text=headline)

    # Speak
    speak_text(headline)

    # Save to DataFrame
    global headline_df
    headline_df = pd.concat([headline_df, pd.DataFrame([[timestamp, category, headline]], columns=headline_df.columns)], ignore_index=True)

    # Save to file
    try:
        headline_df.to_csv("funny_headlines.csv", index=False, encoding="utf-8")
        logging.info(f"Headline generated: {headline}")
    except Exception as e:
        logging.error(f"Error saving headline: {e}")

# Show history
def show_history():
    if headline_df.empty:
        messagebox.showinfo("History", "No headlines generated yet.")
    else:
        history_text = "\n\n".join(headline_df["Headline"].tolist())
        messagebox.showinfo("Headline History", history_text)

# GUI Setup
root = tk.Tk()
root.title("📰 Fake News Headline Generator")
root.geometry("650x450")
root.config(bg="#e6f2ff")

tk.Label(root, text="Select Category:", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)
category_var = tk.StringVar(value="random")
category_menu = tk.OptionMenu(root, category_var, *subjects.keys())
category_menu.pack()

headline_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), bg="#e6f2ff", fg="darkblue")
headline_label.pack(pady=20)

tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Show History", command=show_history, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=5)

root.mainloop()

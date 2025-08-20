 CODE EXPLAINATION : -


 # 📦 Importing Libraries
import random
- 🔹 Picks random items from a list (like names or actions).

import tkinter as tk
from tkinter import messagebox
- 🔹 Creates a window-based app (GUI).
- 🔹 messagebox shows pop-up messages.

from datetime import datetime
- 🔹 Gets the current date and time.

import pyttsx3
- 🔹 Makes your computer speak the headline.

import pandas as pd
- 🔹 Stores and manages data in table format (like Excel).

import numpy as np
- 🔹 Used for math and numbers (not used yet in this code).

import threading
- 🔹 Runs tasks at the same time (like speaking while GUI stays open).

import logging
- 🔹 Records events in a file (helps with tracking and debugging).

# 🛠️ Setup Logging
logging.basicConfig(filename="headline_generator.log", level=logging.INFO, format="%(asctime)s - %(message)s")
- 🔹 Creates a log file named headline_generator.log.
- 🔹 Saves messages with timestamps.

# 🔊 Initialize Text-to-Speech Engine
engine = pyttsx3.init()
- 🔹 Starts the speech engine to speak headlines.

# 📊 Headline Storage
headline_df = pd.DataFrame(columns=["Timestamp", "Category", "Headline"])
- 🔹 Creates an empty table with 3 columns:
  - 🔹 Timestamp: When the headline was made.
  - 🔹 Category: Type of headline (sports, politics, etc.).
  - 🔹 Headline: The actual sentence.

# 🎭 Headline Components

subjects = {
    "sports": ["Virat Kohli", "Rohit Sharma", "A confused umpire", "A retired cricketer"],
    "politics": ["Prime Minister Modi", "Nirmala Sitharaman", "Rahul Gandhi", "A political analyst"],
    "dance": ["Shahrukh Khan", "A Bollywood choreographer", "A dancing peacock", "A flash mob dancer"],
    "random": ["A Mumbai cat", "A group of monkeys", "Auto rickshaw driver from Delhi", "A tea stall vendor"]
}
- 🔹 These are the main characters in your headline.
- 🔹 Each category has its own list of subjects.

actions = {
    "sports": ["scores century against", "gets bowled over by", "celebrates with", "challenges"],
    "politics": ["declares war on", "debates fiercely with", "tweets angrily about", "orders"],
    "dance": ["performs bhangra with", "joins flash mob at", "dances with", "choreographs"],
    "random": ["eats", "launches", "cancels", "celebrates"]
}
- 🔹 These are the verbs or actions that describe what the subject is doing.

places_or_things = {
    "sports": ["during IPL match", "in cricket stadium", "at India Gate", "on national television"],
    "politics": ["inside Parliament", "at election rally", "on Twitter", "in front of media"],
    "dance": ["on dance reality show", "at Ganga Ghat", "in Mumbai local train", "at Red Fort"],
    "random": ["a plate of samosa", "at tea stall", "at Ganga Ghat", "in Mumbai local train"]
}
- 🔹 These are locations or objects that complete the headline.

# 🧪 Example Headline Construction
# If you randomly choose:
# Subject: "Virat Kohli"
# Action: "scores century against"
# Place: "during IPL match"
# Your headline becomes:
# "Virat Kohli scores century against during IPL match"
# You’ll combine these randomly to make new, funny headlines.

emojis = ["😂", "🤣", "😳", "🤯", "😎", "🙈"]
emoji_weights = [0.2, 0.2, 0.15, 0.15, 0.2, 0.1]  # NumPy will use these for weighted selection
- 🔹 This creates a list of emojis to add fun to your headlines.
- 🔹 emoji_weights defines how likely each emoji is to be picked.
  For example, 😂 and 🤣 have higher chances (0.2), while 🙈 is less likely (0.1).
- 🔹 NumPy will use these weights to randomly choose one emoji.

# Text-to-speech in a separate thread
def speak_text(text):
    threading.Thread(target=lambda: engine.say(text) or engine.runAndWait()).start()
- 🔹 This function makes the computer speak the headline.
- 🔹 It runs in a separate thread so the app doesn’t freeze while speaking.
- 🔹 engine.say(text) prepares the speech, and engine.runAndWait() plays it.

# Generate headline
def generate_headline():
    category = category_var.get()
    - 🔹 Gets the selected category from the GUI (like "sports" or "politics").

    if category not in subjects:
        messagebox.showerror("Error", "Please select a valid category.")
        logging.error("Invalid category selected.")
        return
    - 🔹 Checks if the selected category is valid.
    - 🔹 If not, shows an error message and logs the mistake.

    subject = random.choice(subjects[category])
    action = random.choice(actions[category])
    place_or_thing = random.choice(places_or_things[category])
    emoji = np.random.choice(emojis, p=emoji_weights)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    - 🔹 Picks one random subject, action, and place from the selected category.
    - 🔹 Picks one emoji using the weights.
    - 🔹 Gets the current time in a readable format.

    headline = f"{emoji} [{timestamp}] BREAKING NEWS: {subject} {action} {place_or_thing}"
    headline_label.config(text=headline)
    - 🔹 Combines everything into one funny headline.
    - 🔹 Displays the headline in the GUI using headline_label.

# Speak
speak_text(headline)
- 🔹 This line calls the speak_text function to make the computer say the headline out loud.
- 🔹 It uses text-to-speech in a separate thread, so the app stays responsive while speaking.

# Save to DataFrame
global headline_df
headline_df = pd.concat(
    [headline_df, pd.DataFrame([[timestamp, category, headline]], columns=headline_df.columns)],
    ignore_index=True
)
- 🔹 Declares headline_df as a global variable so it can be updated inside the function.
- 🔹 Creates a new row with the current timestamp, selected category, and generated headline.
- 🔹 pd.DataFrame(...) creates a mini table with just that one row.
- 🔹 pd.concat(...) adds the new row to the existing headline_df table.
- 🔹 ignore_index=True resets the row numbers so they stay in order.

- # Save to file
try:
    headline_df.to_csv("funny_headlines.csv", index=False, encoding="utf-8")
    logging.info(f"Headline generated: {headline}")
except Exception as e:
    logging.error(f"Error saving headline: {e}")

- 🔹 This block tries to save all the headlines into a CSV file named funny_headlines.csv.
- 🔹 headline_df.to_csv(...) writes the DataFrame to a file:
   - "funny_headlines.csv" is the file name.
   - index=False means it won’t include row numbers in the file.
   - encoding="utf-8" ensures special characters (like emojis) are saved correctly.
- 🔹 logging.info(...) records a success message in the log file.
- 🔹 If something goes wrong (like file permission issues), the except block catches the error.
- 🔹 logging.error(...) saves the error message in the log file for debugging.

- # Show history
def show_history():
    if headline_df.empty:
        messagebox.showinfo("History", "No headlines generated yet.")
    else:
        history_text = "\n\n".join(headline_df["Headline"].tolist())
        messagebox.showinfo("Headline History", history_text)

- 🔹 This function displays all the previously generated headlines in a pop-up window.
- 🔹 It first checks if the DataFrame headline_df is empty:
   - If yes, it shows a message saying "No headlines generated yet."
- 🔹 If there are headlines:
   - headline_df["Headline"].tolist() gets all the headlines as a list.
   - "\n\n".join(...) joins them with double line breaks for better readability.
   - messagebox.showinfo(...) displays the headlines in a pop-up titled "Headline History".
 
- # GUI Setup
root = tk.Tk()
- 🔹 Creates the main window for your app.

root.title("📰 Fake News Headline Generator")
- 🔹 Sets the title of the window (shown at the top).

root.geometry("650x450")
- 🔹 Sets the size of the window: 650 pixels wide and 450 pixels tall.

root.config(bg="#e6f2ff")
- 🔹 Sets the background color of the window to a light blue shade.

tk.Label(root, text="Select Category:", font=("Arial", 14), bg="#e6f2ff").pack(pady=10)
- 🔹 Adds a label that says "Select Category:".
- 🔹 Uses Arial font, size 14, and matches the background color.
- 🔹 pady=10 adds vertical space around the label.

category_var = tk.StringVar(value="random")
- 🔹 Creates a variable to store the selected category.
- 🔹 Default value is set to "random".

category_menu = tk.OptionMenu(root, category_var, *subjects.keys())
category_menu.pack()
- 🔹 Creates a dropdown menu with category options (like sports, politics).
- 🔹 Uses the keys from the subjects dictionary.
- 🔹 .pack() places it in the window.

headline_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), bg="#e6f2ff", fg="darkblue")
headline_label.pack(pady=20)
- 🔹 Adds a label to show the generated headline.
- 🔹 wraplength=550 ensures long headlines wrap within the window.
- 🔹 fg="darkblue" sets the text color.

tk.Button(root, text="Generate Headline", command=generate_headline, font=("Arial", 12)).pack(pady=5)
- 🔹 Adds a button labeled "Generate Headline".
- 🔹 When clicked, it runs the generate_headline function.

tk.Button(root, text="Show History", command=show_history, font=("Arial", 12)).pack(pady=5)
- 🔹 Adds a button labeled "Show History".
- 🔹 When clicked, it shows all previously generated headlines.

tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=5)
- 🔹 Adds an "Exit" button to close the app.

root.mainloop()
- 🔹 Starts the GUI event loop.
- 🔹 Keeps the window open and responsive until the user closes it.





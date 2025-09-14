import tkinter as tk
import random
WORDS = ["apple", "banana", "grape", "orange", "mango",
         "cherry", "peach", "lemon"]
class HangmanGame:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed = ["_"] * len(self.word)
        self.attempts = 4
        self.used = set()
    def guess(self, letter):
        if letter in self.used or not letter.isalpha() or len(letter) != 1:
            return "invalid"
        self.used.add(letter)
        if letter in self.word:
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.guessed[i] = letter
            return "won" if "_" not in self.guessed else "correct"
        else:
            self.attempts -= 1
            return "lost" if self.attempts == 0 else "wrong"
class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.game = HangmanGame()
        self.word_label = tk.Label(root, text=" ".join(self.game.guessed), font=("Arial", 24))
        self.word_label.pack(pady=20)
        self.status_label = tk.Label(root, text=f"Attempts left: {self.game.attempts}", font=("Arial", 14))
        self.status_label.pack()
        self.message_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
        self.message_label.pack(pady=10)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.buttons = {}
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            btn = tk.Button(self.button_frame, text=letter, width=4, height=2,
                            command=lambda l=letter: self.make_guess(l))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)
            self.buttons[letter] = btn
    def make_guess(self, letter):
        result = self.game.guess(letter)
        self.word_label.config(text=" ".join(self.game.guessed))
        self.status_label.config(text=f"Attempts left: {self.game.attempts}")
        self.buttons[letter].config(state="disabled")
        if result == "won":
            self.message_label.config(text="🎉You won!", fg="green")
            self.disable_buttons()
        elif result == "lost":
            self.message_label.config(text=f"💀You lost! Word was: {self.game.word}", fg="red")
            self.disable_buttons()
    def disable_buttons(self):
        for btn in self.buttons.values():
            btn.config(state="disabled")
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
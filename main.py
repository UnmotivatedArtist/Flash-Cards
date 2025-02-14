import tkinter as tk
from tkinter import messagebox
import json
import random

root = tk.Tk()  

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("600x600")

        self.flashcards = []
        self.current_index = 11
        self.show_answer = False

        self.load_flashcards()

        self.flashcard_frame = tk.Frame(root, bg="white")
        self.flashcard_frame.pack(pady=20)

        self.question_label = tk.Label(self.flashcard_frame, text="", font=("Arial", 24), wraplength=500)
        self.question_label.pack(pady=20)

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_flashcard)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_flashcard)
        self.next_button.pack(side=tk.RIGHT, padx=20)

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_flashcard)
        self.prev_button.pack(side=tk.LEFT, padx=20)

        self.shuffle_button = tk.Button(root, text="Shuffle", command=self.shuffle_flashcards)
        self.shuffle_button.pack(pady=10)

        self.display_flashcard()

    def load_flashcards(self):
        try:
            with open("/c:/Users/thomas.ross_searcysc/Documents/VS Code/Flash Cards/flashcards.json", "r") as file:
                self.flashcards = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Flashcards file not found!")
        except json.JSONDecodeError as e:
            messagebox.showerror("Error", f"Error decoding JSON file: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")")

    def display_flashcard(self):
        if self.flashcards:
            flashcard = self.flashcards[self.current_index]
            if self.show_answer:
                self.question_label.config(text=flashcard["answer"])
            else:
                self.question_label.config(text=flashcard["question"])

    def flip_flashcard(self):
        self.show_answer = not self.show_answer
        self.display_flashcard()

    def next_flashcard(self):
        self.current_index = (self.current_index + 1) % len(self.flashcards)
        self.show_answer = False
        self.display_flashcard()

    def prev_flashcard(self):
        self.current_index = (self.current_index - 1) % len(self.flashcards)
        self.show_answer = False
        self.display_flashcard()

    def shuffle_flashcards(self):
        random.shuffle(self.flashcards)
        self.current_index = 0
        self.show_answer = False
        self.display_flashcard()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
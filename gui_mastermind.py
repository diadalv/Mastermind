import customtkinter as ctk
import random
from tkinter import messagebox

# Configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

COLORS = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple"]

class MastermindApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("HOU Mastermind Project")
        self.geometry("800x700")
        
        # This variable will hold our secret code later
        self.secret_code = []

        # Start the app by showing the menu
        self.show_main_menu()

    def clear_window(self):
        """Removes all widgets from the current window."""
        for widget in self.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """Displays the starting screen."""
        self.clear_window()
        
        self.label = ctk.CTkLabel(self, text="MASTERMIND", font=("Roboto", 32, "bold"))
        self.label.pack(pady=(60, 10))

        self.sub_label = ctk.CTkLabel(self, text="Select your game mode", font=("Roboto", 14))
        self.sub_label.pack(pady=(0, 30))

        # Maker Button
        self.maker_button = ctk.CTkButton(self, text="Code Maker", 
                                          command=self.start_maker_mode,
                                          corner_radius=10, height=45)
        self.maker_button.pack(pady=10)

        # Breaker Button
        self.breaker_button = ctk.CTkButton(self, text="Code Breaker", 
                                            command=self.start_breaker_mode,
                                            corner_radius=10, height=45)
        self.breaker_button.pack(pady=10)
        # --- Info Buttons ---
        # We use a different color (grey) for secondary options
        self.rules_button = ctk.CTkButton(self, text="Game Rules", 
                                          fg_color="#565b5e", hover_color="#3e4144",
                                          command=self.show_rules)
        self.rules_button.pack(pady=10)

        self.history_button = ctk.CTkButton(self, text="Game History", 
                                            fg_color="#565b5e", hover_color="#3e4144",
                                            command=self.show_history)
        self.history_button.pack(pady=10)

    def show_rules(self):
        self.clear_window()
        
        ctk.CTkLabel(self, text="How to Play", font=("Roboto", 24, "bold")).pack(pady=20)

        # Create a scrollable text box for rules
        rules_text = (
            "1. The Code Maker sets a secret code of 4 colors.\n"
            "2. The Code Breaker has 10 attempts to guess the code.\n"
            "3. After each guess, the Maker provides feedback:\n"
            "   - Red Peg: Correct color in the correct position.\n"
            "   - White Peg: Correct color in the wrong position.\n"
            "4. Win by guessing the exact code before running out of turns!"
        )
        
        textbox = ctk.CTkTextbox(self, width=500, height=200)
        textbox.insert("0.0", rules_text)
        textbox.configure(state="disabled") # Make it read-only
        textbox.pack(pady=10)

        ctk.CTkButton(self, text="Back to Menu", command=self.show_main_menu).pack(pady=20)

    def show_history(self):
        self.clear_window()
        
        ctk.CTkLabel(self, text="History of Mastermind", font=("Roboto", 24, "bold")).pack(pady=20)

        history_info = (
            "Mastermind is a code-breaking game for two players. "
            "The modern game with pegs was invented in 1970 by Mordecai Meirowitz, "
            "an Israeli postmaster and telecommunications expert.\n\n"
            "It resembles an earlier pencil and paper game called Bulls and Cows."
        )

        textbox = ctk.CTkTextbox(self, width=500, height=200)
        textbox.insert("0.0", history_info)
        textbox.configure(state="disabled")
        textbox.pack(pady=10)

        ctk.CTkButton(self, text="Back to Menu", command=self.show_main_menu).pack(pady=20)    

    def start_maker_mode(self):
        self.clear_window()
        label = ctk.CTkLabel(self, text="Mode: Code Maker", font=("Roboto", 18))
        label.pack(pady=20)
        
        # Add a back button
        ctk.CTkButton(self, text="Back to Menu", command=self.show_main_menu).pack(side="bottom", pady=20)

    def start_breaker_mode(self):
        self.clear_window()
        
        # Generate the secret code
        self.secret_code = [random.choice(COLORS) for _ in range(4)]
        print(f"Secret Code generated: {self.secret_code}") # For debugging

        self.setup_game_board()

    def setup_game_board(self):
        """Draws the board for the Breaker mode."""
        label = ctk.CTkLabel(self, text="Guess the 4-color code!", font=("Roboto", 20, "bold"))
        label.pack(pady=20)

        # Placeholder for the game board rows
        self.board_frame = ctk.CTkFrame(self)
        self.board_frame.pack(pady=10, fill="both", expand=True)

        # Add a back button
        ctk.CTkButton(self, text="Quit Game", command=self.show_main_menu).pack(side="bottom", pady=20)

if __name__ == "__main__":
    app = MastermindApp()
    app.mainloop()
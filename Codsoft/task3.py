from tkinter import *
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.configure(background="#e2f046")

        # Creating a frame for the heading
        heading_frame = Frame(self.master, bg="#e2f046")
        heading_frame.grid(row=0, column=0, columnspan=7)

        # Heading
        self.load_images()

        self.user_choice_label = Label(self.master, image=self.scissor_hu, bg="#e2f046")
        self.comp_choice_label = Label(self.master, image=self.scissor_img, bg="#e2f046")
        self.comp_choice_label.grid(row=1, column=0)
        self.user_choice_label.grid(row=1, column=4)

        self.user_score_label = Label(self.master, text="User Score: 0", font=("Helvetica", 14), bg="#e2f046")
        self.comp_score_label = Label(self.master, text="Computer Score: 0", font=("Helvetica", 14), bg="#e2f046")
        self.user_score_label.grid(row=0, column=4, columnspan=2, padx=10)
        self.comp_score_label.grid(row=0, column=0, columnspan=2)

        self.user_score = 0
        self.comp_score = 0

        self.create_buttons()

        self.result_label = Label(self.master, text="", font=("Helvetica", 14), bg="#e2f046")
        self.result_label.grid(row=3, columnspan=7)

    def load_images(self):
        self.rock_img = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\rock.png"))
        self.paper_img = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\paper.png"))
        self.scissor_img = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\scissors1.png"))
        self.rock_hu = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\rock_human.png"))
        self.paper_hu = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\paper_human.png"))
        self.scissor_hu = ImageTk.PhotoImage(Image.open("C:\\Users\\User\\Downloads\\Codsoft\\scissors_human.png"))

    def create_buttons(self):
        choices = {"rock": self.rock_img, "paper": self.paper_img, "scissors1": self.scissor_img}
        human_choices = {"rock": self.rock_hu, "paper": self.paper_hu, "scissors1": self.scissor_hu}

        rock_btn = Button(self.master, text="Rock", bd=5, bg="green", width=10, height=2, fg="white",
                          command=lambda: self.play("rock", choices, human_choices))
        paper_btn = Button(self.master, text="Paper", bd=5, bg="#fc5603", width=10, height=2, fg="white",
                           command=lambda: self.play("paper", choices, human_choices))
        scissor_btn = Button(self.master, text="Scissors", bd=5, bg="#15d64c", width=10, height=2, fg="white",
                             command=lambda: self.play("scissors1", choices, human_choices))

        rock_btn.grid(row=2, column=1)
        paper_btn.grid(row=2, column=2)
        scissor_btn.grid(row=2, column=3)

    def get_comp_choice(self):
        return random.choice(["rock", "paper", "scissors1"])

    def play(self, choice, choices, human_choices):
        comp_choice = self.get_comp_choice()
        self.user_choice_label.configure(image=human_choices[choice])
        self.comp_choice_label.configure(image=choices[comp_choice])

        if choice == comp_choice:
            self.result_label.config(text="It's a tie!")
        elif (
                (choice == "rock" and comp_choice == "scissors1")
                or (choice == "paper" and comp_choice == "rock")
                or (choice == "scissors1" and comp_choice == "paper")
        ):
            self.result_label.config(text="You win!")
            self.user_score += 1
        else:
            self.result_label.config(text="Computer wins!")
            self.comp_score += 1

        self.update_scores()

    def update_scores(self):
        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.comp_score_label.config(text=f"Computer Score: {self.comp_score}")

if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    game = RockPaperScissorsGame(root)

    root.mainloop()
